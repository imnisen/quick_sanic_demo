from sanic import Sanic
from asyncpg import create_pool
from aioredis import create_redis_pool
from sanic_session import RedisSessionInterface
from app.views import all_views
import asyncio_redis
from config import pg_config, redis_config, redis_cache_config
from utils import logging_config
from utils import request_logger as logger

app = Sanic('sanic_api', log_config=logging_config)


@app.listener('before_server_start')
async def init_setup(app, loop):
    """服务启动前设置数据库连接池"""

    # 设置 postgres pool
    pg_pool = await create_pool(host=pg_config.get('host', '127.0.0.1'),
                                port=pg_config.get('port', 5432),
                                database=pg_config.get('db', None),
                                user=pg_config.get('user', 'postgres'),
                                password=pg_config.get('password', 'postgres'),
                                min_size=pg_config.get('min_size', '10'),
                                max_size=pg_config.get('max_size', '20'),
                                loop=loop)
    app.pg_pool = pg_pool

    # 设置一般缓存的redis pool
    redis_pool = await create_redis_pool(address=(redis_config.get('host', '127.0.0.1'),
                                                  redis_config.get('port', 6379)),
                                         db=redis_config.get('db', 1),
                                         loop=loop)
    app.redis_pool = redis_pool

    # 设置session使用的redis pool
    redis_cache_pool = await asyncio_redis.Pool.create(host=redis_cache_config.get('host', '127.0.0.1'),
                                                       port=redis_cache_config.get('port', 6379),
                                                       poolsize=10,
                                                       db=redis_cache_config.get('db', 1),
                                                       loop=loop)
    app.redis_cache_pool = redis_cache_pool


@app.listener('after_server_stop')
async def clean_up(app, loop):
    """系统停止后关闭相关数据库连接"""
    await app.pg_pool.close()

    app.redis_pool.close()
    app.redis_cache_pool.close()


########################################
# 设置请求和返回的中间件
########################################
async def redis_cache_pool_getter():
    """辅助函数"""
    return app.redis_cache_pool


session_interface = RedisSessionInterface(redis_cache_pool_getter)


@app.middleware('request')
async def add_session_to_request(request):
    """给请求添加session"""
    await session_interface.open(request)


@app.middleware('response')
async def add_log(request, response):
    """给请求的返回结果添加log"""
    logger.info('REQUEST,{},{},{},{},RESPONSE,{},{}'.format(request.path,
                                                            request.method,
                                                            request.args,
                                                            request.body.decode(),
                                                            response.status,
                                                            response.body.decode()))


@app.middleware('response')
async def save_session(request, response):
    """保存session到redis, 生成相应的cookie"""
    await session_interface.save(request, response)


########################################
# 注册路由
########################################
for bp in all_views:
    app.blueprint(bp)

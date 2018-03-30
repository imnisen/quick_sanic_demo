import configparser

# 初始化
config = configparser.ConfigParser()
config.read("config/config.ini")

sanic_config = {
    'host': config.get('sanic_config', 'host'),
    'port': config.getint('sanic_config', 'port'),
    'debug': config.getboolean('sanic_config', 'debug'),
    'workers': config.getint('sanic_config', 'workers'),
}

pg_config = {
    'host': config.get('pg_config', 'host'),
    'port': config.getint('pg_config', 'port'),
    'db': config.get('pg_config', 'db'),
    'user': config.get('pg_config', 'user'),
    'password': config.get('pg_config', 'password'),
    'min_size': config.getint('pg_config', 'min_size'),
    'max_size': config.getint('pg_config', 'max_size'),

}

redis_config = {
    'host': config.get('redis_config', 'host'),
    'port': config.getint('redis_config', 'port'),
    'db': config.getint('redis_config', 'db'),
    'password': config.get('redis_config', 'password'),
}

redis_cache_config = {
    'host': config.get('redis_cache_config', 'host'),
    'port': config.getint('redis_cache_config', 'port'),
    'db': config.getint('redis_cache_config', 'db'),
    'password': config.get('redis_cache_config', 'password'),
}


__all__ = [
    'server_config',
    'pg_config',
    'redis_config',
    'redis_cache_config',
]

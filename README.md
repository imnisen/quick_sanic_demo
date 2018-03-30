# 安装
```
pip3 install -r requirements.txt
```

# 启动
## 本地启动
```
# config/config.bak 复制成 config/config.ini , 并且配置启动参数

# 运行服务
python3 run.py
```
## docker启动
```
docker-compose up
```

# 项目说明
## 文件结构
- app 业务相关代码
    - main.py  sanic服务相关配置
    - views    业务接口
- test 测试代码
- utils 常用工具
    - decorators.py 装饰器类工具
    - exceptions.py 自定义异常
    - log.py 自定义日志
- config 配置文件
- run.py 启动文件

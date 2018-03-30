#!/bin/bash

# 如果发生错误则退出执行
set -e

## set the postgres database host, port, user and password according to the environment
## and pass them as arguments to the odoo process if not present in the config file
## 要么从环境变量取值,要么设为默认值
#: ${HOST:=${DB_PORT_5432_TCP_ADDR:='db'}}
#: ${PORT:=${DB_PORT_5432_TCP_PORT:=5432}}
#: ${USER:=${DB_ENV_POSTGRES_USER:=${POSTGRES_USER:='odoo'}}}
#: ${PASSWORD:=${DB_ENV_POSTGRES_PASSWORD:=${POSTGRES_PASSWORD:='odoo'}}}
#
#
## 读取配置文件到DB_ARGS
#DB_ARGS=()
#function check_config() {
#    param="$1"
#    value="$2"
#    if ! grep -q -E "^\s*\b${param}\b\s*=" "$OPENERP_SERVER" ; then
#        DB_ARGS+=("--${param}")
#        DB_ARGS+=("${value}")
#   fi;
#}
#check_config "db_host" "$HOST"
#check_config "db_port" "$PORT"
#check_config "db_user" "$USER"
#check_config "db_password" "$PASSWORD"
#
#case "$1" in
#    -- | openerp-server)
#        shift
#        if [[ "$1" == "scaffold" ]] ; then
#            exec openerp-server "$@"
#        else
#            exec openerp-server "$@" "${DB_ARGS[@]}"
#        fi
#        ;;
#    -*)
#        exec openerp-server "$@" "${DB_ARGS[@]}"
#        ;;
#    *)
#        exec "$@"
#esac

# 用环境变量来修改config文件
: ${SANIC_HOST:='0.0.0.0'}
: ${SANIC_PORT:=6623}
: ${SANIC_DEBUG:=false}
: ${SANIC_WORKER:=1}

: ${POSTGRES_HOST:='127.0.0.1'}
: ${POSTGRES_PORT:=5432}
: ${POSTGRES_DB:='test-db-1'}
: ${POSTGRES_USER:='nisen'}
: ${POSTGRES_PASSWORD:='nisen123'}

: ${REDIS_HOST:='127.0.0.1'}
: ${REDIS_PORT:=6379}
: ${REDIS_DB:=1}

: ${REDIS_CACHE_HOST:='127.0.0.1'}
: ${REDIS_CACHE_PORT:=6379}
: ${REDIS_CACHE_DB:=2}

sed -i "s/SANIC_HOST/$SANIC_HOST/g" /opt/config/config.ini
sed -i "s/SANIC_PORT/$SANIC_PORT/g" /opt/config/config.ini
sed -i "s/SANIC_DEBUG/$SANIC_DEBUG/g" /opt/config/config.ini
sed -i "s/SANIC_WORKER/$SANIC_WORKER/g" /opt/config/config.ini

sed -i "s/POSTGRES_HOST/$POSTGRES_HOST/g" /opt/config/config.ini
sed -i "s/POSTGRES_PORT/$POSTGRES_PORT/g" /opt/config/config.ini
sed -i "s/POSTGRES_DB/$POSTGRES_DB/g" /opt/config/config.ini
sed -i "s/POSTGRES_USER/$POSTGRES_USER/g" /opt/config/config.ini
sed -i "s/POSTGRES_PASSWORD/$POSTGRES_PASSWORD/g" /opt/config/config.ini

sed -i "s/REDIS_HOST/$REDIS_HOST/g" /opt/config/config.ini
sed -i "s/REDIS_PORT/$REDIS_PORT/g" /opt/config/config.ini
sed -i "s/REDIS_DB/$REDIS_DB/g" /opt/config/config.ini

sed -i "s/REDIS_CACHE_HOST/$REDIS_CACHE_HOST/g" /opt/config/config.ini
sed -i "s/REDIS_CACHE_PORT/$REDIS_CACHE_PORT/g" /opt/config/config.ini
sed -i "s/REDIS_CACHE_DB/$REDIS_CACHE_DB/g" /opt/config/config.ini

cd /opt

exec python3 run.py

exit 1

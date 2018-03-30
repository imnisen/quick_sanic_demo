import logging
import sys


logging_config = dict(
    version=1,
    disable_existing_loggers=False,

    loggers={
        "root": {
            "level": "INFO",
            "handlers": ["console"]
        },

        "sanic.error": {
            "level": "INFO",
            "handlers": ["error_console"],
            "propagate": True,
            "qualname": "sanic.error"
        },

        "sanic.access": {
            "level": "INFO",
            "handlers": ["access_console"],
            "propagate": True,
            "qualname": "sanic.access"
        },

        # 自已定义的logger
        "request_logger": {
            "level": "INFO",
            "handlers": ["request_handlers"],
            "propagate": True,
        }

    },
    handlers={
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stdout
        },
        "error_console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stderr
        },
        "access_console": {
            "class": "logging.StreamHandler",
            "formatter": "access",
            "stream": sys.stdout
        },

        # 自已定义的handlers
        "request_handlers": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stdout
        },


    },
    formatters={
        "generic": {
            "format": "%(asctime)s - (%(name)s) [%(process)d] [%(levelname)s] : %(message)s",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        },
        "access": {
            "format": "%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: " +
                      "%(request)s %(message)s %(status)d %(byte)d",
            "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
            "class": "logging.Formatter"
        },

        # 暂时不需要
        # # 自已定义的handlers
        # "request_formatter": {
        #     "format": "%(asctime)s - (%(name)s) [%(process)d] [%(levelname)s] %(message)s",
        #     "datefmt": "[%Y-%m-%d %H:%M:%S %z]",
        #     "class": "logging.Formatter"
        # },
    }
)


logger = logging.getLogger('root')
error_logger = logging.getLogger('sanic.error')
access_logger = logging.getLogger('sanic.access')

# 供业务使用的logger
request_logger = logging.getLogger('request_logger')

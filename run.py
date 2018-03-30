from config import sanic_config
from app.main import app

app.run(host=sanic_config.get('host', '0.0.0.0'),
        port=sanic_config.get('port', 8000),
        debug=sanic_config.get('debug', False),
        workers=sanic_config.get('workers', 1))

from api import main
from api.config import DevConfig

app = main.create_app(config_object=DevConfig)

if __name__ == '__main__':
    app.run()
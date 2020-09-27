import os

import app

# os variable is set for development
config_name = os.getenv("APP_SETTINGS")
app = app.create_app(config_name)


if __name__ == "__main__":
    app.run()

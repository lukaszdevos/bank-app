import os

import app

config_name = os.getenv("APP_SETTINGS")
app = app.create_app(config_name)

if __name__ == "__main__":
    app.run(port=8000)

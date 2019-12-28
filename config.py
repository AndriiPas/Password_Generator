import os


class Config:
    SECRET_KEY = 'secret_key'
    PG_USER = os.environ.get("PG_USER", "pas")
    PG_PASSWORD = os.environ.get("PG_PASSWORD", "123")
    PG_HOST = os.environ.get("PG_HOST", "localhost")
    PG_PORT = os.environ.get("PG_PORT", 5432)
    DB_NAME = os.environ.get("DB_NAME", "users")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig:
    SECRET_KEY = 'secret_key1'


def run_config():
    env = os.environ.get("ENV")
    if env == "TEST":
        return TestConfig
    else:
        return Config

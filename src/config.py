from pathlib import Path
from dynaconf import Dynaconf

PROJECT_ROOT = Path(__file__).parents[2]  # настройка пути к корню проекта для работы со статическими файлами

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.

settings = Dynaconf(
    envvar_prefix="FASTAPI_DEMO",
    settings_files=['settings.toml', '.secrets.toml'],
)


def get_settings() -> Dynaconf:
    return settings
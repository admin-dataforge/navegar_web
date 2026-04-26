from pathlib import Path

import yaml


def leer_config(path_config: str):
    ruta = Path(path_config).expanduser().resolve()

    if not ruta.exists():
        raise FileNotFoundError(f"No existe el archivo: {ruta}")

    if not ruta.is_file():
        raise ValueError(f"La ruta no es un archivo válido: {ruta}")

    with open(ruta, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return data

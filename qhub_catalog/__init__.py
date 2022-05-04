from pathlib import Path
from intake import open_catalog

__all__ = ("catalog",)


THIS = Path(__file__).parent
CATALOG = THIS / "qhub_catalog.yml"
catalog = open_catalog(CATALOG)

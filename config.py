
from pathlib import Path

QUERIES_PATH = Path(__file__).resolve().parent / 'database' / 'queries.sql'
DB_CONNECT = f"postgresql://postgres:{'manager1'}@localhost:5432/cw5"
EMPLOYER_MAP = {
    "РутКод": 8642172,
    "AVC": 1626408,
    "МЕТИНВЕСТ": 2596438,
    "ФИНТЕХ": 2324020,
    "ОКБ": 2129243,
}



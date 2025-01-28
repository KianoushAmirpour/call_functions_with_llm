import pathlib

ROOT_DIR = pathlib.Path(__file__).parent
DATASET_PATH = ROOT_DIR / 'data' / 'purchase.csv'

DATABASE_PATH = ROOT_DIR / 'db' /'purchase.db'
TABLE_NAME: str = 'purchase' 

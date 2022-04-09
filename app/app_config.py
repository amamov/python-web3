from pathlib import Path
from dotenv import load_dotenv, dotenv_values
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

load_dotenv()
env = {**dotenv_values(".env")}

BASE_DIR = Path(__file__).resolve().parent
NETWORK_RPC_URI = "https://rpc-mumbai.matic.today"

templates = Jinja2Templates(directory=BASE_DIR / "templates")
static_files = StaticFiles(directory=BASE_DIR / "static")

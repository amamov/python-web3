from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.staticfiles import StaticFiles
from web3 import Web3
from web3.providers.rpc import HTTPProvider


class AppConfig:
    BASE_DIR = Path(__file__).resolve().parent
    NETWORK_RPC_URI = "https://matic-testnet-archive-rpc.bwarelabs.com"


app = FastAPI()
templates = Jinja2Templates(directory=AppConfig.BASE_DIR / "templates")
app.mount(
    "/static", StaticFiles(directory=AppConfig.BASE_DIR / "static"), name="static"
)


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "./index.html",
        {"request": request},
    )


class Account(BaseModel):
    account: str


@app.post("/web3")
async def index(req: Account):
    print(req.account)
    account = req.account
    w3 = Web3(HTTPProvider(AppConfig.NETWORK_RPC_URI))
    print(w3.isConnected())
    return {"account": account}


#  poetry run uvicorn app.main:app --reload

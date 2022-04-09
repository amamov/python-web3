from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from web3 import Web3
from web3.providers.rpc import HTTPProvider
from .app_config import static_files, templates, NETWORK_RPC_URI


app = FastAPI()
app.mount("/static", static_files, name="static")


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
    w3 = Web3(HTTPProvider(NETWORK_RPC_URI))
    print(w3.isConnected())
    return {"account": account}


#  poetry run uvicorn app.main:app --reload

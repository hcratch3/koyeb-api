from fastapi import FastAPI
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import os

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/mail/")
def read_item(to: str, subject: str, body: str = None):
    sendAddress = os.environ.get("sendAddress")
    password = os.environ.get("password")

    fromAddress = 'noreply.hcratch3@gmail.com'

    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(sendAddress, password)

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = fromAddress
    msg['To'] = to
    msg['Date'] = formatdate()

    # 作成したメールを送信
    smtpobj.send_message(msg)
    smtpobj.close()

    return {"status":"200","msg":"success"}

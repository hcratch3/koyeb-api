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
    return {"status":"200","msg":"Prease read docs. ==>> <APIURL>/docs"}


@app.get("/about/")
def read_item():
    return {"status":"200", "msg":"Product by @hcratch3(https://github.com/hcratch3) (c)2025 hcratch3 / License : https://www.gnu.org/licenses/agpl-3.0.html#license-text"}

@app.get("/mail/")
def read_item(to: str, subject: str, body: str = None):
    sendAddress = os.environ.get("sendAddress")
    password = os.environ.get("password")

    if not body:
        body = "NO REPLY"

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

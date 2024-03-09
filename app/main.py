from typing import Annotated
import base64
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(file_name: Annotated[str, Form()], file: Annotated[str, Form()]):
    file_content=base64.b64decode(file)
    with open("/app/storage/" + file_name,"w+") as f:
        f.write(file_content.decode("utf-8"))
    return {"username": file_name}
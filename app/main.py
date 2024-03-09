from typing import Annotated
import base64
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(file_name: Annotated[str, Form()], file: Annotated[str, Form()]):
    wav_file = open("./app/storage/" + str(file_name), "wb")
    decode_string = base64.b64decode(str(file))
    wav_file.write(decode_string)
    return {"username": file_name}
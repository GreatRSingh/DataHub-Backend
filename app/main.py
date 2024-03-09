from typing import Annotated

from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(file_name: Annotated[str, Form()], file: Annotated[str, Form()]):
    return {"username": file_name}
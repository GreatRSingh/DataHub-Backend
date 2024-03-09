from fastapi import FastAPI
import base64

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/audio-dump")
def audio_dump(file_name: str, file: str):
    try:
        wav_file = open("./app/storage/"+file_name, "wb")
        decode_string = base64.b64decode(file)
        wav_file.write(decode_string)
        return {"message": "File saved"}
    except Exception as e:
        return {"error": e}
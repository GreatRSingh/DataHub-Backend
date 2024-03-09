import base64

encode_string = base64.b64encode(open("./app/storage/_0_260.jpeg", "rb").read())
wav_file = open("./temp.jpeg", "wb")
decode_string = base64.b64decode(encode_string)
wav_file.write(decode_string)

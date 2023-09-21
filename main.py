from fastapi import FastAPI
import shortlink
from fastapi.responses import RedirectResponse
import os

if 'HOST_URL' in os.environ:
    host_url = os.environ['HOST_URL']
else:
    host_url = 'https://127.0.0.1:8000'

app = FastAPI()

@app.get("/createShortURL")
def shortURL(url: str,key = False,length:int = 5):
    outputURL = host_url + "/" + str(shortlink.createURL(url,key,length))
    output = { "url": outputURL,
               "longURL" : url
              }

    return output


@app.get("/{key}", response_class=RedirectResponse, status_code=302)
async def redirect_short2Long(key):
    if key!= None and shortlink.keyExists(key) == True:
        return shortlink.getURL(key)
    else:
        return {"error": f"unknown key {key}"}




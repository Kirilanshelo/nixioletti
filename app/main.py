from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

import os
import logging

from utils.log import init_log
from aitask.ocr import do_task
# from miniui.miniui import do_api_task
from miniui.datamodel import MyModel

VERSION = os.environ.get('VERSION', 'dev-version')
LOGFILE = os.environ.get('LOGILE', 'app.log')
LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG')

init_log(LOGFILE, LOGLEVEL)
log = logging.getLogger('app')
log.info('App starting...')

app = FastAPI()


# management

@app.get("/version")
async def get_version():
    return JSONResponse({"version": VERSION})

@app.get("/status")
async def get_status():
    return JSONResponse({"status": "online"})


# task

# @app.get("/mytask")
# async def my_task():
#     data = do_task()
#     return JSONResponse(data)

# @app.post("/rotto")
# async def rotto(body: MyModel):
#     print(body)
#     if isinstance(body.value, float):
#         val = body.value / 3
#         status_code = 200
#         data = {'val':val}
#         return JSONResponse(data, status_code=status_code)
#     else:
#         status_code = 400
#         data = {'lavora':'meglio'}
#         return JSONResponse(data, status_code=status_code)

# miniui

@app.post("/miniui/api")
async def get_api(body: MyModel):
    data = do_task(body)
    return JSONResponse(data)

@app.get("/miniui/ui")
async def get_ui(request: Request):
    with open('miniui/templates/miniui.html') as fi:
        html_content = fi.read()
    return HTMLResponse(content=html_content, status_code=200)

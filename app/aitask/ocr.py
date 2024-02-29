import pandas as pd
import easyocr
import cv2
import numpy as np
import easyocr
import re
import base64
from PIL import Image
from io import BytesIO
import logging
log = logging.getLogger('mylib')

def do_task(body):
  img = re.search('base64,(.*)',body.base64).group(1)
  img = Image.open(BytesIO(base64.b64decode(img)))
  img = np.array(img)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  noise=cv2.medianBlur(gray,3)
  thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
  reader = easyocr.Reader(['it'], gpu=False)
  result = reader.readtext(img,paragraph="False")
  df=pd.DataFrame(result)
  output = {'data': f'{df[1][0]}'}
  log.info(f'ai task done')
  return output
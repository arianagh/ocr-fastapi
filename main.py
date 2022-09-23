import shutil

import pytesseract
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post('/ocr')
def ocr_file(image: UploadFile = File(...)):
    filepath = 'txtfile'
    with open(filepath, mode='w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return pytesseract.image_to_string(filepath, lang='eng')

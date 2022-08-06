from fastapi import APIRouter, FastAPI
from config.db import collection_name
from models.covidData_model import Cases
from schema.covidData_schema import covidData_serializer, covidDatas_serializer
from fastapi.responses import FileResponse
import os

router = APIRouter()
app = FastAPI()

@router.get('/healthCheck')
async def doHealthCheck():
   return {"status": "Application running"}
   
@router.get('/getCovidData')
async def getData():
     data = covidDatas_serializer(collection_name.find())
     return {"data": data}

@app.get('/favicon.ico')
async def favicon():
    file_name = "favicon.png"
    file_path = os.path.join(app.root_path, "images")
    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})
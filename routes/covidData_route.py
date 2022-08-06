from fastapi import APIRouter
from config.db import collection_name
from models.covidData_model import Cases
from schema.covidData_schema import covidData_serializer, covidDatas_serializer
from pymongo import MongoClient

router = APIRouter()

@router.get('/healthCheck')
def doHealthCheck():
   return {"status": "Application running"}
   
@router.get('/getCovidData')
def getData():
     data = covidDatas_serializer(collection_name.find())
     return {"data": data}
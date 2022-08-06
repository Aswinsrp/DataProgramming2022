from fastapi import FastAPI
from routes.covidData_route import router

app = FastAPI()
app.include_router(router)



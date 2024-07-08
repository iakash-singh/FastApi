# from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from pymongo import MongoClient

app = FastAPI()


conn = MongoClient("mongodb+srv://test:akash123@mongo.rfh4yc0.mongodb.net/")




# python3 -m uvicorn server:app --reload
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

script_dir = os.path.dirname(__file__)
print(script_dir)
rel_path = "data/mapimages/"
abs_file_path = os.path.join(script_dir, rel_path)
# print(abs_file_path)

@app.get('/')
def main():
    return "Hello world"

@app.get('/images',response_class=FileResponse)
async def images(z: str, x: str, y: str):

    return image

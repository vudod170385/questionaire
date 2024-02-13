from fastapi import FastAPI, Request
from predict import generate_question_answer
import json
import urllib.parse
import uvicorn
import os




app = FastAPI(debug=True)


def process(data):

    output = generate_question_answer(data['text'], data['num_question'], data['domain'],data['requirement'])

    return output

def generate_response(json_data, output):
    return {
        "input": str(json_data),
        "output": str(output),
    }



@app.get("/")
async def root():
    return {"message": "Generate Question and Answer"}

@app.post("/predict")
async def predict_review(data: Request):
    json_data = await data.json()
    place = process(json_data)

    return generate_response(json_data, place)


@app.get("/status")
async def status():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
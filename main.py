import os
import sys
from fastapi import FastAPI
from pydantic import BaseModel
import torch
from sentence_transformers.cross_encoder import CrossEncoder

app = FastAPI()


### Pre-Load ###
# check device
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

# load checkpoint file
_CUR_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0,_CUR_PATH)
_CKPT_PATH = os.path.join(_CUR_PATH, "Team3_best_checkpoint/") 

# load model
num_labels = 1
model = CrossEncoder(_CKPT_PATH, num_labels=num_labels)

# input
class Data(BaseModel):
    sentence1: str
    sentence2: str

@app.post("/")
def classifier(request: Data):
    data1 = request.sentence1.strip() 
    data2 = request.sentence2.strip() 

    # tokenization
    model_input = [data1, data2]

    # inference 
    pred = model.predict(model_input) * 5 # restore to original scale

    pred = round(pred, 3)
    label = "유사한 문장입니다." if pred >= 3.0 else "유사하지 않은 문장입니다."

    return {"Sentence 1" : data1, "Sentence 2" : data2, "유사도(5점 만점)" : pred, "유사성 여부": label}
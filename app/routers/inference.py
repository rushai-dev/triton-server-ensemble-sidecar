from fastapi import APIRouter, Depends, Request

from services.inference import InferenceService
from schemas.product import ImageItem, TextItem
from config.product import get_product
from utils.request import multi_form_data_request, json_request

router = APIRouter(prefix="/inference", responses={404: {"description": "Not found"}},)

@router.post("/predict")
async def predict_endpoint(request: Request, product: get_product = Depends()):
    if request.headers["content-type"].startswith("multipart/form-data"):
        inputs = await multi_form_data_request(await request.form()).get()
        return InferenceService(product).predict(inputs)
    elif request.headers["content-type"] == "application/json":
        inputs = await json_request(await request.json()).get()
        return InferenceService(product).predict(inputs)
    else:
        return {"message": "Unsupported media type"}
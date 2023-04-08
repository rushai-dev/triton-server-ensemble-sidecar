from fastapi import APIRouter, Depends

from services.inference import InferenceService
from schemas.product import ImageItem, TextItem
from config.product import get_product
from utils.service_result import handle_result

router = APIRouter(prefix="/inference", responses={404: {"description": "Not found"}},)

@router.post("/predict")
async def predict_endpoint(image: ImageItem, text: TextItem, product: get_product = Depends()):
    result = InferenceService(product).predict(image if get_product()=="image" else text)
    return handle_result(result)
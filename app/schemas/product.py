from fastapi import File, UploadFile
from pydantic import BaseModel
from typing import Optional, List

class ImageItem(BaseModel):
    inputs: Optional[UploadFile] = File(None)

class TextItem(BaseModel):
    inputs: List[str]
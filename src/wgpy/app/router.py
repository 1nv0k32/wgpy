from fastapi import APIRouter

from wgpy.app.schemas import BodyModel
from wgpy.app.schemas import ResponseModel


router = APIRouter()


@router.post(
    path="/",
    response_model=ResponseModel,
)
def get_root(body: BodyModel) -> ResponseModel:
    """POST root."""
    return ResponseModel(arg1=body.arg1)

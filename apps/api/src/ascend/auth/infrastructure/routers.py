from fastapi import APIRouter, Depends, status
from .api.user_api_model import UserCreate
from ..domain.user import User
from ..application.services import UserService

router = APIRouter()


@router.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    response_model=User,
)
def create_user(
    user_create: UserCreate, user_service: UserService = Depends(UserService)
):
    return user_service.create_user(user_create)

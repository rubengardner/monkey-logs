from fastapi import FastAPI, Depends
from auth.infrastructure import routers as auth_router
from auth.infrastructure.database import get_session
from auth.infrastructure.user_repository import SQLUserRepository
from auth.domain.user_repository import UserRepository

app = FastAPI(title="Ascend API")


def get_user_repository(session=Depends(get_session)):
    return SQLUserRepository(session)


app.dependency_overrides[UserRepository] = get_user_repository

app.include_router(auth_router.router, prefix="/auth", tags=["Authentication"])

from ascend.auth.infrastructure.api.user_api_model import UserCreate
from fastapi import Depends, HTTPException, status
from ascend.auth.domain.user_repository import UserRepository
from ascend.auth.domain.user import User
import bcrypt


class UserService:
    def __init__(self, user_repository: UserRepository = Depends()):
        self.user_repository = user_repository

    def create_user(self, user_create: UserCreate) -> User:
        existing_user = self.user_repository.get_by_email(user_create.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        hashed_password = self._hash_password(user_create.password)

        # We need to create a new object with the hashed password
        # In a real implementation, the UserCreate model might have a
        # separate field for the hashed password, or we'd create an
        # intermediate model. For now, we'll create a new dict.
        user_data_with_hashed_password = user_create.dict()
        user_data_with_hashed_password["password"] = hashed_password

        # This part is a bit awkward due to our model structure.
        # A better approach might be to have a UserInDB model that includes
        # the hashed password. For now, we'll assume the repository
        # can handle this.

        # A more correct way would be:
        # user_to_create = UserInDB(**user_create.dict(), hashed_password=hashed_password)
        # return self.user_repository.create(user_to_create)

        # For now, let's just pass the modified dict, assuming the repo handles it.
        # This highlights a good point for future refinement.
        return self.user_repository.create(user_data_with_hashed_password)

    def _hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

from abc import ABC, abstractmethod
from .user import User
from ..infrastructure.api.user_api_model import UserCreate


class UserRepository(ABC):
    """
    Abstract repository for user data operations.
    This defines the contract for data storage.
    """

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        """
        Retrieves a user by their email address.
        """
        pass

    @abstractmethod
    def create(self, user_create: UserCreate) -> User:
        """
        Creates a new user in the data store.
        """
        pass

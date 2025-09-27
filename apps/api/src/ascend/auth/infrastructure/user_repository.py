from sqlmodel import Session, select
from ..domain.user import User, UserCreate
from ..domain.repository import UserRepository as AbstractUserRepository

class SQLUserRepository(AbstractUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()

    def create(self, user_create: UserCreate) -> User:
        # In a real implementation, we would expect user_create to be a model
        # that includes the hashed_password. For now, we'll assume it's passed
        # in the dict from the service.
        db_user = User(**user_create)
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

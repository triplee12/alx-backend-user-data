#!/usr/bin/env python3
"""DB module."""

from sqlalchemy import create_engine
# from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound, InvalidRequestError
from user import Base, User

VALID_FIELDS = [
    'id', 'email', 'hashed_password',
    'session_id', 'reset_token'
]


class DB:
    """DB class."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user to the database."""
        if not email or not hashed_password:
            return
        user = User(email=email, hashed_password=hashed_password)
        sess = self._session
        sess.add(user)
        sess.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find user by email."""
        if not kwargs or any(x not in VALID_FIELDS for x in kwargs):
            raise InvalidRequestError
        sess = self._session
        try:
            query = sess.query(User).filter_by(**kwargs)
            user = query.one()
            return user
        except NoResultFound as no_result:
            raise no_result

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user."""
        sess = self._session
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            if k not in VALID_FIELDS:
                raise ValueError
            setattr(user, k, v)
        sess.commit()

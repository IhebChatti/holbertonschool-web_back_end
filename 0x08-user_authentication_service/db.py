#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.session import Session

from user import User
from user import Base

PERMITTED_FIELDS = ['id', 'email', 'hashed_password',
                    'session_id', 'reset_token']


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """[add_user]
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """find_user_by
        """

        if not kwargs:
            raise InvalidRequestError
        if not all(field in PERMITTED_FIELDS for field in kwargs):
            raise InvalidRequestError
        result = self._session.query(User).filter_by(**kwargs).one()
        if not result:
            raise NoResultFound
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """[update_user]
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in PERMITTED_FIELDS:
                raise ValueError
            setattr(user, key, value)
        self._session.commit()

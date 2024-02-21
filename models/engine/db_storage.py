#!/usr/bin/python3
"""
Contains the class DBStorage
"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """Interacts with the MySQL database.

    Attributes:
        __engine: The database engine.
        __session: The database session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object."""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session.

        Args:
            cls: The class to filter the query by (optional).

        Returns:
            A dictionary of objects queried from the database.
        """
        new_dictionary = {}
        for class_name in classes:
            if cls is None or cls is classes[class_name] or cls is class_name:
                objects = self.__session.query(classes[class_name]).all()
                for obj in objects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dictionary[key] = obj
        return new_dictionary

    def new(self, obj):
        """Add the object to the current database session.

        Args:
            obj: The object to be added.
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None.

        Args:
            obj: The object to be deleted (optional).
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload data from the database."""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session

    def close(self):
        """ close method """
        if self.__session:
            self.__session.close()

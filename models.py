from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class User(Base):
    '''Create model for User and relationship to Sport'''
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Categories(Base):
    '''Create model for season and relationship to Sport'''
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    season = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    sports = relationship('Sports')

    @property
    def serialize(self):
        '''Returns data to be JSONified for apis'''
        return {
            'season': self.season,
            'id': self.id
        }


class Sports(Base):
    '''Create model for xGames sport'''
    __tablename__ = 'sport'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(1000))
    description_link = Column(String(500))
    image_link = Column(String(1000))
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Categories')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        '''Returns data to be JSONified for apis'''
        return {
            'name': self.name,
            'description': self.description,
            'description_link': self.description_link,
            'image_link': self.image_link,
            'id': self.id
        }


ENGINE = create_engine(
    'postgres://soxntrmvqyoaqj:471c8019a5142459bbeeccc5306f62987ff0ff3504092548587e0ece60183767@ec2-107-22-235-167.compute-1.amazonaws.com:5432/d9ejg9i508q546')
# ENGINE = create_engine('sqlite:///catalogue.db')

Base.metadata.create_all(ENGINE)

print("added models!")

from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    product_review = Column(Text, nullable=False)
    sentiment = Column(String(10), nullable=False)
    key_points = Column(Text, nullable=False)
    analysis_date = Column(DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'product_review': self.product_review,
            'sentiment': self.sentiment,
            'key_points': self.key_points,
            'analysis_date': self.analysis_date.isoformat(),
        }

def get_engine(settings):
    db_url = settings.get('db.url', 'sqlite:///:memory:') 
    return create_engine(db_url)

def get_session_factory(engine):
    factory = sessionmaker(bind=engine)
    return factory

def initialize_db(engine):
    Base.metadata.create_all(engine)
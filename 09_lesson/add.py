from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://postgres:1234@localhost:5433/QA")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class SpeciesType(Base):

    __tablename__ = "species_type"

    type_id = Column(Integer, primary_key=True)
    type_name = Column(String(100), nullable=False)

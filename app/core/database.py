from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Create the database engine
engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URL))

# Create a configured SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models - using the new import location
Base = declarative_base()
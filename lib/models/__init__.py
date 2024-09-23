from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create the Base class
Base = declarative_base()

# Import all models
from .client import Client
from .policy import Policy
from .reminder import Reminder

# Create engine and session
engine = create_engine('sqlite:///insurance_tracker.db')
Session = sessionmaker(bind=engine)

# This will create all tables
Base.metadata.create_all(engine)
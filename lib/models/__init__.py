from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# database engine
engine = create_engine('sqlite:///insurance_tracker.db')

# sessionmaker bound to this engine
Session = sessionmaker(bind=engine)

# base class for declarative class definitions
Base = declarative_base()

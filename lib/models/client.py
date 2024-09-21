from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Client(Base):
    __tablename__ = 'clients'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String)
    address = Column(String)
    
    # Establish a one-to-many relationship with Policy
    policies = relationship("Policy", back_populates="client")

    def __repr__(self):
        return f"<Client(id={self.id}, name='{self.name}', email='{self.email}')>"
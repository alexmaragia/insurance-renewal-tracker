from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Policy(Base):
    __tablename__ = 'policies'
    
    id = Column(Integer, primary_key=True)
    policy_number = Column(String, unique=True, nullable=False)
    type = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    premium_amount = Column(Float, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    insurance_company = Column(String)  # New field
    
    client = relationship("Client", back_populates="policies")
    reminders = relationship("Reminder", back_populates="policy")

    def __repr__(self):
        return f"<Policy(id={self.id}, policy_number='{self.policy_number}', type='{self.type}', insurance_company='{self.insurance_company}')>"
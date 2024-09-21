from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Reminder(Base):
    __tablename__ = 'reminders'
    
    id = Column(Integer, primary_key=True)
    policy_id = Column(Integer, ForeignKey('policies.id'), nullable=False)
    reminder_date = Column(Date, nullable=False)
    status = Column(String, default='pending')
    
    # Establish a many-to-one relationship with Policy
    policy = relationship("Policy", back_populates="reminders")

    def __repr__(self):
        return f"<Reminder(id={self.id}, policy_id={self.policy_id}, reminder_date='{self.reminder_date}', status='{self.status}')>"
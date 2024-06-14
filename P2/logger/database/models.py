from sqlalchemy import Column, Integer, String
from database.database import db

class Log(db.Model):
  __tablename__ = 'logs'

  id       = Column(Integer, primary_key=True, autoincrement=True)
  action   = Column(String(50), nullable=False)
  datetime = Column(String(50), nullable=False)

  
  def serialize(self):
    return {
      "id": self.id,
      "action": self.action,
      "datetime": self.datetime
    }
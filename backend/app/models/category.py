from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from ..database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    products = relationship("Product", back_populates="category")
    created_at = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return f"<Category {self.name}>"

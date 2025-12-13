from sqlalchemy import Column, Integer, String, DataTime
from sqlalchemy.orm import relationship
from datatime import datatime

from .base import Base
from .category import Category

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, que=True, nullable=False, index=True)
    slug = Column(String, unique=True, nullable=False, index=True)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    image_url = Column(String)
    category_id = Column(Integer, nullable=False)
    created_at = Column(DataTime, default=datatime.now())
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price} )"
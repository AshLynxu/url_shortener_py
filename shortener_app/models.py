# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 22:19:57 2023

@author: danie
"""

from sqlalchemy import Boolean, Column, Integer, String

from .database import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    secret_key = Column(String, unique=True, index=True)
    target_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)
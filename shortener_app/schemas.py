# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 22:06:36 2023

@author: danie
"""

from pydantic import BaseModel

class URLBase(BaseModel):
    target_url: str

class URL(URLBase):
    is_active: bool
    clicks: int

    class Config:
        orm_mode = True

class URLInfo(URL):
    url: str
    admin_url: str
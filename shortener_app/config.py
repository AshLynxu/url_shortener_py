# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 19:38:30 2023

@author: danie
"""
from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"
    
    class Config:
        env_file = ".env"
    
@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings

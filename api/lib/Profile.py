from dataclasses import dataclass, field
from .User import User
from typing import List

"""
Model represents profiles table containing profiles assigned to each user
Every profile must contain user_id and user
rest of args are None by default until changed in profile settings by user
"""


@dataclass
class Profile:
    user_id: int  # foreign key referring to users table
    user: User
    picture: str = None
    name: str = None
    age: str = None
    gender: str = None
    bio: str = None

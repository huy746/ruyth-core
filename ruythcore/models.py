from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class User:
    id: str
    username: str
    discriminator: str = "0000"
    bot: bool = False

@dataclass
class Message:
    id: str
    channel_id: str
    content: str
    author: User
    raw: Dict[str, Any] = None

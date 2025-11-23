"""
RuythCore - Library Discord Bot
"""
__version__ = "1.0.5"
__author__ = "ruythbot_huy"

from .client import Client
from .commands import CommandManager
from .slash import SlashCommandManager
from .voice import VoiceClient
from .http import HTTPClient
from .gateway import Gateway
from .events import EventHandler
from .context import Context
from .models import Message, User
from .constants import *
from . import utils

# aliases
Command = CommandManager
SlashCommand = SlashCommandManager

__all__ = [
    "Client","Command","SlashCommand","VoiceClient","HTTPClient","Gateway",
    "EventHandler","Context","Message","User","utils"
]

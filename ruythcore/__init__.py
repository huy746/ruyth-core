"""
ruythcore - A simple Discord bot library
"""

__version__ = "1.0.2"
__author__ = "ruythbot_huy"

# Import core classes
from .client import Client
from .commands import CommandManager
from .slash import SlashCommandManager
from .voice import VoiceClient
from .http import HTTPClient
from .gateway import Gateway
from .events import EventHandler
from .context import Context
from .constants import *
from . import utils  # Import utils.py

# Define what is exported when doing `from ruythcore import *`
__all__ = [
    "Client",
    "CommandManager",
    "SlashCommandManager",
    "VoiceClient",
    "HTTPClient",
    "Gateway",
    "EventHandler",
    "Context",
    "utils",
    "GATEWAY_URL",
    "HTTP_BASE",
    "USER_AGENT",
    "INTENTS_ALL",
    "OP_DISPATCH",
    "OP_HEARTBEAT",
    "OP_IDENTIFY",
    "OP_STATUS_UPDATE",
    "OP_VOICE_STATE_UPDATE",
    "OP_VOICE_SERVER_PING",
    "OP_RESUME",
    "OP_RECONNECT",
    "OP_REQUEST_GUILD_MEMBERS",
    "OP_INVALID_SESSION",
    "OP_HELLO",
    "OP_HEARTBEAT_ACK"
]

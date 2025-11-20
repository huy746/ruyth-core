from .client import Client, RuythCore
from .context import Context
from .slash import SlashManager
from .command import PrefixCommandManager
from .http import HTTPClient
from .voice import VoiceManager
from .constants import DEFAULT_INTENTS

__all__ = [
    "Client",
    "RuythCore",
    "Context",
    "SlashManager",
    "PrefixCommandManager",
    "HTTPClient",
    "VoiceManager",
    "DEFAULT_INTENTS",
]

# GẮN TRỰC TIẾP VÀO MODULE — FIX CHO import ruythcore; ruythcore.Client
# => người dùng có thể: import ruythcore; bot = ruythcore.Client(...)
Client = Client
RuythCore = RuythCore

__version__ = "1.0.0"
__author__ = "ruythbot_huy"

import datetime

def snowflake_to_timestamp(snowflake: int) -> datetime.datetime:
    discord_epoch = 1420070400000
    timestamp = ((int(snowflake) >> 22) + discord_epoch) / 1000
    return datetime.datetime.fromtimestamp(timestamp)

def mention_user(user_id: str) -> str:
    return f"<@{user_id}>"

def mention_role(role_id: str) -> str:
    return f"<@&{role_id}>"

def mention_channel(channel_id: str) -> str:
    return f"<#{channel_id}>"

def is_valid_snowflake(snowflake: str) -> bool:
    return str(snowflake).isdigit() and len(str(snowflake)) >= 17
                 

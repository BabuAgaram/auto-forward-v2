import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5429387409:AAEGaLLysVB5sY8XYANWt-n5qfcyb0EVpA4")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "21818317"))
    API_HASH = os.environ.get("API_HASH", "bc6ab154300cc41fe127ca4d658dc75d")
    AUTH_USERS = os.environ.get("OWNER", "5650200786")


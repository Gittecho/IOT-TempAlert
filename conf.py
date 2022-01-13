"""Configurations for telegram_IOT.py"""


class confy:
    # Telegram credentials
    # This is the channel ID of the created Telegram channel. Paste after @
    # This is the bot ID of the created Telegram Bot. Paste after bot
    # Threshold beyond which the alert should be sent

    telegram_bot_id = ""
    telegram_chat_id = ""
    threshold = 100

    # Device credentials
    # This is your Bolt Cloud API Key
    # This is the device ID and will be similar to BOLTXXXX where XXXX is some numbers

    bolt_api_key = ''
    device_id = ''

    # Mail credentials
    MAILGUN_API_KEY = ''
    SANDBOX_URL = ''
    SENDER_EMAIL = ''
    RECIPIENT_EMAIL = ''

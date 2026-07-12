import os

COLLECTIONS = {
    "FFTL": "https://guitarsgarden.com/collections/fftl",
    "FFST": "https://guitarsgarden.com/collections/ffst",
    "FFSP": "https://guitarsgarden.com/collections/ffsp",
    "FFVX": "https://guitarsgarden.com/collections/ffvx",
}

STATE_FILE = "known_products.json"

TIMEZONE = "America/Denver"
ACTIVE_START_HOUR = 19
ACTIVE_END_HOUR = 7

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")

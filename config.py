import  os

SESSION = os.environ.get("SESSION", "YouTube-DL-Bot")
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
WORKERS = int(os.environ.get("WORKERS", 100))
PLUGINS = dict(os.environ.get("PLUGINS", {'root': 'plugins'}))
SLEEP_THRESHOLD = int(os.environ.get("SLEEP_THRESHOLD", 5))
DOWNLOAD_LOCATION = "./Downloads"
YOUTUBE_NEXT_FETCH = 0
EDIT_TIME = 5

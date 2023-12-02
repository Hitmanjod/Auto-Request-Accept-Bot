from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "9344337"))
    API_HASH = getenv("API_HASH", "7e55bf98380e416d5de1c4c567395a32")
    BOT_TOKEN = getenv("BOT_TOKEN", "6517618497:AAHZjQz0dRmEkgyY5I7j5q7vFW5SaFAXI2s")
    FSUB = getenv("FSUB", "iMediaUniverse")
    CHID = int(getenv("CHID", "-1001862216322"))
    SUDO = list(map(int, getenv("SUDO", "6040965491").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sujanch9993:sujanch9993@cluster0.yhmdrl9.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

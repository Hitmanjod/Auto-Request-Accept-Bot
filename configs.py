from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25502576"))
    API_HASH = getenv("API_HASH", "f0f35dbb5b0081cdc8d3c9d5383c4628")
    BOT_TOKEN = getenv("BOT_TOKEN", "6134077876:AAHeX0SvR7PMgamOMyaQGnBDQAmqpDYOp-k")
    FSUB = getenv("FSUB", "Sujan_BotZ")
    CHID = int(getenv("CHID", "-1001861445521"))
    SUDO = list(map(int, getenv("SUDO", "5123039648").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://sujanch9993:sujanch9993@cluster0.yhmdrl9.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

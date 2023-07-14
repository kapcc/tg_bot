from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
bot = Bot(token = "6365534625:AAEReibWc95M10UqStVROG-GwSzHuSWHLQQ")
dp = Dispatcher(bot, storage=storage)


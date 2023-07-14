from aiogram.utils import executor
from create_bot import dp





async def on_startup(_):
    print("Bot is UP")




from handlers import client






executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


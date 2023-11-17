import handlers
from loader import dp,bot
from utils.notify import shut_up, start_up
from utils.set_botcommands import commands
import asyncio
async def main():
      dp.startup.register(start_up)
      dp.shutdown.register(shut_up)
      await bot.set_my_commands(commands=commands)
      try:
            await dp.start_polling(bot)
      finally:
            await bot.session().close()








if __name__=='__main__':
      asyncio.run(main())


import asyncio
import datetime
from aiogram import Bot, Dispatcher
import schedule
import time
from datetime import timezone, timedelta


# 🔑 Токен твоего бота (полученный от @BotFather)
TOKEN = "8324144752:AAECID28uaChX7SWnlCTGwIHPOw2K_T--EQ"

# 🆔 ID твоей группы (например: -1001234567890)
GROUP_ID = -1002774414012

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Устанавливаем часовой пояс UTC+5 (Ташкент)
TASHKENT_TZ = timezone(timedelta(hours=5))

# 📊 Функция отправки опроса
async def send_poll():
    now = datetime.datetime.now(TASHKENT_TZ)
    weekday = now.weekday()  # 0=Пн, 6=Вс
    if weekday < 5:  # только Пн–Пт
        await bot.send_poll(
            chat_id=GROUP_ID,
            question="Эртанги вожденияга ким, нечида келади ?",   # твой вопрос
            options=["08:00-09:00", "09:00-10:00", "10:00-11:00", "11:00-12:00","12:00-13:00", "14:00-15:00", "15:00-16:00", "16:00-17:00", "17:00-18:00", "Бормайман"],  # варианты
            is_anonymous=False,                 # видно, кто ответил
            type="regular" # обычный опрос
        )
        print("Опрос отправлен в группу ✅")
    else:
        print("Сегодня выходной — опрос не отправлен.")

# Планировщик с учётом времени UTC+5
def scheduler():
    schedule.every().day.at("20:00").do(lambda: asyncio.run(send_poll()))
    while True:
        schedule.run_pending()
        time.sleep(30)


# Запуск
if __name__ == "__main__":
    print("Бот запущен и ждёт 20:00 по Ташкенту (+5)...")

    scheduler()



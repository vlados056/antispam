import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Вставьте сюда свой токен
API_TOKEN = '7762847259:AAGiWfRx3LTWKpa-dr2KCTOR4GTFb16hyWo'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Список слов, которые считаются спамом
SPAM_WORDS = ['детальнее в лc','детальнее в лс','детальнее','еженедельная прибыль','лc','прибыль','требуется','занятость','сотрудник','сотрудничество','сотрудник','команду','набираем','заработка','требуются', 'напишите в лс', 'удаленно', 'прeдлoжениe o сoтрyдничeствe', 'прoeктe', 'прoeкт', 'личныe соoбщeния', 'вoзможнoсть сoвмещать', 'пишитe в личныe соoбщeния', 'сотрудничество', 'сотрудничество онлайн', 'доход', 'сотруднuчество онлайн', 'сотруднuчество', 'по всем вопросам', 'достаточно телефона']

# Функция для обработки новых сообщений
@dp.message()
async def handle_message(message: types.Message):
    text = message.text.lower()
    logging.info(f"Received message: {text}")
    for word in SPAM_WORDS:
        if word in text:
            logging.info(f"Deleting message containing spam word: {word}")
            await message.delete()
            break

async def main():
    # Запуск поллинга
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

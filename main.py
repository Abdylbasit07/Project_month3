from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config
import logging

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)



@dp.message_handler(commands=["mem"])
async def mem(message: types.message):
    photo = open("media/mmeeemmms.webp", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


@dp.message_handler(commands=["quiz"])
async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    call_button_1 = InlineKeyboardButton("NEXT", callback_data="call_button_1")
    markup.add(call_button_1)

    ques = "Year of release of the programming language 'Python'?"
    answer = [
        '1985',
        '1990',
        '1981',
        '1991',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=ques,
        options=answer,
        correct_option_id=3,
        type="quiz",
        is_anonymous=False,
        explanation="Do you write in Python and don't know the year of release?",
        reply_markup=markup
    )

@dp.callback_query_handler(text="call_button_1")
async def quiz2(call: types.CallbackQuery):
    ques = "By whom invented Python?"
    answer = [
        'Bjorn Stroustrup',
        'Guido Van Rossum',
        'Scott Wiltamut and Anders Heilsberg',
        'James Gosling',
        'Mitchell Reznik',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        correct_option_id=1,
        type="quiz",
        is_anonymous=False,
        explanation="Do you write in Python and don't know the founder of the language?",
    )


@dp.message_handler()
async def echo_stepen(message: types.Message):
    try:
        line = message.text
        a = int(line)
        res = a**2
        await bot.send_message(message.from_user.id, str(res))
    except:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    logging.basicConfig(level=logging.INFO)
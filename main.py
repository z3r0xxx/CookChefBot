import asyncio

from settings import TOKEN
from keyboards import *
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, CallbackQuery, InputMediaPhoto

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    """ Обработчик команды /start """

    # Отправляем баннер и текст с клавиатурой
    await message.answer_photo(
        photo=FSInputFile("images/banner_1.jpg"),
        caption=(
            "🔥 Привет, на связи бот <b>CookChef</b>!\n\n"
            "Чтобы вкусно покушать, не обязательно заказывать еду из ресторана - можно приготовить самому!\n\n"
            "Ниже ты увидишь несколько кнопок. \n"
            "Выбери, что ты хочешь: получить случайный рецепт, подобрать еду по имеющимся продуктам или попробовать рецепт, <b>созданный искуственным интеллектом!</b>"
        ),
        reply_markup=inline_kb_full,
        parse_mode="HTML"
    )


@dp.callback_query(MyCallback.filter())
async def buttons_callback(call: CallbackQuery, callback_data: MyCallback):
    """ Обработчик нажатий на кнопки """

    # Кнопка "Хочу случайный рецепт"
    if callback_data.test == "1":
        await call.message.edit_media(
            media=InputMediaPhoto(media=FSInputFile("images/image_1.jpg"))
        )

        await call.message.edit_caption(
            caption="123",
            parse_mode="HTML",
            reply_markup=inline_kb_random_recipe
        )
    
    if callback_data.test == "0":
        await call.message.edit_media(
            media=InputMediaPhoto(media=FSInputFile("images/banner_1.jpg"))
        )

        await call.message.edit_caption(
            caption=(
                "🔥 Привет, на связи бот <b>CookChef</b>!\n\n"
                "Чтобы вкусно покушать, не обязательно заказывать еду из ресторана - можно приготовить самому!\n\n"
                "Ниже ты увидишь несколько кнопок. \n"
                "Выбери, что ты хочешь: получить случайный рецепт, подобрать еду по имеющимся продуктам или попробовать рецепт, <b>созданный искуственным интеллектом!</b>"
            ),
            parse_mode="HTML",
            reply_markup=inline_kb_full
        )


@dp.message()
async def on_message(message: Message):
    pass


async def main():
    """ Главная функция программы """

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

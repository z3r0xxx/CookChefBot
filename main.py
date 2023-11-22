import asyncio

from logs import logger
from settings import TOKEN
from database import *
from keyboards import *

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, CallbackQuery, InputMediaPhoto

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    """ Обработчик команды /start """

    # Создание пользователя в БД
    create_user(user_id=message.from_user.id)

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
    """ Обработчик нажатия на кнопки """

    # Кнопка "Вернуться в главное меню"
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

    # Кнопка "Хочу случайный рецепт"
    if callback_data.test == "1":
        random_recipe = get_random_recipe()

        await call.message.edit_media(
            media=InputMediaPhoto(media=FSInputFile(random_recipe.image_path))
        )

        await call.message.edit_caption(
            caption=random_recipe.text,
            parse_mode="HTML",
            reply_markup=inline_kb_random_recipe
        )


@dp.message()
async def on_message(message: Message):
    """ Обработчик входящих сообщений """

    # Создание пользователя в БД
    create_user(user_id=message.from_user.id)


async def main():
    """ Главная функция программы """

    print('\n       TELEGRAM BOT by zrx\n')
    logger.info(f'Бот успешно загружен.')

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

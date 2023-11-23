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


async def send_message_with_recipe(call: CallbackQuery, recipe):
    inline_btn_4.callback_data = MyCallback(test=f"add_rate_{recipe.id}").pack()
    inline_btn_4.text = f"Круто! ({recipe.rate})"

    text = (
        f"<b>Как готовить?</b>\n"
        f"{str(recipe.text)}\n\n"
        f"<b>Какие продукты нужны?</b>\n"
        f"{str(recipe.products)}\n\n"
        f"<b>На 100 граммов</b>\n"
        f"Ккал: {recipe.calories}\n"
        f"Белки: {recipe.proteins}\n"
        f"Жиры: {recipe.fats}\n"
        f"Углеводы: {recipe.carbohydrates}\n"
    )

    await call.message.delete()
    await bot.send_photo(
        call.message.chat.id, 
        photo=FSInputFile(recipe.image_path),
        caption=text,
        parse_mode="HTML",
        reply_markup=inline_kb_random_recipe
    )


async def send_message_with_products(call: CallbackQuery):
    await call.message.delete()
    await bot.send_photo(
        call.message.chat.id, 
        photo=FSInputFile("images/banner_2.jpg"),
        caption="Внизу есть кнопочки. Нажми на кнопкочи с нужными продуктами, а после того как закончишь - жми на кнопку \"Готово\"",
        parse_mode="HTML",
        reply_markup=inline_kb_items
    )


@dp.callback_query(MyCallback.filter())
async def buttons_callback(call: CallbackQuery, callback_data: MyCallback):
    """ Обработчик нажатия на кнопки """

    # Кнопка "Вернуться в главное меню"
    if callback_data.test == "0":
        await call.message.delete()
        await bot.send_photo(
            call.message.chat.id, 
            photo=FSInputFile("images/banner_1.jpg"),
            caption=(
                "🔥 Привет, на связи бот <b>CookChef</b>!\n\n"
                "Чтобы вкусно покушать, не обязательно заказывать еду из ресторана - можно приготовить самому!\n\n"
                "Ниже ты увидишь несколько кнопок. \n"
                "Выбери, что ты хочешь: получить случайный рецепт или подобрать еду по имеющимся продуктам!"
            ),
            parse_mode="HTML",
            reply_markup=inline_kb_full
        )

    # Кнопка "Хочу случайный рецепт"
    if callback_data.test == "1":
        recipe = get_random_recipe()
        await send_message_with_recipe(call, recipe)
    
    # Кнопка "Покажите другой"
    if callback_data.test == "5":
        recipe = get_random_recipe()
        await send_message_with_recipe(call, recipe)
    
    # Кнопка "Круто!"
    if callback_data.test.startswith("add_rate_"):
        recipe_id = int(callback_data.test.replace("add_rate_", ""))
        add_rate_to_recipe(recipe_id=recipe_id)

        recipe = get_recipe_(recipe_id=recipe_id)
        await send_message_with_recipe(call, recipe)
    
    # Кнопка "Хочу рецепт по продуктам"
    if callback_data.test == "2":
        await send_message_with_products(call)



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

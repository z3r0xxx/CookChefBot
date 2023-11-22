
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from aiogram.filters.callback_data import CallbackData


# Кастомный класс для обработки кнопок
class MyCallback(CallbackData, prefix="kbd"):
    test: str

# Кнопка "В главное меню"
inline_btn_0 = InlineKeyboardButton(text="В главное меню", callback_data=MyCallback(test="0").pack())

# Клавиатура 1
inline_btn_1 = InlineKeyboardButton(text="Хочу случайный рецепт", callback_data=MyCallback(test="1").pack())
inline_btn_2 = InlineKeyboardButton(text="Хочу рецепт по продуктам", callback_data=MyCallback(test="2").pack())
inline_btn_3 = InlineKeyboardButton(text="🔥 Хочу рецепт от ИИ", callback_data=MyCallback(test="3").pack())

inline_kb_full = InlineKeyboardMarkup(
    inline_keyboard=[
        [inline_btn_1],
        [inline_btn_2],
        [inline_btn_3]
    ]
)

# Клавиатура 2
inline_btn_4 = InlineKeyboardButton(text="Круто! (23)", callback_data=MyCallback(test="4").pack())
inline_btn_5 = InlineKeyboardButton(text="Покажите другой", callback_data=MyCallback(test="5").pack())

inline_kb_random_recipe = InlineKeyboardMarkup(
    inline_keyboard=[
        [inline_btn_4],
        [inline_btn_5],
        [inline_btn_0]
    ]
)

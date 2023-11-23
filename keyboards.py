
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
inline_btn_1 = InlineKeyboardButton(text="🔥Хочу случайный рецепт", callback_data=MyCallback(test="1").pack())
inline_btn_2 = InlineKeyboardButton(text="Хочу рецепт по продуктам", callback_data=MyCallback(test="2").pack())
inline_btn_3 = InlineKeyboardButton(text="🔥 Хочу рецепт от ИИ", callback_data=MyCallback(test="3").pack())

inline_kb_full = InlineKeyboardMarkup(
    inline_keyboard=[
        [inline_btn_1],
        [inline_btn_2]
    ]
)

# Клавиатура 2
inline_btn_4 = InlineKeyboardButton(text="Круто!", callback_data=MyCallback(test="add_rate_").pack())
inline_btn_5 = InlineKeyboardButton(text="Покажите другой", callback_data=MyCallback(test="5").pack())

inline_kb_random_recipe = InlineKeyboardMarkup(
    inline_keyboard=[
        [inline_btn_4],
        [inline_btn_5],
        [inline_btn_0]
    ]
)

# Клавиатура 3
inline_btn_6 = InlineKeyboardButton(text="🐔", callback_data=MyCallback(test="add_item_1").pack())
inline_btn_7 = InlineKeyboardButton(text="🥚", callback_data=MyCallback(test="add_item_2").pack())
inline_btn_8 = InlineKeyboardButton(text="🐟", callback_data=MyCallback(test="add_item_3").pack())
inline_btn_9 = InlineKeyboardButton(text="🍯", callback_data=MyCallback(test="add_item_4").pack())
inline_btn_10 = InlineKeyboardButton(text="🥛", callback_data=MyCallback(test="add_item_5").pack())
inline_btn_11 = InlineKeyboardButton(text="🥜", callback_data=MyCallback(test="add_item_6").pack())
inline_btn_12 = InlineKeyboardButton(text="🍖", callback_data=MyCallback(test="add_item_7").pack())
inline_btn_14 = InlineKeyboardButton(text="🧄", callback_data=MyCallback(test="add_item_9").pack())
inline_btn_15 = InlineKeyboardButton(text="🧅", callback_data=MyCallback(test="add_item_10").pack())
inline_btn_16 = InlineKeyboardButton(text="🐽", callback_data=MyCallback(test="add_item_11").pack())
inline_btn_17 = InlineKeyboardButton(text="🍄", callback_data=MyCallback(test="add_item_12").pack())
inline_btn_19 = InlineKeyboardButton(text="🍫", callback_data=MyCallback(test="add_item_14").pack())
inline_btn_20 = InlineKeyboardButton(text="🌶️", callback_data=MyCallback(test="add_item_15").pack())
inline_btn_21 = InlineKeyboardButton(text="🍅", callback_data=MyCallback(test="add_item_16").pack())
inline_btn_22 = InlineKeyboardButton(text="🥒", callback_data=MyCallback(test="add_item_17").pack())
inline_btn_23 = InlineKeyboardButton(text="Готово, показывайте!", callback_data=MyCallback(test="6").pack())

inline_kb_items = InlineKeyboardMarkup(
    inline_keyboard=[
        [inline_btn_6, inline_btn_8, inline_btn_12, inline_btn_16],
        [inline_btn_7, inline_btn_10, inline_btn_9, inline_btn_11],
        [inline_btn_14, inline_btn_15, inline_btn_21, inline_btn_22],
        [inline_btn_20, inline_btn_19, inline_btn_17],
        [inline_btn_23],
        [inline_btn_0]
    ]
)

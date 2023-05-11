


web_app = WebAppInfo(url="https://mirl1x.github.io/test15/")

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Size", web_app=web_app)]
    ],
    resize_keyboard=True
)

cb= CallbackData('btn', 'action')
key = InLineKeyboardMarkup(

inline_keyboard=[[InlineKeyboardButton('Pay', callback_data='btn:buy')]]
)

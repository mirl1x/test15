from config import PAYMENTS_TOKEN

from keyboard import keyboard

@dp.message_handler(Command('start'))
async def start(message: Message):
    await bot.send_message(message.chat.id,
                           'Hey',
                           reply_markup=keyboard)
    
    PRICE = {
        '1': [LabeledPrice(label='item1', amount=1000000)]
}


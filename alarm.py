from telethon import TelegramClient, events  # Імпортуємо потрібні бібліотеки
import aiogram
from aiogram import Bot, Dispatcher, types, executor
from datetime import datetime

# підключаємо бота
bot = Bot(token='6215212505:AAFjRsEP7YbpKEC_OPQZFbRH3gD-dGe3UyA')
dp = Dispatcher(bot)
 
api_id = 27076955  # Вводимо id нашого телеграм клієнта, та записуємо номер щоб не загубити 
api_hash = 'e6a998a44112d921c71b7b6665807b25'  # Вводимо hash нашого телеграм клієнта

chat_bezbab = -727502806
chat_test = 5900123750

 
client = TelegramClient("Test", api_id, api_hash)  # Збираемо клієнта до купи
target_can = -1001844129402  # Вводимо id в який будемо пересилати повідомлення
key_words_onalarm = ["Повітряна тривога в Волинська область", "Повітряна тривога в Рівненська область"] # Вводимо ключові слова які будемо шукати в повідомленнях
key_wordss_offalarm = ["Відбій тривоги в Волинська область", "Відбій тривоги в Рівненська область"]
#key_words_onalarm = ["Повітряна тривога"]
#key_wordss_offalarm = ["Відбій тривоги"]
 
@client.on(events.NewMessage(
    chats=[-1001766138888, -1001802336341]))  # Запускаємо наш клієнт та скануемо на які саме канали реагувати
async def normal_handler(event):  # Обробляємо подію
    message = ''
    for i in range(len(key_words_onalarm or key_wordss_offalarm)):  # Перебираємо всі ключові слова з нашого списку
        if key_words_onalarm[i] in event.message.message:  # Перевіряємо кожне слово на наявність його в нашому повідомленні
            print(f"Data: {datetime.now().strftime('%d.%m.%Y %T')}\nID Group: {event.message.peer_id} | Text: {event.message.message}") # Роздруковуемо в консоль id чату/групи та текст знайденного повідомлення (не обов'язково)
            print('\n================================================================================\n')
            # await client.send_file(target_can, 'https://i.gifer.com/origin/4e/4e3431b51b9a7587feade70da83f2216.gif')
            # await client.send_message(target_can, event.message)   # Пересилаємо знайдене повідомлення
            await bot.send_animation(chat_id=chat_test, animation='https://i.gifer.com/origin/4e/4e3431b51b9a7587feade70da83f2216.gif')
            await bot.send_message(chat_id=chat_test, text=event.message.text)
            break
        if key_wordss_offalarm[i] in event.message.message:  # Перевіряємо кожне слово на наявність його в нашому повідомленні
            print(f"Data: {datetime.now().strftime('%d.%m.%Y %T')}\nID Group: {event.message.peer_id} | Text: {event.message.message}") # Роздруковуемо в консоль id чату/групи та текст знайденного повідомлення (не обов'язково)
            print('\n================================================================================\n')
            # await client.send_file(target_can, 'https://media.tenor.com/cKrq7zekafEAAAAC/відбійповітряноїтривоги-їжак.gif')
            # await client.send_message(target_can, event.message)
            await bot.send_animation(chat_id=chat_test, animation='https://media.tenor.com/cKrq7zekafEAAAAC/відбійповітряноїтривоги-їжак.gif')
            await bot.send_message(chat_id=chat_test, text=event.message.text)
            break
 
client.start()  # Запускаємо кліент
client.run_until_disconnected()  # Ставимо його в бескінечний цикл

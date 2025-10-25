import telebot
from bot_logic import gen_pass  # Импортируем функцию из bot_logic

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("8494480491:AAHx2J0o72LErIWh82ZsCkfTN_36Spy-yY4")
text_messages = {
    'welcome':
        u'Please welcome {name}!\n\n'
        u'This chat is intended for questions about and discussion of the pyTelegramBotAPI.\n'
        u'To enable group members to answer your questions fast and accurately, please make sure to study the '
        u'project\'s documentation (https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md) and the '
        u'examples (https://github.com/eternnoir/pyTelegramBotAPI/tree/master/examples) first.\n\n'
        u'I hope you enjoy your stay here!',

    'info':
        u'My name is TeleBot,\n'
        u'I am a bot that assists these wonderful bot-creating people of this bot library group chat.\n'
        u'Also, I am still under development. Please improve my functionality by making a pull request! '
        u'Suggestions are also welcome, just drop them in this group chat!',

    'wrong_chat':
        u'Hi there!\nThanks for trying me out. However, this bot can only be used in the pyTelegramAPI group chat.\n'
        u'Join us!\n\n'
        u'https://telegram.me/joinchat/067e22c60035523fda8f6025ee87e30b'
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye или /pass для генерации пароля!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")
# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
    
@bot.message_handler(commands=['help'])
def on_info(message):   
    bot.reply_to(message, text_messages['wrong_chat'])
    
@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open('images/mem.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)


@bot.message_handler(commands=['mem2'])
def send_mem2(message):
    with open('images/mem2.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['mem3'])
def send_mem3(message):
    with open('images/mem3.jpeg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['random_mem'])
def send_random_mem(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)     

@bot.message_handler(commands=['can_be_thrown_into_the_trash'])
def send_hello(message):   
    bot.reply_to(message, ['пищевые остатки, бумага, пластик, одежда, обувь'])

@bot.message_handler(commands=['it_is_possible_to_recycle_it'])
def send_hello(message):   
    bot.reply_to(message, ['бумагу, картон, газеты, стекло, бутылки, банки, металл, пластик, электронику, одежду,батарейки'])       
        
# Запускаем бота
bot.polling()

import telebot
import urllib3
import telepot


token = '1932028191:AAEXdOZlm-fGcTU8KRKm8OnND4qA4l9YPx4'

bot = telebot.TeleBot(token)

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('💳Реквизиты для оплаты','⭕Помощь','⚠Условия и правила')
    keyboard.add('🙋‍♂️Реферальная программа','/start')
    bot.send_message(message.chat.id, 'Привет, я бот который поможет вступить тебе в приватный канал',reply_markup=keyboard)

@bot.message_handler(content_types=['text'])

def requz(message):
    if message.text == '💳Реквизиты для оплаты':
        bot.send_message(message.chat.id, '💸Для входа в группу необходимо перевести денежные средства на реквизиты указанные ниже👇\n\n💳Реквизиты: 4149 3900 0022 6364\n\n'
                                          'После оплаты необходимо сделать скрниншот перевода или фото чека и отправить администратору @jordj0001k\n\n'
                                          '🤑Абонемент на 1 день - 200грн;\n'
                                          '🔥на 3 дня - 450 грн;\n'
                                          '🔥на неделю - 850 грн;\n'
                                          '🔥на месяц - 1500 грн ')
        bot.send_message(message.chat.id,'Как только администратор проверит Ваш платёж, он добавит Вас в приватную группу')
    elif message.text == '⭕Помощь':
        bot.send_message(message.chat.id,'⁉Если у Вас возникли какие-либо проблемы, напишите нашему администратору *@jordj0001k*')
    elif message.text == '⚠Условия и правила':
        bot.send_message(message.chat.id, '• За 30 минут до события будет даваться прогноз в приватную группу\n'
                                          '• Вероятность выиграша от нашего прогноза 94%\n'
                                          '• Если прогноз от наших аналитиков не сыграл (такое бывает редко), мы даём Вам БЕСПЛАТНЫЙ абонемент на 3 дня!\n'
                                          '• Рефералом считается тот человек, который купил один из абонементов!')
    elif message.text == '🙋‍♂️Реферальная программа':
        bot.send_message(message.chat.id,'🤑Приглашай друзей и получай скидку на абонемент!\n'
                                         '🟢При приглашении 1 до 4 человек, Вы получаете скидку 50% на однодневный или трёхдневный абонемент\n'
                                         '󠀥󠀥🟢При приглашении 5 и более людей, Вы получаете скидку 50% на ЛЮБОЙ абонемент!\n'
                                         '❗Приглашённый Вами человек должен написать администратору Ваш никнейм, чтобы Вы получили скидку!\n')


bot.polling(none_stop=True, interval=0)
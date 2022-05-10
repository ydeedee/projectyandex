import vk_api, random

from vk_api.longpoll import VkLongPoll, VkEventType


vk_session = vk_api.VkApi(token="798c432be29cf9c679335ba77f9ead09f54f591247bb6b1f4040b2d5a4ed29e9712f73e8a7d97d52f8693")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

global R


def send_some_msg(id, some_text):
    vk_session.method('messages.send', {"user_id": id, "message": some_text, "random_id": 0})


def random_id():
    R = 0
    R = random.randint(0, 100000000)
    return R


for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('Новое сообщение:')
            print('Для меня от:', event.user_id)
            print('Текст:', event.text)
            msg = event.text.lower()
            id = event.user_id

            if 'привет' in msg or 'здравствуйте' in msg:
                send_some_msg(id, 'Здравствуйте! Вы хотели заказать портрет?')
            elif msg == 'да':
                session_api.messages.send(
                    user_id=id,
                    message='Давайте я вас ознакомлю с ценами: '
                            '\n'
                            '1) Портрет в черно-белом стиле (до плеч) - 300 рублей, '
                            '\n'
                            '2) Портрет в цвете (до плеч) - 500 рублей'
                            '\n'
                            '3) Портрет в черно-белом стиле (по пояс) - 600 рублей'
                            '\n'
                            '4) Портрет в цвете (по пояс) - 800 рублей'
                            '\n'
                            'Если вас что-то заинтересовало, напишите цифру выбранного пункта',
                    keyboard=open('keyboard.js', 'r', encoding='utf-8').read(),
                    random_id=random_id()
                )
            elif msg == '1' or msg == '2' or msg == '3' or msg == '4':
                send_some_msg(id,
                              'Супер! Пришлите, пожалуйста, фото для портрета. Разрешение портрета будет такое же как '
                              'на фотографии.')
                print(msg)

            elif msg == '':
                send_some_msg(id, 'Ожидайте портрет в ближайшее время! Вам напишут, когда все будет готово!'
                                  '\n'
                                  'Оплата будет совершаться через Сбербанк Онлайн по номеру телефона'
                                  '\n'
                                  'Если возникли вопросы, на которые наш бот не смог ответить, свяжитесь с художником: '
                                  '89212620172'
                                  '\n'
                                  'Или можете написать автору по ссылке: https://vk.com/lesyaegorova')
                send_some_msg(id, 'Спасибо за заказ!')
            elif 'врем' in msg or 'долго' in msg or 'готов' in msg or 'срок' in msg:
                send_some_msg(id, 'Вам не придется ждать долго! Это примерно займет 3-4 дня.')
            elif 'стил' in msg:
                send_some_msg(id, 'Со стилем художника вы можете ознакомиться в самом сообществе!'
                                  '\n'
                                  'Или в альбоме: https://vk.com/album-170535722_284054335')
            elif 'пок' in msg or 'до свидани' in msg:
                send_some_msg(id, 'До свидания!')
            elif 'спасибо' in msg or 'супер' in msg or 'отлично' in msg or 'хорошо' in msg or 'ок' in msg:
                send_some_msg(id, 'Всегда пожалуйста!')
            elif 'пожалуйста' in msg:
                send_some_msg(id, ':)')
            elif msg == 'нет':
                send_some_msg(id, 'Тогда зачем вы написали нам?')
            elif 'пример' in msg or 'вариант' in msg:
                send_some_msg(id,
                              'С примерами портретов вы можете ознакомиться в альбоме: https://vk.com/album-170535722_284054335')
            else:
                send_some_msg(id, 'Извините, можете написать свой вопрос конкретнее или свяжитесь с художником для '
                                  'уточнения деталей заказа по номеру телефона: 89212610172'
                                  '\n'
                                  'Или можете написать автору по ссылке: https://vk.com/lesyaegorova')

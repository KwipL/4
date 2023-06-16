import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from cb_rf import get_course
from wiki import get_article

token = "vk1.a.CMKZb_9cujA0kkUeYahbNPS1qpHqAKHDme1QmafJQf8GqUeSsuVkrYN1Yh4q291VtjKvFuwZ0uizUHNBFKJQEh07NAmQQjKHfdhPGtnpFs3zg1h72cqmjOW74vG92aDq9Gqsoqh-9xCth6HWsqbFzyWsz8ERXZjDIUSkXJ276I6Hx5bhOZFpgFOGczaxg7gp4cByTuVQamLhWdoIq_bVhg"

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_message = event.text.lower()
        user_id = event.user_id
        if user_message[:2] == '-k':
            
            response = 'Доллар стоит {0} руб. \nЕвро стоит {1} руб. \nЮань стоит руб. {2}'.format(
                get_course('R01235'), get_course('R01239'), get_course('R01375')
            )
        elif user_message[:2] == '-в':
            article = user_message[2:]
            response = get_article(article)
        else:
            response = 'Такой команды нет'
        vk.messages.send(
            user_id = user_id,
            message = response,
            random_id = random.randint(-10**8, 10**7)
        )
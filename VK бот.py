import vk_api
import random
from cb_rf import get_course

token = "vk1.a.CMKZb_9cujA0kkUeYahbNPS1qpHqAKHDme1QmafJQf8GqUeSsuVkrYN1Yh4q291VtjKvFuwZ0uizUHNBFKJQEh07NAmQQjKHfdhPGtnpFs3zg1h72cqmjOW74vG92aDq9Gqsoqh-9xCth6HWsqbFzyWsz8ERXZjDIUSkXJ276I6Hx5bhOZFpgFOGczaxg7gp4cByTuVQamLhWdoIq_bVhg"
vk = vk_api.VkApi(token=token)
while True:
    messages = vk.method('messages.getConversations', {'count':20, 'filter':'unanswered'})
    if messages['count']>0:
        message_text = messages['items'][0]['last_message']['text']
        if message_text == 'курс':
            ans = f"Курс доллара на сегодня {get_dollar_course()} руб."
        else:
            ans = 'Неизвестная команда'
        user_id = messages['items'][0]['last_message']['from_id']
        random_id = random.randint(-10**7,10**7)
        vk.method('messages.send', {
            'user_id':user_id,
            'random_id':random_id,
            'message':message_text,
        })
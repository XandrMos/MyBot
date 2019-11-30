from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
import telebot
from .lib import TOKEN

bot = telebot.TeleBot(TOKEN)
# Create your views here.

class UpdateBot(APIView):
    def post(self, request):
        json_data = request.body.decode("UTF-8")
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])

        return Response({'code': 200})
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "It's worked!!!")
    user = User()
    user.user_id = message.chat.id
    user.save()


@bot.message_handler(content_types='text')
def send_Message(message):
    bot.send_message(message.chat.id, "It's worked too!!!")


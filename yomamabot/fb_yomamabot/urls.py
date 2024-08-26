# yomamabot/fb_yomamabot/urls.py

# from django.urls import re_path

# from .views import YoMamaBotView

# urlpatterns = [

#                   re_path('MessengerWebhook', YoMamaBotView.as_view())

#                ]

from django.urls import path

from .views import MessengerWebhook
urlpatterns = [
    path('MessengerWebhook/', MessengerWebhook.as_view(), name='messenger_webhook'),
]

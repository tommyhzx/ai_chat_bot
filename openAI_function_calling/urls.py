from django.urls import path
from .views import gpt_chat

urlpatterns = [
    # 处理chat/gpt-chat/的请求
    path('gpt-chat/', gpt_chat, name='gpt_chat'),
]

from django.urls import path
from . import views

# URL conf
urlpatterns = [
    path('ping/', views.ping),
    path('download_channel_message_history/', views.download_channel_message_history),
    path('download_guild_member_data/', views.download_guild_member_data),
]
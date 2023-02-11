from django.urls import include, path
from . import views
urlpatterns = [
    path('sms_pomper', views.send_message, name='sms_pomper'),
    path('v', views.send_message_voda, name='vodafone'),
    path('e', views.send_message_etis, name='etisalat'),
    path('o', views.send_message_orange, name='orange'),

]


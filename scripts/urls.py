from django.urls import path
from . import views

urlpatterns = [
    path('scripts/', views.home_scripts, name='home_scripts'),
    #path('scripts/vodafone/tiktok', views.tiktok_sub, name='tiktok_sub'),
   # path('scripts/vodafone/youtube', views.youtube_sub, name='youtube_sub'),
    #path('scripts/vodafone/pubg', views.pubg_sub, name='pubg_sub'),
    path('scripts/vodafone/Shahid', views.shahid_sub, name='Vodafone_Shahid'),
    #path('scripts/orange/500mega', views.orange500m, name='500m_orange'),
   # path('scripts/orange/orange_bsn', views.orange4500, name='orange_bsn'),
   # path('scripts/myntra/create', views.MyNtragreat, name='MyNtragreat'),
    #path('scripts/myntra/Done', views.MyNtractivate, name='MyNtractivate'),
    #path('scripts/getNumbers', views.getNumbers, name='getNumbers'),
   # path('scripts/getNumbers/Done', views.getNumbers, name='getNumbersDone'),
    path('scripts/orange-500Mg', views.orang_500_mg, name='orange500Mg'),
    path('scripts/orange-100Mg', views.orange_100_mg, name='orange100Mg'),
]

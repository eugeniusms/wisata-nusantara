from django.urls import path
from faq.views import *

app_name = 'wishlist'

urlpatterns = [
    path('', show_faq, name='show_faq'),
    path('json/public/', show_faq_by_json_public, name='show_faq_by_json_public'),
    path('json/private/', show_faq_by_json_private, name='show_faq_by_json_private'),
    path('add/', submit_ajax, name='submit_ajax'),
    path('add_flutter/', add_faq_flutter, name='add_faq_flutter'),
    
]
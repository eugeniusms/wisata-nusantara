from django.urls import path
from faq.views import *

app_name = 'wishlist'

urlpatterns = [
    path('', show_faq, name='show_faq'),
    path('json/', show_faq_by_json_public, name='show_faq_by_json_public'),
    path('add/', submit_ajax, name='submit_ajax'),

]
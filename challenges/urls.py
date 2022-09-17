from django.urls import path
from . import views

urlpatterns = [
    # path('january',views.index),
    # path('feburary',views.feburary),
    path('',views.index, name = 'index'),
    path('<int:month>',views.monthly_challenges_by_number),
    path('<str:month>',views.montyly_challenges,name='month-challenge')
]
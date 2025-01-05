
from django.contrib import admin
from django.urls import path
from task2.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('func_view/', func_view),
    path('class_view/', Class_view.as_view()),
]

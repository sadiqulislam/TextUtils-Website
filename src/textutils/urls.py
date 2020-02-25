from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),

    path('analyzer', views.analyze, name="analyze"),

    # path('removepunctuation', views.rempunc, name="rempunc"),
    # path('capitalizefirst', views.capfirst, name="capfirst"),
    # path('newlineremove', views.newlinerem, name="newlinerem"),
    # path('spaceremove', views.spacerem, name="spacerem"),
    # path('charactercount', views.charcount, name="charcount")
]
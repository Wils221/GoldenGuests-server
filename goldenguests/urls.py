from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from goldenguestsapi.views import register_user, login_user, TicketView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tickets', TicketView, 'ticket')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

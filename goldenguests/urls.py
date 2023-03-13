from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from goldenguestsapi.views import register_user, login_user, TicketView, OpponentView, GoldenGuestView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tickets', TicketView, 'ticket')
router.register(r'opponents', OpponentView, 'opponent')
router.register(r'goldenguests', GoldenGuestView, 'goldenguest')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

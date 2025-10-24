from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from mailer import views as mail_views

urlpatterns = [
    path('', mail_views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='mailer/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('inbox/', mail_views.inbox, name='inbox'),
    path('send/', mail_views.send_message, name='send_message'),
    path('sent/', mail_views.sent_messages, name='sent_messages'),  # 👈 new
    path('admin/', admin.site.urls),
]

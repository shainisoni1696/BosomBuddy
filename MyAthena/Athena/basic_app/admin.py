from django.contrib import admin
from basic_app.models import UserProfileInfo, User,mail
from django.contrib import admin
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
#from models import  mail


# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(mail)

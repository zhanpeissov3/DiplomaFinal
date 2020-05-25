from django.forms import ModelForm
from .models import UserMessage, UserMessageService


class UserMessageForm(ModelForm):
    class Meta:
        model = UserMessage
        fields = ('user_name', 'phone_number', 'subject', 'message')


class UserMessageServiceForm(ModelForm):
    class Meta:
        model = UserMessageService
        fields = ('user_name', 'phone_number', 'service', 'message')

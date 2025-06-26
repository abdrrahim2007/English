from django.forms import ModelForm
from .models import Conversation
# Create your tests here.
class ConversationForm(ModelForm):
     class Meta:
         model = Conversation
         fields = '__all__'
         exclude = ['conversation']
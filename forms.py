from django import forms
from myapp.models import Topic,Webpage,AccessDetails,ProfilePic

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #exclude=('url',)
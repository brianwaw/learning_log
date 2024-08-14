from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Form for adding Topics"""
    class Meta:
        model = Topic
        fields = ['text']


class TopicalEntry(forms.ModelForm):
    """form for Topic Specific entries"""
    class Meta:
        model = Entry
        fields = ['text']


class EntryForm(forms.ModelForm):
    """form for adding Entries of given form"""
    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), to_field_name='text', empty_label='Select a Topic')

    class Meta:
        model = Entry
        fields = ['topic', 'text']



from django import forms
from .models import Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# email post form

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

# end of email post form

# comments form


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
#search form


class SearchForm(forms.Form):
    query = forms.CharField()

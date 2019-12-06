from django import forms

from books.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')


class LoginForm(forms.Form):
    username = forms.CharField()
    print("hello")
    password = forms.CharField(widget=forms.PasswordInput)

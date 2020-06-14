from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea
from blog.models import Post, Comments


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('author', "tittle", 'text')

        widgets = {
            'tittle': TextInput(attrs={'class': 'textinputclass'}),
            'text': Textarea(attrs={'class': 'editable medium-editor-text postcontent'})
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'text')

        widgets = {
            'tittle': TextInput(attrs={'class': 'textinputclass'}),
            'text': Textarea(attrs={'class': 'editable medium-editor-text'})
        }


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

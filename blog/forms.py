from django import forms

from blog.models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(required=True)
    to = forms.EmailField(required=True)
    comments = forms.CharField(required=True, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-lg',
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input mt-1 block w-full rounded-lg',
                'placeholder': 'Your email'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-textarea mt-1 block w-full rounded-lg',
                'placeholder': 'Your comment'
            }),
        }
        

class SearchForm(forms.Form):
    query = forms.CharField()
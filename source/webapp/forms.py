from django import forms
from webapp.models import Article, Comment, STATUS_ACTIVE, Tag


class ArticleForm(forms.ModelForm):
    tags = forms.CharField(max_length=31, required=False)
    class Meta:
        model = Article
        exclude = ['created_at', 'updated_at', 'tags']



class CommentForm(forms.ModelForm):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['article'].queryset = Article.objects.filter(status=STATUS_ACTIVE)

    # article = forms.ModelChoiceField(queryset=Article.objects.filter(status=STATUS_ACTIVE), label='Статья')

    class Meta:
        model = Comment
        exclude = ['created_at', 'updated_at']


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')

class FullSearchForm(forms.Form):
     text = forms.CharField(max_length=100, required=False, label='Текст')
     in_title = forms.BooleanField(initial=True, required=False, label='В заголовках')
     in_text = forms.BooleanField(initial=True, required=False, label='В тексте')
     in_tags = forms.BooleanField(initial=True, required=False, label='В тегах')
     in_comment_text = forms.BooleanField(initial=False, required=False, label='В тексте комментариев')

     author = forms.CharField(max_length=100, required=False, label='Автор')
     in_articles = forms.BooleanField(initial=True, required=False, label='Статей')
     in_commnets = forms.BooleanField(initial=False, required=False, label='Комментариев')
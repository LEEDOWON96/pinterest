from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # Medium Editor 를 사용하여 WYSIWYG
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left', 'style': 'height: auto'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)  # project 선택없이 아티클 생성 가능

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']

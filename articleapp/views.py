from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    # 유저 저장 부분
    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()

        return super().form_valid(form)

    # 아티클 등록 성공시 돌아갈 페이지 설정
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


# DetailView 에는 form이 들어가 있지않아 필요 시, FormMixin을 추가하고 해당 form_class 설정
class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm  # (아티클+댓글폼) 위함
    context_object_name = 'target_article'  # articleapp/detail.html 에서 pk 받을 이름 설정
    template_name = 'articleapp/detail.html'


# decorators.py 에서 article_ownership_required 설정
@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'


# urls.py 에서 list 출력위해 TemplateView 대신 사용할 ListView 생성
class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'  # list.html 에서 아티클 리스트 이름
    template_name = 'articleapp/list.html'
    paginate_by = 10  # 페이지 당 아티클 최대 개수 지정

    # 페이지 최신 정렬
    def get_queryset(self):
        article_list = Article.objects.order_by('-id')
        return article_list

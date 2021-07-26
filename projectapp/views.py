from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscriberapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    # 프로젝트 등록 성공시 돌아갈 페이지 설정
    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'  # projectapp/detail.html 에서 pk 받을 이름 설정
    template_name = 'projectapp/detail.html'
    paginate_by = 25

    # 해당 프로젝트안의 아티클 필터링 및 구독 정보 확인
    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None

        object_list = Article.objects.filter(project=self.get_object())

        return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscription=subscription,
                                                               **kwargs)


# urls.py 에서 list 출력위해 TemplateView 대신 사용할 ListView 생성
class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'  # list.html 에서 for문 프로젝트 리스트 이름
    template_name = 'projectapp/list.html'
    paginate_by = 25  # 페이지 당 아티클 최대 개수 지정

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscriberapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    # 구독 기능 설정
    def get(self, request, *args, **kwargs):
        # 예외처리: project_pk를 소유한 Project 가 없으면 404 리턴(get_object_or_404)
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        subscription = Subscription.objects.filter(user=user, project=project)

        # 구독 상태라면 버튼을 다시 누를시 구독 해제
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super(SubscriptionView, self).get(request, *args, **kwargs)

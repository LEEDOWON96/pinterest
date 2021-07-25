from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm  # 장고에서 제공되지 않아 따로 forms.py 생성
    template_name = 'profileapp/create.html'

    # forms.py 에서 빠진 user 데이터를 저장하기 위해 추가 작성
    def form_valid(self, form):
        temp_profile = form.save(commit=False)  # 임시 데이터 저장(fields = ['image', 'nickname', 'message'])
        temp_profile.user = self.request.user  # user 데이터 저장
        temp_profile.save()

        return super().form_valid(form)  # 수정이후 똑같은 함수 봔환

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm  # 장고에서 제공되지 않아 따로 forms.py 생성
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

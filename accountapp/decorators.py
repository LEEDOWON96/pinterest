from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


# 다른 사용자(user1)가 인위적인 접근 방지 위함(ex_~/delete/3)
def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()

        return func(request, *args, **kwargs)

    return decorated

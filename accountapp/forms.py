from django.contrib.auth.forms import UserCreationForm


# 회원 수정 시, 회원 아이디 수정 제한 기능
class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True

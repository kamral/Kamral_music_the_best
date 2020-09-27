from django.contrib.auth.forms import\
    UserCreationForm, \
    UserChangeForm

from .models import CustomUser

class CustomUserCreationFrom(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)


class CustomUserCreationChangeForm(UserChangeForm):

    class Meta:
        model=CustomUser
        fields=UserChangeForm.Meta.fields


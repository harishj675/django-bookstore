from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User


class userNameOrEmailAuthBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None

        try:
            if '@' in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

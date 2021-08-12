from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, mobile_number, password=None):
        if not email:
            raise ValueError(_("Users must have an email address"))
        if not username:
            raise ValueError(_("Users must have a username"))
        if not mobile_number:
            raise ValueError(_("Users must have a mobile_number"))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            mobile_number=mobile_number,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, mobile_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            mobile_number=mobile_number,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

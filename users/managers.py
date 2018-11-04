from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, authy_id, password,
                     **extra_fields):
        if not email:
            raise ValueError('Accounts must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          authy_id=authy_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, authy_id=None, password=None,
                    **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email,
            authy_id,
            password,
            **extra_fields
        )

    def create_superuser(self, email, authy_id, password,
                         **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self._create_user(
            email,
            authy_id,
            password,
            **extra_fields
        )
        user.is_admin = True
        return user

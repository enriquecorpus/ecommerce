import django.forms
import utils.email
import django.core.exceptions


def _is_email_valid(email: str):
    if not utils.email.is_valid(email):
        raise django.core.exceptions.ValidationError('Invalid Email.')


def _is_name_valid(full_name: str):
    if not len(full_name.strip()) > 1:
        raise django.core.exceptions.ValidationError('Invalid Name')


class InitRegistrationForm(django.forms.Form):
    email = django.forms.EmailField(label='Email Address', validators=[_is_email_valid])
    first_name = django.forms.CharField(label='First Name', max_length=50, validators=[_is_name_valid])
    middle_name = django.forms.CharField(label='Middle Name', max_length=50, validators=[_is_name_valid])
    last_name = django.forms.CharField(label='Last Name', max_length=50, validators=[_is_name_valid])

from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError


UserModel = get_user_model()


class SignInForm(AuthenticationForm):
    pass


class SignUpForm(UserCreationForm):
    PRODUCER = 'is_producer'
    CUSTOMER = 'is_customer'
    TYPE_CHOICES = (
        (PRODUCER, 'Producer'),
        (CUSTOMER, 'Customer'),
    )

    user_type = forms.ChoiceField(
        choices=TYPE_CHOICES,
        required=True,
        label='Sign up like:',
        help_text='If you want to sell - choose "producer", if you want to buy choose "customer"',
    )

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2', 'user_type')

    def clean(self):
        if self.cleaned_data['user_type'] == self.PRODUCER:
            self.instance.is_producer = True
        elif self.cleaned_data['user_type'] == self.CUSTOMER:
            self.instance.is_consumer = True
        else:
            raise ValidationError('Choose one of the available roles!')

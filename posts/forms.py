from django import forms
from posts.models import Review, Product


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=256)
    description = forms.CharField(widget=forms.Textarea())
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = forms.IntegerField()


class ReviewCreateForm(forms.Form):
    text = forms.CharField(max_length=256)
    product = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].choices = [(product.id, product.title) for product in Product.objects.all()]
from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput(), min_length=3)
    password2 = forms.CharField(widget=forms.PasswordInput(), min_length=3)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password =forms.CharField(widget=forms.PasswordInput(), min_length=3)


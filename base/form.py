from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . models import User, Donation, Donator


class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override the default widget attributes with Bootstrap classes
        self.fields['name'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['username'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['email'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control w-75'})

    class Meta:
        model = User
        fields = ['name', 'username', 'phone', 'email', 'password1', 'password2']


class DonationForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override the default widget attributes with Bootstrap classes
        self.fields['name'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['fund_target'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['yayasan'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['beneficiary'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['category'].widget.attrs.update({'class': 'form-control w-25'})
        self.fields['fundraising_story'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['time_span'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['thumbnail'].widget.attrs.update({'class': 'form-control w-75'})

    class Meta:
        model = Donation
        exclude = ['user', 'collected', 'created']

class DonatorForm(ModelForm):
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Override the default widget attributes with Bootstrap classes
        self.fields['amount'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control w-75'})
        self.fields['payment_method'].widget.attrs.update({'class': 'form-control w-75'})

    class Meta:
        model = Donator
        fields = ['amount', 'comment', 'payment_method']
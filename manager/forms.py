from django import forms
from multiselectfield import MultiSelectFormField

from manager.models import CaseModel, CommentModel


class NewCaseForm(forms.ModelForm):
    class Meta:
        model = CaseModel
        fields = ('role', 'farmerName', 'companyName', 'phone', 'tegName')
        tegName = MultiSelectFormField()
        widgets = {
            'role': forms.RadioSelect(
                attrs={'id': 'role', 'type': 'radio', 'required': 'True'},
            ),
            'farmerName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'имя ', 'id': "name_client"}),
            'companyName': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'название компании', 'id': 'name_company'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'телефон', 'id': 'phone_client'}),

        }


class MoreAddressForm(forms.ModelForm):
    class Meta:
        model = CaseModel
        fields = ('companyName', 'farmerName', 'phone', 'mail', 'address')
        widgets = {
            'farmerName': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'имя ', 'id': "name_client_id"}),
            'companyName': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'название компании', 'id': "name_company_id"}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'телефон', 'id': 'phone_client_id'}),
            'mail': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'email', 'id': "name_mail_id"}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'адрес', 'id': 'name_address_id'})
        }


class MoreTegsForm(forms.ModelForm):
    class Meta:
        model = CaseModel
        fields = ('tegName',)
        tegName = MultiSelectFormField()


class MoreCommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('text_comment',)
        widgets = {
            'text_comment': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'ваш комментарий', 'id': 'more_comment_id'
            })
        }

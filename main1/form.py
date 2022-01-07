from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.core import validators


from .models import CustomerUser
from .models import FeedbackModel

class Register(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields=('U_name','U_gmail','U_password', 'U_repeat_password' ,'U_phone','U_address',)
        widgets = {
            'U_name': forms.TextInput(attrs={'placeholder': 'Họ tên'}),
            'U_gmail': forms.TextInput(attrs={'type': 'email','placeholder': 'Email'}),
            'U_password': forms.PasswordInput(attrs={'placeholder': 'Mật khẩu'}),
            'U_repeat_password': forms.PasswordInput(attrs={'placeholder': 'Nhập lại mật khẩu' }),
            'U_phone': forms.TextInput(attrs={'type':'phone','placeholder': 'Số điện thoại'}),
            'U_address': forms.TextInput(attrs={'type': 'address', 'placeholder': 'Địa chỉ'})

        }
class Contact(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields=('Fb_title','Fb_content','Fb_user_id')
        widgets = {
            'Fb_title': forms.TextInput(attrs={'type': 'text','placeholder': 'Tiêu đề','value':''}),
            'Fb_content': forms.TextInput(attrs={'type': 'text','placeholder': 'Nội dung','value':''}),
            'Fb_user_id':forms.TextInput(attrs={'type': 'hidden','value' : '{{user_id}}' }),
        }






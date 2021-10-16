from django import forms
from .models import Profile,Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ProfileUpdateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Profile','Profile',css_class = 'btn-success'))

    class Meta:
        model = Profile
        fields = [
            'profile_image',
            'bio',
        ]

class CommentForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Comment','Comment',css_class = 'btn-success'))

    class Meta:
        model = Comment
        fields = [
            'body',
        ]

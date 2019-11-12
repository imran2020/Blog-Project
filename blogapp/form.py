from django import forms
from .models import article,author,comment,category,post,post_comment,About
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm


class createForm(forms.ModelForm):
    class Meta:
        model=article
        fields=[
            "title",
            "image",
            "body",
            "category",
        ]

class registerUser(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        ]

class createauthor(forms.ModelForm):
    class Meta:
        model=author
        fields=[
            "profile_picture",
            "details",
        ]

class commentForm(forms.ModelForm):
    class Meta:
        model=comment
        fields=[
            "name",
            "post_comment"
        ]

class Ccategory(forms.ModelForm):
    class Meta:
        model=category
        fields=[
            "name",

        ]

class postForm(forms.ModelForm):
    class Meta:
        model=post
        fields=[

            "body",
        ]

class Pcomment(forms.ModelForm):
    class Meta:
        model=post_comment
        fields=[

            "comment"
        ]

class U_about(forms.ModelForm):
    class Meta:
        model=About
        fields=[
            "Current_city",
            "Home_town",
            "School",
            "University",
            "Religion",
            "Nationality",
            "Meritial_status",
            "Worked_at",
        ]
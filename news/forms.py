from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    postHead = forms.CharField(min_length=5, max_length=50)
    postBody = forms.CharField(min_length=100)

    class Meta:
        model = Post
        fields = [
            'postCategory',
            'authors',
            'postHead',
            'postBody',
        ]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     description = cleaned_data.get("description")
    #     # if description is not None and len(description) < 20:
    #     #     raise ValidationError({
    #     #         "description": "Описание не может быть менее 20 символов."
    #     #     })
        
    #     name = cleaned_data.get("name")
    #     if name == description:
    #         raise ValidationError(
    #             "Описание не должно быть идентично названию."
    #         )

    #     return cleaned_data
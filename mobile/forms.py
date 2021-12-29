from django import forms
from django.contrib import messages
from mobile.models import *
from .models import Mobile


class MobileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['brand_name'].label = "Brand Name:"
        self.fields['model_name'].label = "Model Name :"
        self.fields['color'].label = "Color :"
        self.fields['image'].label = "Image :"
        self.fields['jan_code'].label = "Jan Code :"

        self.fields['brand_name'].widget.attrs.update(
            {
                'placeholder': 'Brand Name',
            }
        )
        self.fields['model_name'].widget.attrs.update(
            {
                'placeholder': 'Model Name',

            }
        )
        self.fields['color'].widget.attrs.update(
            {
                'placeholder': 'Color',
                
            }
        )
        self.fields['jan_code'].widget.attrs.update(
            {
                'placeholder': 'Jan Code',
                'required': 'required'
            }
        )
        self.fields['image'].widget.attrs.update(
            {
                'placeholder': 'Image Link',
              
            }
        )

    class Meta:
        model = Mobile
        fields = "__all__"

    def clean_color(self):
        model_name = self.cleaned_data.get('model_name')
        color = self.cleaned_data.get('color')
        is_exist = Mobile.objects.filter(model_name = model_name.id ,color = color.id).exists()
        if not is_exist:
            return color
        raise forms.ValidationError("Model with Color Already Exist")


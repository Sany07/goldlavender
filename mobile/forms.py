from django import forms
from django.contrib import messages
from mobile.models import *



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
                # 'class':'form-select appearance-none bg-gray-100 bg-opacity-50 block w-full  px-3 py-1.5 text-base text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded transition ease-in-out  m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none my-4'
                

            }
        )
        self.fields['model_name'].widget.attrs.update(
            {
                'placeholder': 'Model Name',
                
                # 'class':'form-select appearance-none bg-gray-100 bg-opacity-50 block w-full  px-3 py-1.5 text-base text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded transition ease-in-out  m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none my-4'
      

            }
        )
        self.fields['color'].widget.attrs.update(
            {
                'placeholder': 'Color',
                
                #   'class':'form-select appearance-none bg-gray-100 bg-opacity-50 block w-full  px-3 py-1.5 text-base text-gray-700 bg-white bg-clip-padding bg-no-repeat border border-solid border-gray-300 rounded transition ease-in-out  m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none my-4'
      

            }
        )
        self.fields['jan_code'].widget.attrs.update(
            {
                'placeholder': 'Jan Code',
                # 'class':'mt-4 w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-14 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out my-4'

            }
        )
        self.fields['image'].widget.attrs.update(
            {
                'placeholder': 'Image Link',
                # 'class':'mt-4 w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-14 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out my-4'

            }
        )



    class Meta:
        model = Mobile
        fields = "__all__"

    # def clean_category(self):
    #     category = self.cleaned_data.get('category')

    #     if not category:
    #         raise forms.ValidationError("Category is required")
    #     return category

    # def clean_thumbnail(self):
    #     thumbnail = self.cleaned_data.get('thumbnail')

    #     if not thumbnail:
    #         raise forms.ValidationError("Thumbnail is required")
    #     return thumbnail

    # def save(self, commit=True):
    #     course = super(CourseModelForm, self).save(commit=False)
    #     if commit:
    #         course.save()
    #     return course



from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView

from .models import Mobile, Color, Brand_Name, Model_Name
from .forms import MobileForm


class HomePageView(ListView):
    
    model = Mobile
    context_object_name = 'data'
    template_name = 'mainsite/index.html'

    def get_queryset(self):
        return self.model.objects.order_by('-id')

class  CreateMobileObjectView(CreateView, SuccessMessageMixin):
    """
        Provides the ability to Create Mobile Object
    """
    model = Mobile
    form_class = MobileForm
    template_name = 'mainsite/add_mobile.html'
    success_url = '/'
    success_message = "Data was added successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['color'] = Color.objects.all()
        context['brand_name'] = Brand_Name.objects.all()
        context['model_name'] = Model_Name.objects.all()
        print('s')
        return context

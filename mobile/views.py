
from django.views.generic import ListView, CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db.models import Q
from django.forms.models import model_to_dict


from .models import Mobile, Color, Brand_Name, Model_Name
from .forms import MobileForm


class HomePageView(ListView):
    
    model = Mobile
    context_object_name = 'data'
    template_name = 'mainsite/index.html'

    def get_queryset(self):
        return self.model.objects.order_by('-id').select_related('brand_name','color','model_name')

class  CreateMobileObjectView( SuccessMessageMixin, CreateView):
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
        return context

class DeleteProducts(SuccessMessageMixin, FormView):
    """
        Provides the ability to Delete Mobile Objects
    """
    success_message = "Products are deleted successfully."
    error_message = "Something went wrong."
    def post(self, request, *args, **kwargs):
        mobile = self.request.POST.getlist('mobile')
        print('mobile',mobile)
        is_true = Mobile.objects.filter(pk__in=mobile).delete()
        if len(is_true) > 0:
            messages.success(self.request, self.success_message)
        else:
            messages.error(self.request, self.error_message)
        return redirect('mainsite:home')


def Search_Phone(request):
    """
        Ajax Based Search
    """
    if request.is_ajax():
        model_or_jancodee = request.GET.get('query',None)
        if model_or_jancodee:
            data = Mobile.objects.filter(
                Q(jan_code__iexact=model_or_jancodee)|
                Q(model_name__model_name__iexact=model_or_jancodee)
            ).select_related('brand_name','color','model_name').distinct()
            mobile_list=[]
            if data:
                for item in data:
                    data ={
                        'id' : item.pk,
                        'brand_name': item.brand_name.brand_name,
                        'model_name': item.model_name.model_name,
                        'color': item.color.color,
                        'jan_code': item.jan_code,
                        'image': item.image
                    }
                    mobile_list.append(data)
                data={  'data':mobile_list } 
                return JsonResponse(data)
            return JsonResponse({'msg': 'No exact data found '})
    else:
        return JsonResponse({})

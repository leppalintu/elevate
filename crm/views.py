import math
from random import random

from django.db.models import Max
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, View
from .models import Country


# Create your views here.
class HomePageView(ListView):
    model = Country
    template_name = 'crm/index.html'
    paginate_by = 10
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['title'] = 'Homepage'
        return context


class SearchResultView(View):
    model = Country
    template_name = 'crm/index.html'
    paginate_by = 10
    ordering = ['name']

    def post(self, request, *args, **kwargs):

        if request.POST.get('search'):

            phrase = request.POST.get('q')

            if phrase and len(phrase) > 2:
                results = Country.objects.filter(name__icontains=phrase).order_by('name')
                if results:
                    return render(request, self.template_name,
                                  {'object_list': results, 'title': 'Search Results', 'q': phrase})
        if request.POST.get('random'):
            total = len(Country.objects.all())
            object_list = get_random_item(Country, total)[:5]
            return render(request, self.template_name, {'object_list': object_list})

        return redirect('index')


def error_404(request, *args, **kwargs):
    return render(request, '404.html', status=404)


def error_500(request, *args, **kwargs):
    return render(request, '500.html', status=500)


def get_random_item(model, max_id=None):
    if max_id is None:
        max_id = model.objects.aggregate(Max('id')).values()[0]
    min_id = math.ceil(max_id * random())
    return model.objects.filter(id__gte=min_id)

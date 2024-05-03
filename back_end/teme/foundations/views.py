import json

from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from foundations.models import Foundation
from django.http import JsonResponse
from foundations import forms

class CreateView(View):
    def post(self, request, *args, **kwargs):
        post_data = request.body.decode('utf-8')
        form = forms.FoundationForm(json.loads(post_data))
        if not form.is_valid():
            return JsonResponse({'status': 'error', 'message': form.errors})
        
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')

        try:
            Foundation.objects.create(email=email, name=name)
            return JsonResponse({'status': 'ok', 'message': 'Foundation created successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        
class ListView(View):
    def get(self, request, *args, **kwargs):
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 10))
        start = (page - 1) * limit
        end = start + limit
        foundations = Foundation.objects.filter(id__gte=start, id__lt=end)
        return JsonResponse({'status': 'ok', 'data': [foundation.to_dict() for foundation in foundations]})

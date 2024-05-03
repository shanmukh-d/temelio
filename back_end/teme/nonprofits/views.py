from django.shortcuts import render
import json

# Create your views here.
from django.views.generic.base import View
from nonprofits.models import Nonprofit, SentEmails
from django.http import JsonResponse
from nonprofits import forms
from common import public as common_public
from common.decorators import permission_required, login_required


class CreateView(View):
    @login_required
    @permission_required('create_nonprofit')
    def post(self, request, *args, **kwargs):
        post_data = request.body.decode("utf-8")
        form = forms.NonProfitForm(json.loads(post_data))
        if not form.is_valid():
            return JsonResponse({"status": "error", "message": form.errors})
        
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        address = form.cleaned_data.get("address")

        try:
            Nonprofit.objects.create(email=email, address=address, name=name)
            return JsonResponse({"status": "ok", "message": "Nonprofit created successfully"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)

class ListView(View):
    def get(self, request, *args, **kwargs):
        page = int(request.GET.get("page", 1))
        limit = int(request.GET.get("limit", 10))
        start = (page - 1) * limit
        end = start + limit
        print(Nonprofit.objects.all())
        nonprofits = Nonprofit.objects.filter(id__gte=start, id__lt=end)
        return JsonResponse({"status": "ok", "data": [nonprofit.to_dict() for nonprofit in nonprofits]})
    
class SentMailsListView(View):
    def get(self, request, *args, **kwargs):
        page = int(request.GET.get("page", 1))
        limit = int(request.GET.get("limit", 10))
        start = (page - 1) * limit
        end = start + limit
        emails = SentEmails.objects.filter(id__gte=start, id__lt=end)
        return JsonResponse({"status": "ok", "data": [email.to_dict() for email in emails]})
    
class SendMailView(View):
    @login_required
    @permission_required('send_mail')
    def post(self, request, *args, **kwargs):
        post_data = request.body.decode("utf-8")
        data = json.loads(post_data)
        user = request.user
        from_email = user.email
        to_emails = data.get("to_emails") or []
        subject = data.get("subject") or 'Money Credit Alert!'
        # message = data.get("message")  if wanted to send a custom message to each email

        
        try:
            for to_email in to_emails:
                email_content = f'Sending money to Non profit: {to_email}'
                # can also batch and send these emails asynchronously
                SentEmails.objects.create(sent_from=from_email, sent_to=to_email, subject=subject, message=email_content)
            return JsonResponse({"status": "ok", "message": "Email sent successfully"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
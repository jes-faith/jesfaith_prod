from django.views.generic import TemplateView
from django.shortcuts import redirect
from .model_db import PrayerRequest


class HomePageView(TemplateView):
    template_name = "home.html"
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        try:
            PrayerRequest(
                name=name,
                email=email,
                message=message
            ).save()
        except Exception as e:
            print(f"Failed to save prayer request: {e}")
            pass

        return redirect("thank_you")
    
    

class AboutPageView(TemplateView):
    template_name = "about.html"

class ServicePageView(TemplateView):
    template_name = "service.html"

class ThankYouView(TemplateView):
    template_name = "thank_you.html"
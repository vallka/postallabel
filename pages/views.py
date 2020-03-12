from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class MainPageView(TemplateView):
    template_name = 'pages/main.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ServicesPageView(TemplateView):
    template_name = 'pages/services.html'    
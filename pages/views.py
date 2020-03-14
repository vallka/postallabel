import uuid
from django.conf import settings

from django.views.generic import TemplateView
from django.http import HttpResponse

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class MainPageView(TemplateView):
    template_name = 'pages/main.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class ServicesPageView(TemplateView):
    template_name = 'pages/services.html'    



from django.utils.html import escape
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def putfile(request):
    filename = str(uuid.uuid1()) + '.pdf'
    f = open(os.path.join(settings.MEDIA_ROOT,filename)   ,'wb')
    f.write(request.body)
    f.close()

    return HttpResponse(os.path.join(settings.MEDIA_URL,filename))


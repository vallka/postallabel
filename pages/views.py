import uuid
import os
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

    filename = request.GET.get('filename',str(uuid.uuid1()) + '.pdf')

    f = open(os.path.join(settings.MEDIA_ROOT,filename)   ,'wb')
    f.write(request.body)
    f.close()

    
    import pprint
    print('*GET*')
    pprint.pprint(request.GET)
    print('*POST*')
    pprint.pprint(request.POST)

    if not settings.LOCAL:
        newfile = process_pdf(os.path.join(settings.MEDIA_ROOT,filename))
        return HttpResponse(os.path.join(settings.MEDIA_URL,filename+'-dymo.pdf'))
    else:
        return HttpResponse(os.path.join(settings.MEDIA_URL,filename))




def process_pdf(file):

    from pdf2image import convert_from_path, convert_from_bytes

    from pdf2image.exceptions import (
        PDFInfoNotInstalledError,
        PDFPageCountError,
        PDFSyntaxError
    )


    images = convert_from_path(file)

    for i in images:
        doPage(i,file,'dpd')

    return file+'-dymo.pdf'

def doPage(image,input,typ):
    typs = {
        'dpd': {
            'cropBox' : (156,139,947,949),
            'down' : 17,
        },
        'hermes': {
            'cropBox' : (156-80,139-62,947-160,949+47),
            'down' : 17,
        },
    }


    cropBox = typs[typ]['cropBox']
    down = typs[typ]['down']

    #print (images)

    print (image.size)
    image2 = image.crop(cropBox)

    #image2.save(input + '-2.pdf')

    w = image2.size[0]
    h = image2.size[1]

    print (w,h)

    top = image2.crop((0,0,w, h/2-down))
    bot = image2.crop((0,h/2-down,w, h))

    image3 = top.crop((0,0,w*2, h/2-down))

    image3.paste(bot,(w+1,0))

    print (image3.size)

    if os.path.isfile(input+'-dymo.pdf'):
        image3.save(input+'-dymo.pdf', append=True)
    else:    
        image3.save(input+'-dymo.pdf', append=False)





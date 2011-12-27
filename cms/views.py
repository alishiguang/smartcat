# Create your views here.

from smartcat.cms.models import *
from django.shortcuts import render_to_response

def index(request):
    guestbook_list=Guestbook.objects.all()
    return render_to_response('cms/index.html',{'guestbook_list':guestbook_list})

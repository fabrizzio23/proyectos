# Create your views here.
from principal.models import Fotos
from principal.forms import FotosForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def inicio(request):
   datos = Fotos.objects.all()
   formulario = FotosForm()
   if request.method == 'POST':
      formulario = FotosForm(request.POST, request.FILES)
      if formulario.is_valid():
         formulario.save()
         return HttpResponseRedirect('/')
	    
   return render_to_response('inicio.html',{'formulario':formulario, 'datos': datos}, context_instance=RequestContext(request))
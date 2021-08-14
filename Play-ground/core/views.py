from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name="core/home.html"

    "FORMA BASICA DE DICCIONARIO DE CONTEXTO PARA UN SOLO VALOR"
    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SALUDO'] = "HOLA A TODOS"
        context["otro"] = 1
        context["carros"] = Carro.objects.all() ====> para llamar todos los elementos del modelo
        return context"""

    "FORMA 2"
    def get(self,request, *args,**kwargs):
        return render(request, self.template_name,{'SALUDO':"HOLA A TODOS"})


class SamplePageView(TemplateView):
    template_name = "core/sample.html"
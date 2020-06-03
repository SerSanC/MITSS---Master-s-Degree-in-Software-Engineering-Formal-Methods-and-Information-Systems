from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import *
from .models import Choice, Question, Peliculas,Socios
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, DetailView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
            """
            Excludes any questions that aren't published yet.
            """
            return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class PeliculasCreate(generic.CreateView):
    model = Peliculas
    form_class = PeliculaForm
    template_name = "polls/peliculas_create.html"
    success_url = reverse_lazy('peliculas_manage')

    def form_valid(self, request):
        print(self.request)
        if self.request.method == "POST":
            print("antes")
            form = PeliculaForm(self.request.POST)
            print(form.data)
            if form.is_valid():
                print("valid")
                pelicula = Peliculas()
                pelicula.director = form.data['director']
                pelicula.fecha_de_estreno = form.data['fecha_de_estreno']
                pelicula.nombre = form.data['nombre']
                pelicula.precio_alquiler = form.data['precio_alquiler']
                pelicula.videoclub_dato = form.data['videoclub_dato']
                pelicula.key = Videoclub.objects.get(id=pelicula.videoclub_dato)
                post = pelicula.save()
                print(post)
                """post = form.save(commit=False)
                post.author = self.request.user
                post.published_date = timezone.now()
                post.save()"""
            return redirect('/videoclub/peliculas') 
        else:
            print("else")
            form = PeliculaForm()

class SociosCreate(generic.CreateView):
    model = Socios
    form_class = SociosForm
    template_name = "polls/socios_create.html"
    success_url = reverse_lazy('socios_manage')

    def form_valid(self, request):
        if self.request.method == "POST":
            print("antes")
            form = SociosForm(self.request.POST)
            if form.is_valid:
                print("valid")
                socios = Socios()
                socios.nombre = form.data['nombre']
                socios.edad = form.data['edad']
                socios.email = form.data['email']
                socios.sexo = form.data['sexo']
                post = socios.save()
            return redirect('/videoclub/socios') 
        else:
            print("else")
            form = SociosForm()       

class AltaCreate(generic.CreateView):
    model = Alquileres
    form_class = AlquileresForm
    template_name = "polls/alquiler_create.html"
    success_url = reverse_lazy('alquiler_manage')

    def form_valid(self, request):
        if self.request.method == "POST":
            print("antes")
            form = AlquileresForm(self.request.POST)        
            if form.is_valid:
                alquiler = Alquileres()
                alquiler.fecha_de_devolucion = form.data['fecha_de_devolucion']
                alquiler.fecha_de_recogida = form.data['fecha_de_recogida']
                alquiler.total_a_pagar = form.data['total_a_pagar']
                post = alquiler.save()
            return redirect('/videoclub/alquiler') 
        else:
            print("else")
            form = AlquileresForm()               

class AltaEstadistica(generic.CreateView):
    model = Estadisticas
    form_class = EstadisticasForm
    template_name = "polls/estadisticas_create.html"
    success_url = reverse_lazy('alquiler_manage')

    def form_valid(self, form):
        if form.is_valid:
            messages.success(
                self.request,
                "{} se ha añadido a la base de datos".format(
                        form.cleaned_data['titulo']
                    ),
                extra_tags='add success'
            )
            return super(AltaEstadistica, self).form_valid(form)
        else:
            messages.error(self.request, "Algo ha salido mal")            

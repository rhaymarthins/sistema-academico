from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Matricula, Curso
from django.utils import timezone

# Create your views here.
def index(request):
    matriculas = Matricula.objects.all()
    cursos = Curso.objects.order_by('codigo').filter(ativo=True)

    dados = {
        'matriculas' : matriculas,
        'cursos' : cursos,
    }
    return render(request, 'index.html', dados)

def cadastro(request):
    return render(request, 'cadastro.html')


def edu(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    data_acesso = timezone.now()
    curso_a_exibir = {
        'curso': curso,
        'data_acesso' : data_acesso
    }
    return render(request, 'curso.html', curso_a_exibir)


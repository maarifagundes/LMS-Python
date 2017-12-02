from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from core.models import Curso, Aluno
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def get(self, request):
    form = LoginForm()
    NovoUsu = NovoUsu.objects.all()

    args = {'form':form,'NovoUs':novousu}
    return render(request, self.template_name,args)
def index(request):
    return render(request, "index.html", {})

def contato(request):
    return render(request,"contato.html", {})

def noticias(request):
    return render(request,"noticias.html", {})

def novocurso(request):
    return render(request,"novocurso.html", {})

def ads(request):
    return render(request,"ads.html", {})

def esquecisenha(request):
    return render(request,"esquecisenha.html", {})
    
def novousu(request):
    if request.method == 'POST':
        form = NovoUsuForm(request.POST)
        if form.is_valid():
            numRa = request.POST.get('ra', '')
            txtCel= request.POST.get('celular', '')
            txtEmail = request.POST.get('email', '')
            txtNome = request.POST.get('nome', '')
            txtSenha = request.POST.get('senha', '')
            numRa.save()
            txtCel.save()
            txtEmail.save()
            txtNome.save()
            txtSenha.save()
         #   novousu_obj = NovoUsu(numRa=numRa,txtCel=txtCel,txtEmail=txtEmail,txtNome = txtNome, txtSenha=txtSenha)
          #  novousu_obj.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            form = NovoUsuForm()

    return render(request,"novousu.html", {})

def banana(requisicao):
    contexto = {
        "cursos": Curso.objects.all(),
    }
    return render(requisicao,"index.html",contexto)

def checa_aluno(usuario):
    return usuario.perfil == "A"

def checa_professor(usuario):
    return usuario.perfil == "P"

@login_required(login_url="/login")
@user_passes_test(checa_aluno)
def aluno(request):
    return render(request,"aluno.html")
    
@login_required(login_url="/login")
@user_passes_test(checa_professor)
def professor(request):
    return render(request,"professor.html")

def contato(request):
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.envia_email()
    else:
        form = ContatoForm()
    contexto = {
        "form":form
    }
    return render(request,"contato.html", contexto)

def cursos(request):
    contexto = {
        "cursos":Curso.objects.all()
    }
    return render(request,"cursos.html", contexto)

def curso (request, id):
    contexto = {
        "curso":Curso.objects.get(id=id)
    }
    return render(request,"curso.html", contexto)
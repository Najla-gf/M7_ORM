from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, PropertySearchForm
from django.http import JsonResponse
from .models import Inmueble, Comuna, Region, TipoInmueble


# Create your views here.
#Pagina de inicio con buscador
def index(request):
    form = PropertySearchForm()
    properties = Inmueble.objects.all()

    if request.GET:
        form = PropertySearchForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['tipo_inmueble']:
                properties = properties.filter(tipo_inmueble=form.cleaned_data['tipo_inmueble'])
            if form.cleaned_data['region']:
                properties = properties.filter(region=form.cleaned_data['region'])
            if form.cleaned_data['comuna']:
                properties = properties.filter(comuna=form.cleaned_data['comuna'])

    context = {
        'form': form,
        'properties': properties,
        'regiones': Region.objects.all()  # Aseguramos que las regiones estén en el contexto
    }
    return render(request, 'index.html', context)

#funcion para filtrar comunas segun la region
def load_comunas(request):
    region_id = request.GET.get('region_id')
    comunas = Comuna.objects.filter(region_id=region_id).order_by('nombre')
    return JsonResponse(list(comunas.values('id', 'nombre')), safe=False)

#formulario de registro
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tu cuenta fue creada con éxito. Ahora puedes iniciar sesión')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


#Vista del perfil
@login_required
def profile(request):
    return render(request, 'profile.html')

#Actualizar perfil
@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'¡Tu perfil ha sido actualizado!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form
    }
    return render(request, 'edit_profile.html', context)


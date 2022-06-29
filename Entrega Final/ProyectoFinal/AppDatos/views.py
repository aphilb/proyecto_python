from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppDatos.forms import AutoFormulario, CamionetaFormulario, MotoFormulario
from AppDatos.models import Auto, Camioneta, Moto

def inicio(request):

      return render(request, "inicio.html")


def automoviles(request):

      if request.method == 'POST':

            autoForm = AutoFormulario(request.POST)

            print(autoForm)

            if autoForm.is_valid:

                  informacion = autoForm.cleaned_data
                  print(informacion)
                  automovil = Auto (fabricante=informacion['Fabricante'], modelo=informacion['Modelo'],segmento=informacion['Segmento'], cantidadDeCilindros=informacion['Cant. de Cilindros'], cilindrada=informacion['Cilindrada']) 

                  automovil.save()

            return render(request, "inicio.html")

      else: 

            autoForm= AutoFormulario()

      return render(request, "automovil.html", {"autoForm":autoForm})

def camionetas(request):

      if request.method == 'POST':

            camForm =CamionetaFormulario(request.POST)

            print(camForm)

            if camForm.is_valid:

                  informacion = camForm.cleaned_data
                  print(informacion)
                  camioneta = Camioneta (fabricante=informacion['Fabricante'], modelo=informacion['Modelo'],tipo=informacion['Tipo'], cantidadDeCilindros=informacion['Cant. de Cilindros'], cilindrada=informacion['Cilindrada']) 

                  camioneta.save()

            return render(request, "inicio.html")

      else: 

            camForm= CamionetaFormulario()

      return render(request, "camioneta.html", {"camForm":camForm})

def motos(request):

      if request.method == 'POST':

            motoForm = MotoFormulario(request.POST)

            print(motoForm)

            if motoForm.is_valid:

                  informacion = motoForm.cleaned_data
                  print(informacion)
                  moto = Moto (fabricante=informacion['Fabricante'], modelo=informacion['Modelo'],cantidadDeCilindros=informacion['Cant. de Cilindros'], cilindrada=informacion['Cilindrada']) 

                  moto.save()

            return render(request, "inicio.html")

      else: 

            motoForm= CamionetaFormulario()

      return render(request, "moto.html", {"motoForm":motoForm})

def buscar(request):

      if  request.GET["auto"]: #if request.method == 'Get':

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            fabricante = request.GET['auto'] 
            print(fabricante)
            modelo = Auto.objects.filter(fabricante__icontains=fabricante)
            print(modelo)
            return render(request, "inicio.html", {"Fabricante":fabricante, "Modelo":modelo})

      else: 

	      respuesta = "No enviaste datos"
            
      return render(request,"inicio.html", {"respuesta":respuesta})
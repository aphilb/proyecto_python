from django import forms

class AutoFormulario(forms.Form):

    fabricante=forms.CharField(max_length=30)
    modelo=forms.CharField(max_length=30)
    segmento=forms.CharField(max_length=30)
    cantidadDeCilindros=forms.IntegerField()
    cilindrada=forms.IntegerField()

class CamionetaFormulario(forms.Form):

    fabricante=forms.CharField(max_length=30)
    modelo=forms.CharField(max_length=30)
    tipo=forms.CharField(max_length=30)
    cantidadDeCilindros=forms.IntegerField()
    cilindrada=forms.IntegerField()

class MotoFormulario(forms.Form):

    fabricante=forms.CharField(max_length=30)
    modelo=forms.CharField(max_length=30)
    cantidadDeCilindros=forms.IntegerField()
    cilindrada=forms.IntegerField()
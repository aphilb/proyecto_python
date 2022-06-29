from django.db import models

class Auto(models.Model):

    fabricante=models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    segmento=models.CharField(max_length=30)
    cantidadDeCilindros=models.IntegerField()
    cilindrada=models.IntegerField()

class Camioneta(models.Model):

    fabricante=models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    tipo=models.CharField(max_length=30)
    cantidadDeCilindros=models.IntegerField()
    cilindrada=models.IntegerField()

class Moto(models.Model):

    fabricante=models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    cantidadDeCilindros=models.IntegerField()
    cilindrada=models.IntegerField()
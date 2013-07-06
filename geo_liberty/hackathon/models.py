# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from geo_liberty.models import Municipio

class DadosBF(models.Model):
	cod_ibge = models.ForeignKey(Municipio)
	nome = models.CharField(max_length=64)
	idh = models.DecimalField(max_digits=5,decimal_places=5)
	prefeito = models.CharField(max_length=128)
	partido = models.CharField(max_length=64)
	populacao = models.IntegerField()
	familias_cadunico = models.IntegerField()
	familias_bf = models.IntegerField()
	pobres_urbano = models.IntegerField()
	pobres_rural = models.IntegerField()
	pobres_total = models.IntegerField()
	indice = models.DecimalField(max_digits=64,decimal_places=64)


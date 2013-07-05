# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from geo_liberty.models import Municipio

class Pactuacoes(models.Model):
	
	periodo = models.CharField(max_length=256)
	regiao = models.CharField(max_length=32)
	uf = models.CharField(max_length=4)
	municipio = models.ForeignKey(Municipio)
	redeOfertante = models.CharField(max_length=256)
	unidadeEnsino = models.CharField(max_length=256)
	unidadeEnsinoMatriz = models.CharField(max_length=256)
	demandante = models.CharField(max_length=256)
	tipoCurso = models.CharField(max_length=128)
	eixoTecnologico = models.CharField(max_length=128)
	curso = models.CharField(max_length=128)
	cargaHoraria = models.CharField(max_length=8)
	vagas = models.CharField(max_length=8)
	situacao = models.CharField(max_length=16)
	situacaoDemandante = models.CharField(max_length=64)

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


# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.gis.gdal import SpatialReference,CoordTransform
from django.contrib.auth import authenticate, login, logout
from geo_liberty.models import Municipio
from hackathon.models import DadosBF
from decimal import *

def Inicio (request):
	
	return render_to_response('index.html', RequestContext(request,{}))

def Pobreza(request):

	dadosbfp = DadosBF.objects.order_by('indice')[:50]
	dadosbfr = DadosBF.objects.order_by('-indice')[:50]
	dadosbfm = DadosBF.objects.all().filter(indice=29)[:50]
	ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
	for d in dadosbfp:
		d.cod_ibge.mpoly.transform(ct)
		#d.indice = Decimal(d.indice)
	for e in dadosbfr:
		e.cod_ibge.mpoly.transform(ct)
		#e.indice = Decimal(e.indice)
	for m in dadosbfm:
		m.cod_ibge.mpoly.transform(ct)
		print m.cod_ibge.mpoly
		#m.indice = Decimal(e.indice)
	return render_to_response('pobreza.html', RequestContext(request,{'dadosbfr':dadosbfr, 'dadosbfp': dadosbfp, 'dadosbfm': dadosbfm}))


def Vagas(request,id_municipio):

	dadosbf = DadosBF.objects.filter(cod_ibge = id_municipio)
	#vagas = 
	for d in dadosbf:
		if(d.populacao != None and d.pobres_total != None):
			d.indice = d.populacao / d.pobres_total
	
	return render_to_response('pobreza.html', RequestContext(request,{'dadosbf':dadosbf}))
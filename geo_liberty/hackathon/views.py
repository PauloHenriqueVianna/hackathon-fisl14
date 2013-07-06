# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.gis.gdal import SpatialReference,CoordTransform
from django.contrib.auth import authenticate, login, logout
from django.db.models import Avg
from geo_liberty.models import Municipio, Uf
from hackathon.models import DadosBF
from decimal import *

def Inicio (request):

	ufs = Uf.objects.all().order_by('uf');
	return render_to_response('index.html', RequestContext(request,{'ufs':ufs}))

def Pobreza(request):

	ufs = Uf.objects.all().order_by('uf');
	dadosbfp = DadosBF.objects.order_by('indice')[:50]
	dadosbfr = DadosBF.objects.order_by('-indice')[:50]
	dadosbfm = DadosBF.objects.all().filter(indice=29)[:50]
	ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
	for d in dadosbfp:
		d.cod_ibge.mpoly.transform(ct)
	for e in dadosbfr:
		e.cod_ibge.mpoly.transform(ct)
	for m in dadosbfm:
		m.cod_ibge.mpoly.transform(ct)
	return render_to_response('pobreza.html', RequestContext(request,{'dadosbfr':dadosbfr, 'dadosbfp': dadosbfp, 'dadosbfm': dadosbfm, 'ufs':ufs}))

def PobrezaEstado(request,id_uf):
	
	ufs = Uf.objects.all().order_by('uf');
	avg = DadosBF.objects.filter(cod_ibge__microRegiao__mesoRegiao__uf__id=id_uf).aggregate(Avg('indice'))
	num = DadosBF.objects.filter(cod_ibge__microRegiao__mesoRegiao__uf__id=id_uf).count()
	media = avg.get('indice__avg')
	media1 = media - 0.5
	media2 = media + 0.5
	media3 = num / 3
	dadosbfp = DadosBF.objects.filter(cod_ibge__microRegiao__mesoRegiao__uf__id=id_uf).order_by('indice')[:media3]
	dadosbfr = DadosBF.objects.filter(cod_ibge__microRegiao__mesoRegiao__uf__id=id_uf).order_by('-indice')[:media3]
	dadosbfm = DadosBF.objects.all().filter(indice__range=(media1, media2),cod_ibge__microRegiao__mesoRegiao__uf__id=id_uf)[:media3]
	ct = CoordTransform(SpatialReference('EPSG:4326'), SpatialReference('EPSG:900913'))
	for d in dadosbfp:
		d.cod_ibge.mpoly.transform(ct)
	for e in dadosbfr:
		e.cod_ibge.mpoly.transform(ct)
	point = ''
	centro = Uf.objects.filter(id=id_uf)
	for c in centro:
		c.mpoly.transform(ct)
		point = c.mpoly
	print point.centroid.x
	lat = str(point.centroid.x).replace(',','.')
	lon = str(point.centroid.y).replace(',','.')
	for m in dadosbfm:
		m.cod_ibge.mpoly.transform(ct)
	return render_to_response('pobreza-estado.html', RequestContext(request,{'dadosbfr':dadosbfr, 'dadosbfp': dadosbfp, 'dadosbfm': dadosbfm, 'ufs':ufs, 'lat':lat, 'lon':lon}))

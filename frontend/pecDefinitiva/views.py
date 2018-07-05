# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
########################
###### HOME VIEW #######
########################

def home(request):
	return render(request, 'home.html')


@csrf_exempt
def get_ajax_calidad_country(request):
	result_set = {"response":[],"error":"" }
	
	try:
		#conexion con bbdd (ficheros csv)
		resp_data = get_data_calidad_media()
		result_set["response"] = resp_data
	except:
		result_set["error"] = "No se ha podido establecer la conexion con la bbdd (csv)"
	
	return JsonResponse(result_set, safe=False)

@csrf_exempt
def get_ajax_precio_country(request):
	result_set = {"response":[],"error":"" }
	
	try:
		#conexion con bbdd (ficheros csv)
		resp_data = get_data_precio_medio_por_pais()
		result_set["response"] = resp_data
	except:
		result_set["error"] = "No se ha podido establecer la conexion con la bbdd (csv)"
	
	return JsonResponse(result_set, safe=False)

@csrf_exempt
def get_ajax_precio_puntuacion(request):
	result_set = {"response":[],"error":"" }
	
	try:
		#conexion con bbdd (ficheros csv)
		resp_data = get_data_precio_medio_por_puntuacion()
		result_set["response"] = resp_data
	except:
		result_set["error"] = "No se ha podido establecer la conexion con la bbdd (csv)"
	
	return JsonResponse(result_set, safe=False)

@csrf_exempt
def get_ajax_vinos_pais(request):
	result_set = {"response":[],"error":"" }
	
	try:
		#conexion con bbdd (ficheros csv)
		resp_data = get_data_vinos_por_pais()
		result_set["response"] = resp_data
	except:
		result_set["error"] = "No se ha podido establecer la conexion con la bbdd (csv)"
	
	return JsonResponse(result_set, safe=False)

@csrf_exempt
def get_ajax_calidad_precio(request):
	result_set = {"response":[],"error":"" }
	
	try:
		#conexion con bbdd (ficheros csv)
		resp_data = get_calidad_precio()
		result_set["response"] = resp_data
	except:
		result_set["error"] = "No se ha podido establecer la conexion con la bbdd (csv)"
	
	return JsonResponse(result_set, safe=False)

@csrf_exempt
def get_ajax_description(request):
	result_set = {"response":[],"error":"" }
	
	try:
		#conexion con bbdd (ficheros csv)
		resp_data = get_description()
		result_set["response"] = resp_data
	except:
		result_set["error"] = "No se ha podido establecer la conexion con la bbdd (csv)"
	
	return JsonResponse(result_set, safe=False)

	
	
########################################
# FUNCIONES AUXILIARES A LA BBDD (CSV) #
########################################
def get_data_calidad_media():
	list_data = [{'key': "Calidad media",'values':[]}]
	with open('../backend/bbdd/calidad_media.csv', 'r') as read_file:
		header = read_file.readline()
		for line in read_file:
			obj = {}
			my_line = line.strip().split(',')
			obj['label'] = my_line[0]
			obj['value'] = my_line[1]
			list_data[0]['values'].append(obj)
	return list_data

def get_data_precio_medio_por_pais():
	list_data = []
	with open('../backend/bbdd/precio_medio.csv', 'r') as read_file:
		header = read_file.readline()
		for line in read_file:
			obj = {}
			my_line = line.strip().split(',')
			obj['label'] = my_line[0]
			obj['value'] = round(float(my_line[1]),0)
			list_data.append(obj)
	return list_data

def get_data_precio_medio_por_puntuacion():
	list_data = [{'key': "Precio medio por puntuacion",'values':[]}]
	with open('../backend/bbdd/precio_medio_por_puntuacion.csv', 'r') as read_file:
		header = read_file.readline()
		for line in read_file:
			obj = {}
			my_line = line.strip().split(',')
			obj['label'] = my_line[0]
			obj['value'] = round(float(my_line[1]),0)
			list_data[0]['values'].append(obj)
	return list_data

def get_data_vinos_por_pais():
	list_data = []
	with open('../backend/bbdd/vinos_por_pais.csv', 'r') as read_file:
		header = read_file.readline()
		for line in read_file:
			obj = {}
			my_line = line.strip().split(',')
			obj['label'] = my_line[0]
			obj['value'] = round(float(my_line[1]),0)
			list_data.append(obj)
	return list_data

def get_calidad_precio():
	list_data = []
	with open('../backend/bbdd/data_israel.csv', 'r') as read_file:
		header = read_file.readline()
		obj = {}
		obj['key'] = ''
		obj['values'] = []
		for line in read_file:
			my_line = line.replace('\r\n','').strip().split('€')
			province = my_line[7]
			transform_province = transform(province)
			obj_multichart = {}
			obj['key'] = my_line[2]
			try:
				obj_multichart['x'] = round(float(my_line[6]),0)
			except:
				obj_multichart['x'] = 0
			obj_multichart['y'] = transform_province
			obj_multichart['size'] = my_line[5]
			obj_multichart['shape'] = "circle"
			obj['values'].append(obj_multichart)
		list_data.append(obj)
	return list_data

def transform(province):

	province_json = ['Upper Galilee','Golan Heights','Galilee','Judean Hills','Samson','Galil','Jerusalem Hills',
					'Shomron','Haut-Judeé','Negev','Dan','Israel','Negev Hills','Ella Valley']
	codigo = 0
	if province in province_json:
		return province_json.index(province)
	else:
		return 0
			
def get_description():
	description = ""
	with open('../backend/bbdd/data_israel.csv', 'r') as read_file:
		header = read_file.readline()
		for line in read_file:
			my_line = line.strip().split('€')
			desc = my_line[3]
			description += desc + ". "
	
	description = clear_stopwords(description)
	return description

def clear_stopwords(text):
	clean_text = text.lower()
	with open('../backend/stopwords.csv', 'r') as read_file:
		for line in read_file:
			word = line.strip()
			if " " +word+ " " in clean_text:
				clean_text = clean_text.replace(" " +word+ " ",' ')
	
	return clean_text
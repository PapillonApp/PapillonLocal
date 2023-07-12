# importe les modules importants
from pyexpat.errors import messages
import hug
import pronotepy
import datetime
import time
import secrets
import falcon
import json
import socket


# import resource
# resource.setrlimit(resource.RLIMIT_CORE, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

# importe les ENT
from pronotepy.ent import *

from wsgiref.simple_server import make_server
from os.path import dirname, join
from typing import Tuple, Union, List, Dict, Optional



API_VERSION = "3.5.1-android"
cas_list_raw = """
[
    {
      "name": "Aucun ENT",
      "url": "index-education.net",
      "py": ""
    },
    {
      "name": "Académie de Clermont-Ferrand (Ma Classe En Auvergne Rhône-Alpes)",
      "url": "cas.ent.auvergnerhonealpes.fr",
      "py": "ac_clermont_ferrand"
    },
    {
      "name": "Académie de Grenoble (Ma Classe En Auvergne Rhône-Alpes)",
      "url": "cas.ent.auvergnerhonealpes.fr",
      "py": "ac_grenoble"
    },
    {
      "name": "Académie de la Réunion (Métice)",
      "url": "sso.ac-reunion.fr",
      "py": "ac_reunion",
      "educonnect": true
    },
    {
      "name": "Académie de Lyon (Ma Classe En Auvergne Rhône-Alpes)",
      "url": "cas.ent.auvergnerhonealpes.fr",
      "py": "ac_lyon"
    },
    {
      "name": "Académie de Montpellier (Mon ENT Occitanie)",
      "url": "cas.mon-ent-occitanie.fr",
      "py": "occitanie_montpellier_educonnect",
      "educonnect": true
    },
    {
      "name": "Académie de Rennes (Toutatice)",
      "url": "www.toutatice.fr",
      "py": "ac_rennes",
      "educonnect": true
    },
    {
      "name": "Académie de Toulouse (Mon ENT Occitanie)",
      "url": "cas.mon-ent-occitanie.fr",
      "py": "occitanie_toulouse"
    },
    {
      "name": "Académie de Toulouse (Mon ENT Occitanie) via ÉduConnect",
      "url": "cas.mon-ent-occitanie.fr",
      "py": "occitanie_toulouse_edu",
      "educonnect": true
    },
    {
      "name": "Académie d'Orléans-Tours (Net O'Centre)",
      "url": "ent.netocentre.fr",
      "py": "ac_orleans_tours",
      "educonnect": true
    },
    {
      "name": "Académie de Poitiers",
      "url": "sp-ts.ac-poitiers.fr",
      "py": "ac_poitiers",
      "educonnect": true
    },
    {
      "name": "Agora 06",
      "url": "cas.agora06.fr",
      "py": "cas_agora06",
      "educonnect": true
    },
    {
      "name": "Arsene76",
      "url": "cas.arsene76.fr",
      "py": "cas_arsene76"
    },
    {
      "name": "Arsene76 via ÉduConnect",
      "url": "cas.arsene76.fr",
      "py": "cas_arsene76_edu",
      "educonnect": true
    },
    {
      "name": "Atrium Sud",
      "url": "www.atrium-sud.fr",
      "py": "atrium_sud"
    },
    {
      "name": "CyberColleges42",
      "url": "cas.cybercolleges42.fr",
      "py": "cas_cybercolleges42"
    },
    {
      "name": "CyberColleges42 via ÉduConnect",
      "url": "cas.cybercolleges42.fr",
      "py": "cas_cybercolleges42_edu",
      "educonnect": true
    },
    {
      "name": "e-Co//ège 31",
      "url": "cas.ecollege.haute-garonne.fr",
      "py": "ecollege_haute_garonne"
    },
    {
      "name": "e-Co//ège 31 via ÉduConnect",
      "url": "cas.ecollege.haute-garonne.fr",
      "py": "ecollege_haute_garonne_edu",
      "educonnect": true
    },
    {
      "name": "e-Lyco",
      "url": "cas3.e-lyco.fr",
      "py": "ent_elyco",
      "educonnect": true
    },
    {
      "name": "ÉCLAT-BFC",
      "url": "cas.eclat-bfc.fr",
      "py": "eclat_bfc",
      "educonnect": true
    },
    {
      "name": "ÉduConnect sans ENT",
      "url": "hubeduconnect.index-education.net",
      "py": "prn_educonnect",
      "educonnect": true
    },
    {
      "name": "ENC Hauts-de-Seine",
      "url": "enc.hauts-de-seine.fr",
      "py": "enc_hauts_de_seine"
    },
    {
      "name": "ENT27",
      "url": "cas.ent27.fr",
      "py": "cas_ent27"
    },
    {
      "name": "ENT77",
      "url": "ent77.seine-et-marne.fr",
      "py": "ent77"
    },
    {
      "name": "ENT Hauts-de-France",
      "url": "connexion.enthdf.fr",
      "py": "ent_hdf",
      "educonnect": true
    },
    {
      "name": "ENT Mayotte",
      "url": "mayotte.opendigitaleducation.com",
      "py": "ent_mayotte"
    },
    {
      "name": "Extranet Collèges de la Somme",
      "url": "colleges.cg80.fr",
      "py": "extranet_colleges_somme"
    },
    {
      "name": "La Classe (Grand Lyon)",
      "url": "www.laclasse.com",
      "py": "laclasse_lyon"
    },
    {
      "name": "La Classe (Grand Lyon) via ÉduConnect",
      "url": "www.laclasse.com",
      "py": "laclasse_educonnect",
      "educonnect": true
    },
    {
      "name": "L'Éduc de Normandie via ÉduConnect",
      "url": "connexion.l-educdenormandie.fr",
      "py": "l_normandie",
      "educonnect": true
    },
    {
      "name": "Lycée Connecté",
      "url": "jeunes.nouvelle-aquitaine.fr",
      "py": "lyceeconnecte_aquitaine",
      "educonnect": false
    },
    {
      "name": "Lycée Connecté via ÉduConnect",
      "url": "jeunes.nouvelle-aquitaine.fr",
      "py": "lyceeconnecte_edu",
      "educonnect": true
    },
    {
      "name": "Ma Classe en Auvergne Rhône-Alpes via ÉduConnect",
      "url": "cas.ent.auvergnerhonealpes.fr",
      "py": "ent_auvergnerhonealpe",
      "educonnect": true
    },
    {
      "name": "Mon Bureau Numérique via ÉduConnect",
      "url": "cas.monbureaunumerique.fr",
      "py": "monbureaunumerique",
      "educonnect": true
    },
    {
      "name": "Mon Collège du Val d'Oise",
      "url": "cas.moncollege.valdoise.fr",
      "py": "val_doise"
    },
    {
      "name": "Mon Collège (Essonne)",
      "url": "www.moncollege-ent.essonne.fr",
      "py": "ent_essonne"
    },
    {
      "name": "MonLycée.net",
      "url": "ent.iledefrance.fr",
      "py": "ile_de_france"
    },
    {
      "name": "Néo Connect",
      "url": "neoconnect.opendigitaleducation.com",
      "py": "neoconnect_guadeloupe"
    },
    {
      "name": "OSÉ (Argos 2.0)",
      "url": "ds.ac-bordeaux.fr",
      "py": "ent2d_bordeaux"
    },
    {
      "name": "OZE Collège (Yvelines)",
      "url": "ozecollege.yvelines.fr",
      "py": "ozecollege_yvelines"
    },
    {
      "name": "Paris Classe Numérique",
      "url": "ent.parisclassenumerique.fr",
      "py": "paris_classe_numerique"
    },
    {
      "name": "Skolengo",
      "url": "cas.skolengo.com",
      "py": "cas_kosmos"
    },
    {
      "name": "Webcollège",
      "url": "cas.webcollege.seinesaintdenis.fr",
      "py": "cas_seinesaintdenis_edu",
      "educonnect": true
    }
]

"""
CAS_LIST = json.loads(cas_list_raw)

# ajouter les CORS sur toutes les routes
@hug.response_middleware()
def CORS(request, response, resource):
	response.set_header('Access-Control-Allow-Origin', '*')
	response.set_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
	response.set_header(
		'Access-Control-Allow-Headers',
		'Authorization,Keep-Alive,User-Agent,'
		'If-Modified-Since,Cache-Control,Content-Type'
	)
	response.set_header(
		'Access-Control-Expose-Headers',
		'Authorization,Keep-Alive,User-Agent,'
		'If-Modified-Since,Cache-Control,Content-Type'
	)
	if request.method == 'OPTIONS':
		response.set_header('Access-Control-Max-Age', 1728000)
		response.set_header('Content-Type', 'text/plain charset=UTF-8')
		response.set_header('Content-Length', 0)
		response.status_code = hug.HTTP_204

# système de tokens
saved_clients = {}
"""
saved_clients ->
	token ->
		client -> instance de pronotepy.Client
		last_interaction -> int (provenant de time.time(), entier représentant le temps depuis la dernière intéraction avec le client)
"""
client_timeout_threshold = 300 # le temps en sec avant qu'un jeton ne soit rendu invalide

def get_client(token: str) -> Tuple[str,  Union[pronotepy.Client, None]]:
	"""Retourne le client Pronote associé au jeton.

	Args:
		token (str): le jeton à partir duquel retrouver le client.
		instance (bool): si True, le client ne sera pas recherché sur les autres instances.

	Returns:
		tuple: le couple (statut, client?) associé au jeton
			str: le statut de la demande ('ok' si le client est trouvé, 'expired' si le jeton a expiré, 'notfound' si le jeton n'est pas associé à un client)
			 Union[pronotepy.Client, None]: une instance de client si le token est valide, None sinon.

	"""
	if token in saved_clients:
		client_dict = saved_clients[token]
		if time.time() - client_dict['last_interaction'] < client_timeout_threshold:
			client_dict['last_interaction'] = time.time()
			return 'ok', client_dict['client']
		else:
			del saved_clients[token]
			print(len(saved_clients), 'valid tokens')
			return 'expired', None
	else:
		return 'notfound', None

@hug.get('/infos')
def infos():
	return {
		'status': 'ok',
		'message': 'server is running',
		'server': socket.gethostname(),
		'version': API_VERSION,
		'ent_list': CAS_LIST
	}

# requête initiale :
# un client doit faire
# token = POST /generatetoken body={url, username, password, ent}
# GET * token=token
@hug.post('/generatetoken')
def generate_token(response, body=None, method: hug.types.one_of(['url', 'qrcode'])='url'):
	if not body is None:
		noENT = False

		if method == "url":
			for rk in ('url', 'username', 'password', 'ent'):
				if not rk in body and rk != 'ent':
					response.status = falcon.get_http_status(400)
					return {
						"token": False,
						"error": f'Missing {rk}'
					}
				elif not rk in body and rk == 'ent':
					noENT = True 

			try:
				if noENT:
					client = pronotepy.Client(body['url'], username=body['username'], password=body['password'])
				else:
					client = pronotepy.Client(body['url'], username=body['username'], password=body['password'], ent=getattr(pronotepy.ent, body['ent']))
			except Exception as e:
				response.status = falcon.get_http_status(498)
				print(f"Error while trying to connect to {body['url']}")
				print(e)

				error = {
					"token": False,
					"error": str(e),
				}
				return error

		elif method == "qrcode":
			for rk in ('url', 'qrToken', 'login', 'checkCode'):
				if not rk in body:
					response.status = falcon.get_http_status(400)
					return {
						"token": False,
						"error": f'Missing {rk}'
					}
				elif rk == "checkCode":
					if len(body["checkCode"]) != 4:
						response.status = falcon.get_http_status(400)
						return {
							"token": False,
							"error": f'checkCode must be 4 characters long (got {len(body["checkCode"])})'
						}

			try:
				client = pronotepy.Client.qrcode_login({
					"jeton": body['qrToken'],
					"login": body['login'],
					"url": body['url']
				}, body['checkCode'])
			except Exception as e:
				response.status = falcon.get_http_status(498)
				print(e)

				error = {
					"token": False,
					"error": str(e),
				}
				return error
		
		token = secrets.token_urlsafe(16)

		# Set current period
		client.calculated_period = __get_current_period(client)
		client.activated_period = __get_current_period(client, False, None, True)

		saved_clients[token] = {
			'client': client,
			'last_interaction': time.time()
		}

		print(len(saved_clients), 'valid tokens')

		# if error return error
		if client.logged_in:
			tokenArray = {
				"token": token,
				"error": False
			}
			return tokenArray
		else:
			response.status = falcon.get_http_status(498)
			error = {
				"token": False,
				"error": "Login failed",
			}
			return error
	else:
		response.status = falcon.get_http_status(400)
		error = {
			"token": False,
			"error": "missingbody",
		}
		return error


# TODO: METTRE A JOUR CETTE PARTIE SI DES PROBLEMES APPARAISSENT
# Peut poser problème avec certains établissements
def __get_current_period(client: pronotepy.Client, wantSpecificPeriod: bool = False, specificPeriod: str = None, wantAllPeriods: bool = False) -> pronotepy.Period:
	"""
	Permet de récupérer la période actuelle du client Pronote ou une période spécifique.
	
	Args:
		client (pronotepy.Client): Le client Pronote
		wantSpecificPeriod (bool, optional): Si True, la fonction va retourner la période spécifiée par specificPeriod. Si False, la fonction va retourner la période actuelle. Defaults to False.
		specificPeriod (str, optional): La période à retourner. Defaults to None.
		wantAllPeriods (bool, optional): Si True, la fonction va retourner toutes les périodes. Defaults to False.
		
	Returns:
		pronotepy.Period: La période actuelle ou la période spécifiée.
	"""
	
	if client.logged_in:
		if not wantSpecificPeriod:
			CURRENT_PERIOD_NAME = client.current_period.name.split(' ')[0]
			if CURRENT_PERIOD_NAME == 'Trimestre':
				CURRENT_PERIOD_NAME = 'Trimestre'
			elif CURRENT_PERIOD_NAME == 'Semestre':
				CURRENT_PERIOD_NAME = 'Semestre'
			elif CURRENT_PERIOD_NAME == 'Année':
				CURRENT_PERIOD_NAME = 'Année'
			else:
				print("WARN: Couldn't find current period name")
				return client.current_period
			
			if wantAllPeriods: allPeriods = []

			for period in client.periods:
				if period.name.split(' ')[0] == CURRENT_PERIOD_NAME:
					
					if not wantAllPeriods:   
						raw = datetime.datetime.now().date()
						now = datetime.datetime(raw.year, raw.month, raw.day)
						if period.start <= now <= period.end:
							return period
					else:
						allPeriods.append(period)
			
			return allPeriods
		else:
			for period in client.periods:
				if period.name == specificPeriod:
					return period
			print("WARN: Couldn't find specific period name")
			return __get_current_period(client, False, None)


@hug.post('/changePeriod')
def change_period(token: str, response, periodName: str):
	"""
	Permets de changer la période actuelle du client Pronote.
	
	Args:
		token (str): Le token du client Pronote
		response (falcon.Response): La réponse de la requête
		periodName (str): Le nom de la période à sélectionner
		
	Returns:
		dict[str, str]: Le statut de la requête et le nom de la période sélectionnée
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		if client.logged_in:
			try:
				client.calculated_period = __get_current_period(client, True, periodName)
				return {
					'status': 'ok',
					'period': client.calculated_period.name
				}
			except Exception as e:
				response.status = falcon.get_http_status(500)
				return {
					'status': 'error',
					'message': str(e)
				}
	else:
		response.status = falcon.get_http_status(498)
		return success


@hug.get('/user')
def user(token: str, response):
	"""
	Récupère les informations de l'utilisateur.
	
	Args:
		token (str): Le token du client Pronote
		response (falcon.Response): La réponse de la requête
		
	Returns:
		dict: Les informations de l'utilisateur sous la forme : 
		
		{ 
			"name": str,
			"class": str, 
			"establishment": str, 
			"phone": str,
			"address": list[str], 
			"email": str,
			"ine": str,
			"profile_picture": str|None, 
			"delegue": bool, 
			"periodes": list[dict] 
		}
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		if client.logged_in:
			periods = []
			for period in client.periods:
				periods.append({
					'start': period.start.strftime('%Y-%m-%d'),
					'end': period.end.strftime('%Y-%m-%d'),
					'name': period.name,
					'id': period.id,
					'actual': client.calculated_period.id == period.id
				})

			userData = {
				"name": client.info.name,
				"class": client.info.class_name,
				"establishment": client.info.establishment,
				"phone": client.info.phone,
				"email": client.info.email,
				"address": client.info.address,
				"ine": client.info.ine_number,
				"profile_picture": client.info.profile_picture.url if client.info.profile_picture else None,
				"delegue": client.info.delegue,
				"periods": periods
			}

			return userData
	else:
		response.status = falcon.get_http_status(498)
		return success


@hug.get('/timetable')
def timetable(token: str, dateString: str, response):
	"""
	Récupère l'emploi du temps de l'utilisateur.
	
	Args:
		token (str): Le token du client Pronote
		dateString (str): La date à récupérer sous la forme YYYY-MM-DD
		response (falcon.Response): La réponse de la requête
		
	Returns:
		list[dict]: Les informations de l'emploi du temps :
		
		[{
			"id": str,
			"num": int,
			"subject": {
				"id": str,
				"name": str,
				"groups": bool
			},
			"teachers": list[str],
			"rooms": list[str],
			"group_names": list[str]
			"start": str,
			"end": str,
			"duration": int
			"is_cancelled": bool,
			"is_outing": bool,
			"is_detention": bool,
			"is_exempted": bool,
			"is_test": bool,
		}]
	"""
	
	dateToGet = datetime.datetime.strptime(dateString, "%Y-%m-%d").date()
	success, client = get_client(token)

	if success == 'ok':
		if client.logged_in:
			lessons = client.lessons(dateToGet)

			lessonsData = []
			for lesson in lessons:
				lessonData = {
					"id": lesson.id,
					"num": lesson.num,
					"subject": {
						"id": lesson.subject.id if lesson.subject is not None else "0",
						"name": lesson.subject.name if lesson.subject is not None else "",
						"groups": lesson.subject.groups if lesson.subject is not None else False
					},
					"teachers": lesson.teacher_names,
					"rooms": lesson.classrooms,
					"group_names": lesson.group_names,
					"memo": lesson.memo,
					"virtual": lesson.virtual_classrooms,
					"start": lesson.start.strftime("%Y-%m-%d %H:%M"),
					"end": lesson.end.strftime("%Y-%m-%d %H:%M"),
					"background_color": lesson.background_color,
					"status": lesson.status,
					"is_cancelled": lesson.canceled,
					"is_outing": lesson.outing,
					"is_detention": lesson.detention,
					"is_exempted": lesson.exempted,
					"is_test": lesson.test,
				}
				lessonsData.append(lessonData)

			return lessonsData
	else:
		response.status = falcon.get_http_status(498)
		return success

@hug.get('/content')
def content(token: str, dateString: str, response):
	"""
	Récupère le contenu des cours.
	
	Args:
		token (str): Le token du client Pronote
		dateString (str): La date à récupérer sous la forme YYYY-MM-DD
		response (falcon.Response): La réponse de la requête
		
	Returns:
		list[dict]: Les contenus du cours 
	"""
	
	dateToGet = datetime.datetime.strptime(dateString, "%Y-%m-%d").date()
	success, client = get_client(token)

	if success == 'ok':
		if client.logged_in:
			content = client.lessons(dateToGet, dateToGet)

			contentData = []
			for lesson in content:
				if lesson.content != None:
					for contentElement in lesson.content:
						files = []
						for file in contentElement.files:
							files.append({
								"id": file.id,
								"name": file.name,
								"url": file.url,
								"type": file.type
							})
						
						contentList = {
							"title": contentElement.title,
							"description": contentElement.description,
							"category": contentElement.category,
							"files": files
						}

				contentData.append(contentList)

			return contentData
	else:
		response.status = falcon.get_http_status(498)
		return success

@hug.get('/homework')
def homework(token: str, dateFrom: str, dateTo: str, response):
	"""
	Récupère les devoirs de l'utilisateur.
	
	Args:
		token (str): Le token du client Pronote
		dateFrom (str): La date de début à récupérer sous la forme YYYY-MM-DD
		dateTo (str): La date de fin à récupérer sous la forme YYYY-MM-DD
		response (falcon.Response): La réponse de la requête
		
	Returns:
		list[dict]: Les informations des devoirs :

		{
			"id": str,
			"subject": {
				"id": str,
				"name": str,
				"groups": bool
			},
			"description": str,
			"background_color": str,
			"date": str,
			"files": list[dict {
				"id": str,
				"name": str,
				"url": str,
				"type": int
			}]
		}
	"""
	
	dateFrom = datetime.datetime.strptime(dateFrom, "%Y-%m-%d").date()
	dateTo = datetime.datetime.strptime(dateTo, "%Y-%m-%d").date()
	success, client = get_client(token)

	if success == 'ok':
		if client.logged_in:
			homeworks = client.homework(date_from=dateFrom, date_to=dateTo)

			homeworksData = []
			for homework in homeworks:
				files = []
				for file in homework.files:
					files.append({
						"id": file.id,
						"name": file.name,
						"url": file.url,
						"type": file.type
					})

				homeworkData = {
					"id": homework.id,
					"subject": {
						"id": homework.subject.id,
						"name": homework.subject.name,
						"groups": homework.subject.groups,
					},
					"description": homework.description,
					"background_color": homework.background_color,
					"done": homework.done,
					"date": homework.date.strftime("%Y-%m-%d %H:%M"),
					"files": files
				}
				homeworksData.append(homeworkData)

			return homeworksData
	else:
		response.status = falcon.get_http_status(498)
		return success


def __get_grade_state(grade_value:str, significant:bool = False) -> Union[int, str] :
	"""
	Récupère l'état d'une note sous forme d'int. (Non Rendu, Absent, etc.)
	
	Args:
		grade_value (str): La valeur de la note
		significant (bool): Si on souhaite récupérer l'état de la note ou la note elle-même. Si True on récupère l'état sous la forme d'un int :
			1 : Absent
			2 : Dispensé
			3 : Non Noté
			4 : Inapte
			5 : Non Rendu
			6 : Absent compte 0
			7 : Non Rendu compte 0
			8 : Félicitations
			Si False on récupère la note elle-même ou -1 si la note ne compte pas comme telle. Defaults to False.
		
	Returns:
		int|str: L'état de la note sous forme d'int ou la note elle-même (str) si significant est False.    
	"""
	
	grade_value = str(grade_value)

	if significant:
		grade_translate = [
			"Absent",
			"Dispense",
			"NonNote",
			"Inapte",
			"NonRendu",
			"AbsentZero",
			"NonRenduZero",
			"Felicitations"
		]
		try:
			int(grade_value[0])
			return 0
		except (ValueError, IndexError):
			if grade_value == "":
				return -1
			return grade_translate.index(grade_value) + 1
	else:
		try:
			int(grade_value[0])
			return grade_value
		except (ValueError, IndexError):
			return "-1"


def __transform_to_number(value:str)->  Union[float, int]:
	"""
	Transforme une valeur en nombre (int ou float)
	
	Args:
		value (str): La valeur à transformer
		
	Returns:
		float|int: La valeur transformée ('1,5' -> 1.5)
	"""
	
	try:
		return int(value)
	except ValueError:
		return float(value.replace(",", "."))


@hug.get('/grades')
def grades(token: str, response):
	"""
	Récupère les notes de l'utilisateur.
	
	Args:
		token (str): Le token du client Pronote
		response (falcon.Response): La réponse de la requête
		
	Returns:
		dict: Les informations des notes :
		
		{
			grades : [{
				"id": str,
				"subject": {
					"id": str,
					"name": str,
					"groups": bool
				},
				"date": str,
				"description": str,
				"is_bonus": bool,
				"is_optional": bool,
				"is_out_of_20": bool,
				"grade": {
					"value": int,
					"out_of": int,
					"coefficient": int,
					"average": int,
					"max": int,
					"min": int,
					"significant": int
				},
			}],
			"average": [{
				"subject": {
					"id": str,
					"name": str,
					"groups": bool
				},
				"average": int,
				"class_average": int,
				"max": int,
				"min": int,
				"out_of": int,
				"significant": int
			}],
			"overall_average": int,
			"class_overall_average": int,
		}
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		allGrades = client.calculated_period.grades
		gradesData = []
		for grade in allGrades:
			gradeData = {
				"id": grade.id,
				"subject": {
					"id": grade.subject.id,
					"name": grade.subject.name,
					"groups": grade.subject.groups,
				},
				"date": grade.date.strftime("%Y-%m-%d %H:%M"),
				"description": grade.comment,
				"is_bonus": grade.is_bonus,
				"is_optional": grade.is_optionnal,
				"is_out_of_20": grade.is_out_of_20,
				"grade": {
					"value": __transform_to_number(__get_grade_state(grade.grade)),
					"out_of": __transform_to_number(grade.out_of),
					"coefficient": __transform_to_number(grade.coefficient),
					"average": __transform_to_number(__get_grade_state(grade.average)),
					"max": __transform_to_number(__get_grade_state(grade.max)),
					"min": __transform_to_number(__get_grade_state(grade.min)),
					"significant": __get_grade_state(grade.grade, True),
				}
			}

			gradesData.append(gradeData)

		averagesData = []

		allAverages = client.calculated_period.averages
		for average in allAverages:
			averageData = {
				"subject": {
					"id": average.subject.id,
					"name": average.subject.name,
					"groups": average.subject.groups,
				},
				"average": __transform_to_number(__get_grade_state(average.student)),
				"class_average": __transform_to_number(__get_grade_state(average.class_average)),
				"max": __transform_to_number(__get_grade_state(average.max)),
				"min": __transform_to_number(__get_grade_state(average.min)),
				"out_of": __transform_to_number(__get_grade_state(average.out_of)),
				"significant": __get_grade_state(average.student, True),
				"color": average.background_color if average.background_color != None else "#08BE88"
			}

			averagesData.append(averageData)

		gradeReturn = {
			"grades": gradesData,
			"averages": averagesData,
			"overall_average": __transform_to_number(__get_grade_state(client.calculated_period.overall_average)),
			"class_overall_average": __transform_to_number(__get_grade_state(client.calculated_period.class_overall_average)),
		}

		return gradeReturn
	else:
		response.status = falcon.get_http_status(498)
		return success


@hug.get('/absences')
def absences(token: str, response, allPeriods: bool = True):
	"""
	Récupère les absences de l'utilisateur.
	
	Args:
		token (str): Le token du client Pronote
		response (falcon.Response): La réponse de la requête
		allPeriods (bool): Si toutes les périodes doivent être récupérées. Par défaut, toutes les périodes sont récupérées.
		
	Returns:
		list[dict]: Les informations des absences :
		
		[{
			"id": str,
			"from": str,
			"to": str,
			"justified": bool,
			"hours": int,
			"reasons": list[str],
		}]
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		if allPeriods:
			allAbsences = [absence for period in client.activated_period for absence in period.absences]
		else:
			allAbsences = client.calculated_period.absences

		absencesData = []
		for absence in allAbsences:
			absenceData = {
				"id": absence.id,
				"from": absence.from_date.strftime("%Y-%m-%d %H:%M"),
				"to": absence.to_date.strftime("%Y-%m-%d %H:%M"),
				"justified": absence.justified,
				"hours": absence.hours,
				"reasons": absence.reasons,
			}

			absencesData.append(absenceData)

		return absencesData
	else:
		response.status = falcon.get_http_status(498)
		return success


@hug.get('/delays')
def delays(token: str, response, allPeriods: bool = True):
	"""
	Récupère les retards de l'utilisateur.
	
	Args:
		token (str): Le token du client Pronote
		response (falcon.Response): La réponse de la requête
		allPeriods (bool): Si toutes les périodes doivent être récupérées. Par défaut, toutes les périodes sont récupérées.
		
	Returns:
		list[dict]: Les informations des retards :
		
		[{
			"id": str,
			"date": str,
			"duration": int,
			"justified": bool,
			"justification": str,
			"reasons": list[str]
		}]
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		if allPeriods:
			allDelays = [delay for period in client.activated_period for delay in period.delays]
		else:
			allDelays = client.calculated_period.delays
		
		delaysData = []
		for delay in allDelays:
			delayData = {
				"id": delay.id,
				"date": delay.date.strftime("%Y-%m-%d %H:%M"),
				"duration": delay.minutes,
				"justified": delay.justified,
				"justification": delay.justification,
				"reasons": delay.reasons,
			}

			delaysData.append(delayData)

		return delaysData
	else:
		response.status = falcon.get_http_status(498)
		return success


@hug.get('/punishments')
def punishments(token: str, response, allPeriods: bool = True):
	"""
	Récupère les punitions de l'utilisateur.
	
	Args:
		token (str): Le token du client Pronote
		response (falcon.Response): La réponse de la requête
		allPeriods (bool): Si toutes les périodes doivent être récupérées. Par défaut, toutes les périodes sont récupérées.
		
	Returns:
		list[dict]: Les informations des punitions :
		
		[{
			"id": str,
			"schedulable": bool,
			"schedule": [
				{
					"id": str,
					"start": str,
					"duration": int,
			],
			"date": str,
			"given_by": str,
			"exclusion:" bool,
			"during_lesson": bool,
			"homework": {
				"text": str,
				"documents": [{
					"id": str,
					"name": str,
					"url": str,
					"type": int,
				}],
			},
			"reasons": {
				"text": str,
				"circumstances": str,
				"documents": [{
					"id": str,
					"name": str,
					"url": str,
					"type": int,
				}],
			},
			"nature": str,
			"duration": int,
		}]
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		if allPeriods:
			allPunishments = [punishment for period in client.activated_period for punishment in period.punishments]
		else:
			allPunishments = client.calculated_period.punishments
		
		punishmentsData = []
		for punishment in allPunishments:
			homeworkDocs = []
			if punishment.homework_documents is not None:
				for homeworkDoc in punishment.homework_documents:
					homeworkDocs.append({
						"id": homeworkDoc.id,
						"name": homeworkDoc.name,
						"url": homeworkDoc.url,
						"type": homeworkDoc.type
					})

			circumstanceDocs = []
			if punishment.circumstance_documents is not None:
				for circumstanceDoc in punishment.circumstance_documents:
					circumstanceDocs.append({
						"id": circumstanceDoc.id,
						"name": circumstanceDoc.name,
						"url": circumstanceDoc.url,
						"type": circumstanceDoc.type
					})

			schedules = []
			if punishment.schedule is not None:
				for schedule in punishment.schedule:
					schedules.append({
						"id": schedule.id,
						"start": schedule.start.strftime("%Y-%m-%d %H:%M"),
						"duration": schedule.duration,
					})

			punishmentData = {
				"id": punishment.id,
				"schedulable": punishment.schedulable,
				"schedule": schedules,
				"date": punishment.given.strftime("%Y-%m-%d %H:%M"),
				"given_by": punishment.giver,
				"exclusion": punishment.exclusion,
				"during_lesson": punishment.during_lesson,
				"homework": {
					"text": punishment.homework,
					"documents": homeworkDocs,
				},
				"reason": {
					"text": punishment.reasons,
					"circumstances": punishment.circumstances,
					"documents": circumstanceDocs,
				},
				"nature": punishment.nature,
				"duration": punishment.duration
			}

			punishmentsData.append(punishmentData)

		return punishmentsData
	else:
		response.status = falcon.get_http_status(498)
		return success


@hug.get('/news')
def news(token: str, response):
	"""
	Récupère les actualités de l'utilisateur.
	
	Args:
		token (str): Le token du client Pronote
		response (falcon.Response): La réponse de la requête
		
	Returns:
		list[dict]: Les informations des actualités :
		
		[{
			"id": str,
			"title": str,
			"date": str,
			"category": str,
			"read": bool,
			"survey": bool,
			"anonymous_survey": bool,
			"author": str,
			"content": str,
			"attachments": [{
				"id": str,
				"name": str,
				"url": str,
				"type": int,
			}],
			"html_content": str,
		}]
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		allNews = client.information_and_surveys()

		newsAllData = []
		for news in allNews:
			attachments = []
			if news.attachments is not None:
				for attachment in news.attachments:
					attachments.append({
						"id": attachment.id,
						"name": attachment.name,
						"url": attachment.url,
						"type": attachment.type
					})

			newsData = {
				"id": news.id,
				"title": news.title,
				"date": news.creation_date.strftime("%Y-%m-%d %H:%M"),
				"category": news.category,
				"read": news.read,
				"survey": news.survey,
				"anonymous_survey": news.anonymous_response,
				"author": news.author,
				"content": news.content,
				"attachments": attachments,
				"html_content": news._raw_content
			}

			newsAllData.append(newsData)

		return newsAllData
	else:
		response.status = falcon.get_http_status(498)
		return success


@hug.get('/discussions')
def discussions(token: str, response):
	"""
	Récupère les discussions de l'utilisateur.
	
	Args:
		token (str): Le token du client Pronote
		response (falcon.Response): La réponse de la requête
		
	Returns:
		list[dict]: Les informations des discussions :
		
		[{
			"id": str,
			"subject": str,
			"creator": str,
			"participants": list[str],
			"date": str,
			"unread": int,
			"replyable": bool,
			"messages": [{
				"id": str,
				"content": str,
				"author": str,
				"date": str,
				"seen": bool,
			}],
		}]
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		allDiscussions = client.discussions()

		discussionsAllData = []
		for discussion in allDiscussions:
			messages = []
			for message in discussion.messages:
				messages.append({
					"id": message.id,
					"content": message.content,
					"author": message.author,
					"date": message.date.strftime("%Y-%m-%d %H:%M") if message.date is not None else None,
					"seen": message.seen
				})

			discussionData = {
				"id": discussion.id,
				"subject": discussion.subject,
				"creator": discussion.creator,
				"participants": discussion.participants,
				"date": discussion.date.strftime("%Y-%m-%d %H:%M") if discussion.date is not None else None,
				"unread": discussion.unread,
				"closed": discussion.close,
				"replyable": discussion.replyable,
				"messages": messages,
			}

			discussionsAllData.append(discussionData)

		return discussionsAllData
	else:
		response.status = falcon.get_http_status(498)
		return success


@hug.post('/discussion/delete')
def delete_discussion(token: str, discussionId: str, response):
	"""
	Supprime une discussion.
	
	Args:
		token (str): Le token du client Pronote
		discussionId (str): L'identifiant de la discussion
		response (falcon.Response): La réponse de la requête
		
	Returns:
		str: 'ok' si la discussion a été supprimée, 'not found' si la discussion n'a pas été trouvée, 'error' si une erreur est survenue.
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		try:
			allDiscussions = client.discussions()
			for discussion in allDiscussions:
				if discussion.id == discussionId:
					discussion.delete()
					return {
						"status": "ok",
						"error": None
					}
				else:
					response.status = falcon.get_http_status(404)
					return {
						"status": "not found",
						"error": "La discussion n'a pas été trouvée."
					}
		except Exception as e:
			response.status = falcon.get_http_status(500)
			return {
				"status": "error",
				"error": str(e)
			}
	else:
		response.status = falcon.get_http_status(498)
		return success

@hug.post('/discussion/readState')
def read_discussion(token: str, discussionId: str, response):
	"""
	Change l'état de lecture d'une discussion.
	
	Args:
		token (str): Le token du client Pronote
		discussionId (str): L'identifiant de la discussion
		response (falcon.Response): La réponse de la requête
		
	Returns:
		str: 'ok' si l'état de lecture a été changé, 'not found' si la discussion n'a pas été trouvée, 'error' si une erreur est survenue.
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		try:
			allDiscussions = client.discussions()
			for discussion in allDiscussions:
				if discussion.id == discussionId:
					if discussion.unread == 0: discussion.mark_as(False)
					else: discussion.mark_as(True)
					return {
						"status": "ok",
						"error": None
					}
				else:
					response.status = falcon.get_http_status(404)
					return {
						"status": "not found",
						"error": "La discussion n'a pas été trouvée."
					}
		except Exception as e:
			response.status = falcon.get_http_status(500)
			return {
				"status": "error",
				"error": str(e)
			}
	else:
		response.status = falcon.get_http_status(498)
		return success

@hug.post('/discussion/reply')
def reply_discussion(token: str, discussionId: str, content: str, response):
	"""
	Répond à une discussion.
	
	Args:
		token (str): Le token du client Pronote
		discussionId (str): L'identifiant de la discussion
		content (str): Le contenu du message
		response (falcon.Response): La réponse de la requête
		
	Returns:
		str: 'ok' si le message a été envoyé, 'not replyable' si la discussion n'est pas ouverte à la réponse, 'not found' si la discussion n'a pas été trouvée, 'error' si une erreur est survenue.
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		try:
			allDiscussions = client.discussions()
			for discussion in allDiscussions:
				if discussion.id == discussionId:
					if discussion.replyable:
						discussion.reply(content)
						return {
							"status": "ok",
							"error": None
						}
					else:
						response.status = falcon.get_http_status(403)
						return {
							"status": "not replyable",
							"error": "La discussion n'est pas ouverte à la réponse."
						}
				else:
					response.status = falcon.get_http_status(404)
					return {
						"status": "not found",
						"error": "La discussion n'a pas été trouvée."
					}
		except Exception as e:
			response.status = falcon.get_http_status(500)
			return {
				"status": "error",
				"error": str(e)
			}
	else:
		response.status = falcon.get_http_status(498)
		return success


@hug.get('/recipients')
def recipients(token: str, response):
	"""
	Récupère la liste des destinataires possibles.
	
	Args:
		token (str): Le token du client Pronote
		response (falcon.Response): La réponse de la requête
		
	Returns:
		list: La liste des destinataires possibles.
		
		[{
			"id": str,
			"name": str,
			"type": str,
			"email": str,
			"functions": list[str],
			"with_discussion": bool
		}]
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		allRecipients = client.get_recipients()

		recipientsAllData = []
		for recipient in allRecipients:
			recipientData = {
				"id": recipient.id,
				"name": recipient.name,
				"type": recipient.type,
				"email": recipient.email,
				"functions": recipient.functions,
				"with_discussion": recipient.with_discussion
			}

			recipientsAllData.append(recipientData)
		
		return recipientsAllData
	else:
		response.status = falcon.get_http_status(498)
		return success


@hug.post('/discussion/create')
def create_discussion(token: str, subject: str, content: str, recipientsId: str, response):
	"""
	Créer une discussion.
	
	Args:
		token (str): Le token du client Pronote
		subject (str): Le sujet de la discussion
		content (str): Le contenu du message
		recipientsId (str): La liste des identifiants des destinataires ([id1, id2, id3])
		response (falcon.Response): La réponse de la requête
		
	Returns:
		str: 'ok' si la discussion a été créée, 'error' si une erreur est survenue.
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		try:
			prn_recipients = []
			for recipient in json.loads(recipientsId):
				for prn_recipient in client.get_recipients():
					if prn_recipient.id == recipient:
						prn_recipients.append(prn_recipient)
						
			if len(prn_recipients) == 0:
				response.status = falcon.get_http_status(400)
				return {
					"status": "no recipient",
					"error": "Aucun destinataire valide n'a été trouvé."
				}
				
			for prn_recipient in prn_recipients:
				if prn_recipient.with_discussion == False:
					response.status = falcon.get_http_status(400)
					return {
						"status": "recipient not accept discussion",
						"error": "Un ou plusieurs destinataires n'acceptent pas les discussions."
					}
					
			client.new_discussion(subject, content, prn_recipients)
			return {
				"status": "ok",
				"error": None
			}
		except Exception as e:            
			response.status = falcon.get_http_status(500)
			return {
				"status": "error",
				"error": str(e)
			}
	else:
		response.status = falcon.get_http_status(498)
		return success


@hug.get('/evaluations')
def evaluations(token: str, response):
	"""
	Permet de récupérer les évaluations.
	
	Args:
		token (str): Le token du client Pronote
		response (falcon.Response): La réponse de la requête
		
	Returns:
		list[dict]: La liste des évaluations.
		
		[{
			"id": str,
			"subject": {
				"id": str,
				"name": str,
				"groups": bool
			},
			"name": str,
			"description": str,
			"teacher": str, 
			"date": str,
			"palier": str,
			"coefficient": str,
			"acquisitions": [{
				"id": str,
				"name": str,
				"coefficient": str,
				"abbreviation": str,
				"domain": str,
				"level": str
			}],
		}]
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		allEvaluations = client.calculated_period.evaluations

		evaluationsAllData = []
		for evaluation in allEvaluations:
			acquisitions = []
			if evaluation.acquisitions is not None:
				for acquisition in evaluation.acquisitions:
					acquisitions.append({
						"id": acquisition.id,
						"name": acquisition.name,
						"coefficient": acquisition.coefficient,
						"abbreviation": acquisition.abbreviation,
						"domain": acquisition.domain,
						"level": acquisition.level
					})

			evaluationData = {
				"id": evaluation.id,
				"subject": {
					"id": evaluation.subject.id,
					"name": evaluation.subject.name,
					"groups": evaluation.subject.groups,
				},
				"name": evaluation.name,
				"description": evaluation.description,
				"teacher": evaluation.teacher,
				"date": evaluation.date.strftime("%Y-%m-%d %H:%M"),
				"paliers": evaluation.paliers,
				"coefficient": evaluation.coefficient,
				"acquisitions": acquisitions,
			}

			evaluationsAllData.append(evaluationData)

		return evaluationsAllData
	else:
		response.status = falcon.get_http_status(498)
		return success

def __get_meal_food(meal: Optional[List[Dict]]) -> Optional[List[Dict]]:
	"""
	Permet de récupérer les aliments d'un repas.
	
	Args:
		meal (list): La liste des aliments du repas
		
	Returns:
		list[dict]: La liste des aliments du repas.
	"""
	
	if meal is None:
		return None
	else:
		foods = []
		for food in meal:
			foods.append({
				"name": food.name,
				"labels": __get_food_labels(food.labels),
			})
		return foods

def __get_food_labels(labels: Optional[List[Dict]]) -> Optional[List[Dict]]:

	"""
	Permet de récupérer les labels d'un aliment.
	
	Args:
		labels (list): La liste des labels de l'aliment
		
	Returns:
		list[dict]: La liste des labels de l'aliment.
	"""
	
	if labels is None:
		return None
	else:
		foodLabels = []
		for label in labels:
			foodLabels.append({
				"id": label.id,
				"name": label.name,
				"color": label.color,
			})
		return foodLabels

@hug.get('/menu')
def menu(token: str, dateFrom: str, dateTo: str, response):
	"""
	Permet de récupérer les menus.
	
	Args:
		token (str): Le token du client Pronote
		dateFrom (str): La date de début
		dateTo (str): La date de fin
		response (falcon.Response): La réponse de la requête
		
	Returns:
		list[dict]: La liste des menus.
		
		[{
			"id": str,
			"name": str,
			"date": str,
			"type": {
				"is_lunch": bool,
				"is_dinner": bool,
			},
			"first_meal": list[dict],
			"dessert": list[dict],
			"cheese": list[dict],
			"other_meal": list[dict],
			"side_meal": list[dict],
			"main_meal": list[dict],
		}]
	"""
	
	dateFrom = datetime.datetime.strptime(dateFrom, "%Y-%m-%d").date()
	dateTo = datetime.datetime.strptime(dateTo, "%Y-%m-%d").date()
	success, client = get_client(token)
	if success == 'ok':
		allMenus = client.menus(date_from=dateFrom, date_to=dateTo)

		menusAllData = []
		for menu in allMenus:
			cheese = __get_meal_food(menu.cheese)
			dessert = __get_meal_food(menu.dessert)
			other_meal = __get_meal_food(menu.other_meal)
			side_meal = __get_meal_food(menu.side_meal)
			main_meal = __get_meal_food(menu.main_meal)
			first_meal = __get_meal_food(menu.first_meal)

			menuData = {
				"id": menu.id,
				"name": menu.name,
				"date": menu.date.strftime("%Y-%m-%d"),
				"type": {
					"is_lunch": menu.is_lunch,
					"is_dinner": menu.is_dinner,
				},
				"first_meal": first_meal,
				"dessert": dessert,
				"cheese": cheese,
				"other_meal": other_meal,
				"side_meal": side_meal,
				"main_meal": main_meal,
			}

			menusAllData.append(menuData)

		return menusAllData
	else:
		response.status = falcon.get_http_status(498)
		return success

@hug.get('/export/ical')
def export_ical(token: str, response):
	"""
	Permet d'exporter les données de Pronote en iCal. (si l'instance de Pronote le permet)
	
	Args:
		token (str): Le token du client Pronote
		response (falcon.Response): La réponse de la requête
		
	Returns:
		str: L'URL de l'iCal.
	"""
	
	success, client = get_client(token)
	if success == 'ok':
		ical_url = client.export_ical()
		return ical_url
	else:
		response.status = falcon.get_http_status(498)
		return success


@hug.post('/homework/changeState')
def set_homework_as_done(token: str, dateFrom: str, dateTo: str, homeworkId: str, response):
	"""
	Change l'état d'un devoir. (fait ou non fait)
	
	Args:
		token (str): Le token du client Pronote
		dateFrom (str): La date de début
		dateTo (str): La date de fin
		homeworkId (str): L'ID du devoir
		response (falcon.Response): La réponse de la requête
		
	Returns:
		str: 'ok' si tout s'est bien passé, 'not found' si le devoir n'a pas été trouvé, 'error' si une erreur est survenue.
	"""
	
	dateFrom = datetime.datetime.strptime(dateFrom, "%Y-%m-%d").date()
	dateTo = datetime.datetime.strptime(dateTo, "%Y-%m-%d").date()
	success, client = get_client(token)

	if success == 'ok':
		if client.logged_in:
			try:
				homeworks = client.homework(date_from=dateFrom, date_to=dateTo)
				
				for homework in homeworks:
					changed = False
					if homework.id == homeworkId:
						if homework.done: homework.set_done(False)
						else: homework.set_done(True)
						changed = True
						return {
							"status": "ok",
							"error": None
						}
				if not changed:
					response.status = falcon.get_http_status(404)
					return {
						"status": "not found",
						"error": "Aucun devoir trouvé avec cet ID."
					}
			except Exception as e:
				response.status = falcon.get_http_status(500)
				return {
					"status": "error",
					"error": str(e)
				}
	else:
		response.status = falcon.get_http_status(498)
		return success

def main():
	server = hug.API(__name__)
	server.http.serve(port=8000)

if __name__ == '__main__':
	main()
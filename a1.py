#Name:Rohith Rajesh
#Roll number:2018182
#Section:A
#Group:6
from urllib.request import * 
def weather_response(location, API_key):
	'''function to give the json string for the weather of a  particular location.
	inputs: location, API key
	output: json string'''
	content = urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key)
	content= content.read()
	content=content.decode()
	p= content.find('\"main\"')
	q=content.find(':',p)
	content=content[q+1:]
	return(content)

 
def has_error(location,json):
	'''Function to check wheather the input location corresponds to the location returned by the json string
	inputs: location,json
	outputs:True if both locations don't match
			False if they match'''
	p=str(json).find("\"city\"")
	q=str(json).find('\"name\"',p)
	r=str(json).find(':',q)
	s=str(json).find(',',q)
	if (location==str(json)[r+2:s-1]):
		return  False
	else:		
		return True

from datetime import *
def get_temperature (json, n=0,t="03:00:00"):
	''' function which returns the temperature on the nth day at the given time from a json string corresponding to a particular
	location
	input: json, n={0,1,2,3,4}, t={"00:00:00","03:00:00","06:00:00","09:00:00","12:00:00","15:00:00","18:00:00","21:00:00"}
	output: temperature(Kelvin).
	 '''
	today= date.today()
	look_date= str(date.today()+ timedelta(days=n))
	date_time= (look_date + " " + t)
	p= str(json).find(date_time)
	t= str(json)[:p].rfind('\"temp\"')
	x= str(json).find(':',t)
	y= str(json).find(',',t)
	return float(str(json)[x+1:y])

def get_humidity(json, n=0,t="03:00:00"):
	'''function returns the humidity of a given location on the nth day at a given time.
	input: json, n={0,1,2,3,4}, t={"00:00:00","03:00:00","06:00:00","09:00:00","12:00:00","15:00:00","18:00:00","21:00:00"}
	output: humidity percent'''
	today= date.today()
	look_date= str(date.today()+ timedelta(days=n))
	date_time= (look_date + " " + t)
	p= str(json).find(date_time)
	t= str(json)[:p].rfind("\"humidity\"")
	x= str(json).find(':',t)
	y= str(json).find(',',t)
	return float((str(json)[x+1:y]))

def get_pressure(json, n=0,t="03:00:00"):
	'''function returns the pressure of a given location on the nth day at a given time.
	input: json, n={0,1,2,3,4},t={"00:00:00","03:00:00","06:00:00","09:00:00","12:00:00","15:00:00","18:00:00","21:00:00"}
	output: pressure(hectopascals)''' 
	today= date.today()
	look_date= str(date.today()+ timedelta(days=n))
	date_time= (look_date + " " + t)
	p= str(json).find(date_time)
	t= str(json)[:p].rfind("\"pressure\"")
	x= str(json).find(':',t)
	y= str(json).find(',',t)
	return float(str(json)[x+1:y])


def get_wind(json, n=0,t="03:00:00"):
	''' function returns the wind speed of a given location on the nth day at a given time.
	input: json, n={0,1,2,3,4},t={"00:00:00","03:00:00","06:00:00","09:00:00","12:00:00","15:00:00","18:00:00","21:00:00"}
	output: wind speed(m/s)'''
	today= date.today()
	look_date= str(date.today()+ timedelta(days=n))
	date_time= (look_date + " " + t)
	p= str(json).find(date_time) 
	q= str(json)[:p].rfind('\"wind\"')
	t=str(json).find('\"speed\"',q)
	x= str(json).find(':',t)
	y= str(json).find(',',t)
	return float(str(json)[x+1:y]) 


def get_sealevel(json, n=0, t="03:00:00" ):
	'''function returns the sea level of a given location on the nth day at a given time.
	input: json, n={0,1,2,3,4},t={"00:00:00","03:00:00","06:00:00","09:00:00","12:00:00","15:00:00","18:00:00","21:00:00"}
	output: atmospheric pressure at sea level(in hPa)  '''
	today= date.today()
	look_date= str(date.today()+ timedelta(days=n))
	date_time= (look_date + " " + t)
	p= str(json).find(date_time) 
	t= str(json)[:p].rfind('\"sea_level\"')
	x= str(json).find(':',t)
	y= str(json).find(',',t)
	return float(str(json)[x+1:y])
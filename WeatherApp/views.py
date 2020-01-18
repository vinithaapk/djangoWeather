from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode= request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&zipCode+" + zipcode + "&latitude=13.0029&longitude=80.2235&distance=25&API_KEY=C016847F-2C0E-4B02-8F49-94456D389821")
		#http://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude=13.0029&longitude=80.2235&distance=25&API_KEY=C016847F-2C0E-4B02-8F49-94456D389821
		try:
			api= json.loads(api_request.content)
		except Exception as e:
			api="Error"
		if api[0]['Category']['Name'] == "Good":
			category_desc="Air quality is considered satisfactory, and air pollution poses little or no risk."
			category_color="Good"
		elif api[0]['Category']['Name'] == "Moderate": 
			category_desc="Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution"
			category_color="Moderate"	
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitivite Groups":
			category_desc="Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."     	
			category_color="Unhealthy"	


		return render(request, 'home.html', {'api': api,
			'category_desc': category_desc,
			'category_color': category_color}) 

	else:

		api_request = requests.get("http://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&zipCode=600003&latitude=13.0029&longitude=80.2235&distance=25&API_KEY=C016847F-2C0E-4B02-8F49-94456D389821")
		#http://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude=13.0029&longitude=80.2235&distance=25&API_KEY=C016847F-2C0E-4B02-8F49-94456D389821
		try:
			api= json.loads(api_request.content)
		except Exception as e:
			api="Error"
		if api[0]['Category']['Name'] == "Good":
			category_desc="Air quality is considered satisfactory, and air pollution poses little or no risk."
			category_color="Good"
		elif api[0]['Category']['Name'] == "Moderate": 
			category_desc="Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution"
			category_color="Moderate"	
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitivite Groups":
			category_desc="Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."     	
			category_color="Unhealthy"	


		return render(request, 'home.html', {'api': api,
			'category_desc': category_desc,
			'category_color': category_color}) 


def about(request):
	return render(request, 'base.html', {}) 
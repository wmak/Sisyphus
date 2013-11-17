from config import parse_config
import urllib2
import json

class weather(object):
	zip_code = "http://api.wunderground.com/api/%s/geolookup/q/%s.json"

	def __init__():
		config = parse_config()
		self.api = config.get("Weather", "api_key")
		self.url = "http://api.wunderground.com/api/"
		self.forecast = []
		self.location = self.get_location()

	def update_weather():
		f = urllib2.urlopen('http://api.wunderground.com/api/749d42017bcd5650/geolookup/conditions/q/IA/Cedar_Rapids.json')
		json_string = f.read()
		parsed_json = json.loads(json_string)
		location = parsed_json['location']['city']
		temp_f = parsed_json['current_observation']['temp_f']

	def get_weather():
		pass

	def get_location():
		if hasattr(self, "location"):
			return self.location
		else:
			pass
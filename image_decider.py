from config import parse_config
import urllib2
import json

class weather(object):
	def __init__(self):
		config = parse_config()
		self.api = config.get("Weather", "api_key")
		self.zip = config.get("Weather", "zip_code")
		self.url = "http://api.wunderground.com/api/%s" %self.api
		self.forecast = []
		self.location = self.get_location()

	def weather(self):
		pass

	def update_forecast(self):
		url = self.url + "/hourly/q/%s.json" % self.location
		f = urllib2.urlopen(url)
		json_string = f.read()
		parsed_json = json.loads(json_string)
		for item in parsed_json["hourly_forecast"]:
			self.forecast.append((item["FCTTIME"]["hour"], item["condition"]))

	def get_location(self):
		if hasattr(self, "location"):
			return self.location
		else:
			url = self.url + "/geolookup/q/%s.json" % self.zip
			f = urllib2.urlopen(url)
			json_string = f.read()
			parsed_json = json.loads(json_string)
			self.location = parsed_json["location"]["wmo"]

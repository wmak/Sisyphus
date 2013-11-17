import ConfigParser

def parse_config():
	config = ConfigParser.ConfigParser()
	config.read("config.ini")
	return config
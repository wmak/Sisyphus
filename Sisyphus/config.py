import ConfigParser

def parse_config():
	config = ConfigParser.ConfigParser()
	config.read("../conf/config.ini")
	return config
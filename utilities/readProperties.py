import configparser

config = configparser.ConfigParser()
config.read("/Users/jigarjethwani/Documents/AutomationFramework/Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('BasicInfo', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('BasicInfo','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('BasicInfo','password')
        return password

    @staticmethod
    def getAPIEndPoint(section,key):
        endpoint = config.get(section, key)
        return endpoint

    @staticmethod
    def getBrowserName():
        browser = config.get('BasicInfo', 'browser')
        return browser
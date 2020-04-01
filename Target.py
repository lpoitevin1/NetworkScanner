from Colors import Colors
import socket
from ip2geotools.databases.noncommercial import DbIpCity


class Target: 
    def __init__(self):
        self.hostname = None
        self.ip = None
        self.country = None
        self.region = None
        self.city = None
        self.lat = None
        self.lng = None
        self.colors = Colors()    


    def getResumeTarget(self):
        self.colors.print_random_color('[INFO TARGET HOST]\r\n')
        resume = self.getDetailsTarget()
        if self.ip is not None :
            print('PUBLIC IP: '+str(self.ip))
        if resume[0] is not None :
            print('COUNTRY: '+resume[0])
        if resume[1] is not None :
            print('CITY: '+resume[1])
        if resume[2] is not None :
            print('REGION: '+resume[2])
        if resume[3] is not None :
            print('LATITUDE: '+str(resume[3]))
        if resume[4] is not None :
            print('LONGITUDE: '+str(resume[4]))
        print('\r\n')

    def getTargetIP(self):
        if self.ip is None :
            self.getDetailsTarget()
            return self.ip




    def getDetailsTarget(self):
        self.hostname = input('[*] Type your target (ip or hostname): ')
        print('\r\n')
        location =  DbIpCity.get(self.getIPFromHostname(), api_key='free')
        self.country = location.country
        self.city = location.city
        self.region = location.region
        self.lat = location.latitude
        self.lng = location.longitude
        return self.country,self.city,self.region,self.lat,self.lng
    
    def getIPFromHostname(self):
        if self.ip is None :
            self.ip = socket.gethostbyname(str(self.hostname))
            return self.ip
        return self.ip
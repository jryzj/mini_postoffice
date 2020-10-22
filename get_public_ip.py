##define function to get public ip


from urllib.request import urlopen
from json import load

def method_1(website):
    return urlopen(website).read().decode('utf-8')

def method_2(website):
    return load(urlopen(website))['ip']

def method_3(website):
    return load(urlopen(website))['origin']

def method_4(website):
    return load(urlopen(website))['ip']

class GetPublicIP:
    def __init__(self):
        self._website = [
            'http://ip.42.pl/raw',
            'http://jsonip.com',
            'http://httpbin.org/ip',
            'https://api.ipify.org/?format=json'
        ]
        
        self._methods = [
            method_1,
            method_2,
            method_3,
            method_4            
        ]
        
        self._count = 4
    
    def get_ip(self, method = 0, show_web = False):
        if method < self._count and method >= 0:
            ip = self._methods[method](self._website[method])
            if show_web:
                ip = '%s : %s ' %(self._website[method], ip)
            return ip
        else:
            print('method index out of range')
    
    def add_method(self, website, fn):
        self._website.append(website)
        self._methods.append(fn)
        self._count += 1
        
    def remove_method(self, index):
        if index < self._count and index >= 0:
            self._website.pop(index)
            self._methods.pop(index)
            self._count -= 1
        else:
            print('method index out of range')

    def get_count(self):
        return self._count
    
    def get_websites(self):
        return self._website

    
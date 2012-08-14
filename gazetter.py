from ConfigParser import ConfigParser

def search(searchstring, name):
    return SearchResult(name), True

def getGazetteers():
    config = ConfigParser()
    config.read('config.ini')
    return config.sections()

class SearchResult():
    """ Result from a gazetter search """
    def __init__(self, gazetteer):
        self._description = None
        self._x = None
        self._y = None
        self._zoom = None
        self._zoomunits = None
        self._gazetteer = gazetteer
        
    @property
    def gazetter(self):
        return self._gazetteer
    
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, value):
        self.__description = value
    
    @property        
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def zoom(self):
        return self.__zoom
    
    @zoom.setter
    def zoom(self, value):
        self.__zoom = value
    
    @property
    def zoomunits(self):
        return self.__zoomunits
    
    @zoomunits.setter
    def set_zoomunits(self, value):
        self.__zoomunits = value

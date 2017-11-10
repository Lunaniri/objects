class Vehicle(object):
    def __init__(self,brand,model,km,service):
        self.brand=brand
        self.model=model
        self.km=km
        self.service=service
    def __str__(self):
        return self.brand+" "+self.model+"("+str(self.km)+"km)"+self.service
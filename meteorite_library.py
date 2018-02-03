# Authors : Jonathan McGuire, Adam Olsen, Sivasankari Ponnusamy, Kana Yamane 
#
# Library for meteorites
#

# Meteorite class
class meteor:
    meteorCount=0
    def __init__(self,id,nametype,recclass,fall,year, reclat,reclong):
        self.id=id
        self.nametype=nametype
        self.recclass=recclass
        self.fall=fall
        self.year=year
        self.reclat=reclat
        self.reclong=reclong
        meteor.meteorCount+=1
        
    def displayCount(self):
        print("Total meteorites: ", meteor.meteorCount)
            
    def getnametype(self):
        return self.nametype
        
    def setnametype(self,val):
        self.nametype=val

    def getid(self):
        return self.id
        
    def setid(self,val):
        self.id=val
            
    def getrecclass(self):
        return self.recclass
        
    def setrecclass(self,val):
        self.recclass=val

    def getfall(self):
        return self.fall
        
    def setfall(self,val):
        self.fall=val
            
    def getyear(self):
        return self.year
        
    def setyear(self,val):
        self.year=val

    def getreclat(self):
        return self.reclat
        
    def setreclat(self,val):
        self.reclat=val

    def getreclong(self):
        return self.reclong
        
    def setreclong(self,val):
        self.reclong=val  

# Subclass for meteorite fall
class meteorfall(meteor):
    def __init__(self, id, nametype, recclass, fall, year, reclat, reclong, isfell, isfound):
        meteor.__init__(self, id, nametype, recclass, fall, year, reclat, reclong)
        self.isfell = isfell
        self.isfound = isfound
    
def Isfell(self):
    if(self.fall == True):
        print('The meteorite was seen falling')
    else:
        print('The meteorite was discovered')
        
def Isfound(self):
    if(isfound == True):
        print('The meteorite was discovered')
    else:
        print('The meteorite was seen falling')
         

# Subclass for meteorite type
class meteortype(meteor):
    def __init__(self, id, nametype, recclass, fall, year, reclat, reclong, isvalid, isrelict):
        meteor.__init__(self, id, nametype, recclass, fall, year, reclat, reclong)
        self.isvalid = isvalid
        self.isrelict = isrelict
    
    def Isvalid(self):
        if(self.nametype == True):
            print('The meteorite’s type is valid')
        else: 
            print('The meteorite’s type is relict')
            
    def Isrelict(self):
        if(self.nametype == True):
            print('The meteorite’s type is relict')
        else:
            print('The meteorite’s type is valid')

    def printvals():
        print("Id: ",id)








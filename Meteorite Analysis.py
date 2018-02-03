# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:47:45 2017

# Authors : Jonathan McGuire, Adam Olsen, Sivasankari Ponnusamy, Kana Yamane
#
# Main program
#

"""

#import required libraries
import pandas               as pd
import matplotlib.pyplot    as plt
import numpy                as np
import mpl_toolkits.basemap as bm

#import custom library
import meteorite_library

#import statistics module
import statistics


#Using Pandas to read the meteorite landings data CSV file
data = pd.read_csv("Meteorite_Landings.csv")
price=pd.read_csv("Meteorite Prices.csv")

#Clean up the imported data
data = data[(data.reclat != 0.0) | (data.reclong != 0.0)]
data = data[(data.reclat <= 90) & (data.reclat >= -90)]
data = data[(data.reclong <= 180) & (data.reclong >= -180)]
data = data[(data.year >= 860) & (data.year <= 2013)]
data = data[(data.mass <= 60000000) & (data.mass >= 0)]
#drop unnecessary columns- name, id, geolocation
#data.drop(['name', 'id', 'GeoLocation'], axis=1, inplace=True)

#display columns
data.info()

Fell = data.groupby('fall').get_group('Fell')
Found = data.groupby('fall').get_group('Found')

#meteorite price table merge
#price per gram, given class
#get rid of everything past , / - ( .
data['recclass']= data['recclass'].apply(lambda x: pd.Series(str(x).split(',')))
data['recclass']= data['recclass'].apply(lambda x: pd.Series(str(x).split('/')))
data['recclass']= data['recclass'].apply(lambda x: pd.Series(str(x).split('-')))
data['recclass']= data['recclass'].apply(lambda x: pd.Series(str(x).split('(')))
data['recclass']= data['recclass'].apply(lambda x: pd.Series(str(x).split('.')))
data['recclass']= data['recclass'].apply(lambda x: pd.Series(str(x).split('~')))
data['recclass']= data['recclass'].apply(lambda x: pd.Series(str(x).split(' ')))
#get rid of digits
data['recclass'] = data['recclass'].str.replace('\d+', '')
data['recclass'] = data['recclass'].str.replace('?', '')
data=pd.merge(data,price, on=['recclass'])
#create new value column
data['Value']=data['price']*data['mass']
#drop price per gram
data.drop(['price'], axis=1, inplace=True)

def temporal_view(data):
    # Plot for Temporal view of landings made per year
    
    print("Temporal View Method Called")
    plt.plot()
    data.year.hist(bins=np.arange(1900,2014,1),figsize=(9,8))
    plt.title('Number of Meteorites per year 1900-2013')
    plt.xlim(1900,2014)
    plt.savefig("Temporal Discoveries.png")
    plt.show()
    plt.tight_layout()
    plt.show()

def geolocation():
    #create map of reclong(longitude), reclat(latitude)
    plt.figure(figsize=(15,8))
    long = []
    lat = []
    for i in data['reclong'][1:31929]: long.append(i)
    for i in data['reclat'][1:31929]: lat.append(i)
    map = bm.Basemap(projection='gall', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
    map.drawcoastlines()
    map.drawcountries()
    map.drawstates()
    map.bluemarble()
    meridians = np.arange(-180., 181., 60.)
    map.drawmeridians(meridians, color='LightBlue', labels=[True,False,False,True])
    parallels = np.arange(-90., 91., 30.)
    map.drawparallels(parallels, color='LightBlue', labels=[True,True,True,True])
    x,y = map(long, lat)
    map.plot(x, y, 'yo', markersize=3)
    plt.title("Map of Geographic Location of Meteorite Landings")
    plt.savefig("Geographic Location of Meteorite Landings")
    plt.show() 

def location():
    #Location of all the Fell Vs Found Meteorites
    plt.figure(figsize=(15,8))
    map = bm.Basemap(projection='cyl',llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
    map.drawcoastlines()
    map.drawcountries()
    map.drawstates()
    map.drawmapboundary(fill_color='w')
    meridians = np.arange(-180., 181., 60.)
    map.drawmeridians(meridians, color='LightBlue', labels=[True,False,False,True])
    parallels = np.arange(-90., 91., 30.)
    map.drawparallels(parallels, color='LightBlue', labels=[True,True,True,True])
    map.scatter(Fell.reclong,Fell.reclat,alpha=1,color='g')
    map.scatter(Found.reclong,Found.reclat,alpha=1,color='b')
    plt.title('Location of all Fell and Found Meteorites',fontsize=15)
    plt.legend("Fell","Found")
    plt.show()

#Plot for finding the Found meteorites
def displayFoundMeteorite(data):
    plt.subplot(221)
    Found.year.hist(bins=np.arange(1900,2014,1),figsize=(9,8),color='green')
    plt.title('Meteorites found per year 1900-2013- FOUND Category',fontsize=15)
    plt.xlim(1900,2014)
    plt.savefig("Found Meteorites.png")
    plt.show()
displayFoundMeteorite(data)


#Plot for finding the Found meteorites
def displayFoundMeteorite123(data): 
    plt.subplot(222)
    Found.year.hist(bins=np.arange(1900,2014,1),figsize=(9,8),color='green')
    plt.title('Meteorites found per year 1900-2013- FOUND Category',fontsize=15)
    plt.xlim(1900,2014)
    plt.savefig("Found Meteorites.png")
    plt.show()


#Plot for finding the Fell meteorites
def displayFellMeteorite(data):
    plt.subplot(223)
    Fell.year.hist(bins=np.arange(1900,2014,1),figsize=(9,8),color='blue')
    plt.title('Meteorites found per year 1900-2013 - FELL Category',fontsize=15)
    plt.xlim(1900,2014)
    plt.savefig("Fell Discoveries.png")
    plt.show()


def display_masslocation(data):
    #Plot the location of meteorites with their mass  
    plt.figure(figsize=(15,8))
    map = bm.Basemap(projection='cyl',llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')
    map.drawcoastlines()
    map.drawcountries()
    map.drawstates()
    map.drawmapboundary(fill_color='w')
    meridians = np.arange(-180., 181., 60.)
    map.drawmeridians(meridians, color='LightBlue', labels=[True,False,False,True])
    parallels = np.arange(-90., 91., 30.)
    map.drawparallels(parallels, color='LightBlue', labels=[True,True,True,True])
    map.scatter(Fell.reclong,Fell.reclat,alpha=1,color='g')
    map.scatter(data.reclong,data.reclat,s=np.sqrt(data.mass/150),alpha=1,color='g')
    plt.title('Location of all meteorites with their mass')
    plt.show()

def heaviest(data):
    # Heaviest Meterorite found till now
    Highest =0
    Highest = max(data.mass)
    print(Highest)
    plt.figure(figsize=(15,8))
    map = bm.Basemap()
    map.drawmapboundary(fill_color='lightblue')
    map.fillcontinents(color='white',lake_color=None)
    #Adding text to point
    idx = data[data['mass']==Highest].index.values.astype(int)[0]
    ptName= data['name'][idx]
    ptClass= data['recclass'][idx]
    ptYear= data['year'][idx]
    ptGeo= data['GeoLocation'][idx]
    ptLat = data['reclat'][idx]
    ptLong = data['reclong'][idx]
    anText = "Name: %s \n Year: %s \n Class: %s \n Geo: %s" % (ptName, ptYear, ptClass, ptGeo)
    map.drawcoastlines()
    map.plot(ptLat, ptLong, marker='D',color='m')
    x2 = ptLat+60
    y2 = ptLong+60
    plt.annotate(anText, xy=(ptLat, ptLong), xycoords='data', xytext=(x2, y2), textcoords='offset points',
                    color='r', arrowprops=dict(arrowstyle="fancy", color='g'),bbox=dict(boxstyle="round", facecolor="w",
                   alpha=0.9))
    plt.title("Location  of the Heaviest Meteorite ")
    plt.show()


def top_twenty_mass(data):
    t= 0
    # Top 20 Heaviest Meterorites
    plt.figure(figsize=(25,12))
    print("\n Count by Name")
    r=data[['mass','name']].sort_values(by='mass',ascending=False)
    t=r.head(20).plot.bar()
    plt.title("The Top Heaviest Meterorites Landing till now")
    plt.xlabel("Name of the Meteorites")
    plt.ylabel("Mass in gms")
    plt.show()



def display_heatmap(data):
    
    plt.figure(figsize=(15,8))
    h = plt.hist2d(data.reclong,data.reclat,bins=(np.arange(-180,180,3),np.arange(-90,91,3)))
    X,Y = np.meshgrid(h[1][:-1]+2.0,h[2][:-1]+2.0) 
   
    #setting map visualization attributes
    map = bm.Basemap(projection='cyl')
    map.drawcoastlines()
    map.drawcountries()
    map.drawstates()
    map.drawmapboundary(fill_color='w')
    map.drawmeridians(np.arange(0, 360, 20),linewidth=0.1)
    map.drawparallels(np.arange(-90., 91., 30.), color='LightBlue', labels=[False,False,False,False])
    
    #map dat and the coordinates
    dataForMap, xCord, yCord = map.transform_scalar(np.log10(h[0].T+0.2), X[0], Y[:,0], 360, 360, returnxy=True)
    map.contourf(xCord, yCord, dataForMap, cmap='OrRd')
    map.colorbar()

    plt.title('Denisty/ Mass of all Meteorite Landings Throughout the World')
    plt.show()


def display_pricemap(data):
    
    plt.figure(figsize=(15,8))

   
    #setting map visualization attributes
    map = bm.Basemap(projection='cyl')
    map.drawcoastlines()
    map.drawcountries()
    map.drawstates()
    map.drawmapboundary(fill_color='w')
    map.drawmeridians(np.arange(0, 360, 20),linewidth=0.1)
    map.drawparallels(np.arange(-90., 91., 30.), color='LightBlue', labels=[False,False,False,False])
    
    #map dat and the coordinates
    plt.hexbin(data.reclong,data.reclat,C=None,bins=None)
    plt.scatter(data.reclong,data.reclat,s=data.Value/100000,alpha=1, cmap='RdBu',c=data.Value)

    plt.title('Value of Meteorites ($100,000s)')
    map.colorbar()
    plt.show()

#Run Methods
temporal_view(data)
geolocation()
location()
displayFoundMeteorite123(data)
displayFellMeteorite(data)
display_masslocation(data)
heaviest(data)
top_twenty_mass(data)
display_heatmap(data)
display_pricemap(data)


# Create algorithms (possibly multiclass linear regression, clustering, calculate average mass of meteorites, )

print("The average mass of the meteorites is", format(statistics.mean(data.mass), '.2f'), "grams")



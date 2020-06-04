import datetime
import os
import wget
import sys
from subprocess import call
ee.Initialize()
ulx = 76
uly = 9
lrx = 77
lry = 10
month = 11
for x in range(2012, 2014):
	startyear=x
	endyear=x+1
	regionname = 'alappuzha'
	bands= ['B2', 'B3', 'B4', 'B5']
	output=regionname+'_'+str(endyear)+'_'+str(month)
	os.chdir('/home')
	region=[ulx,lry], [ulx, uly], [lrx, uly], [lrx, lry]  
	strregion=str(list(region))
	"""vis = {
	    'min': 0,
	    'max': 1,
	    'palette': [
		'FFFFFF', 'CE7E45', 'FCD163',
		'99B718', '74A901', '66A000', '529400', '3E8601',
		'207401', '056201', '004C00', '023B01', '012E01',
		'011D01', '011301'
	    ]}"""
	
	def getle8(img): 
		#return(img.normalizedDifference(['B5', 'B4']))>
		return img.expression('(b("B5") - b("B4")) / (b("B5") + b("B4"))>.1')
	unzippedfilename=output+".le7.tif"
	if(os.path.exists(unzippedfilename)):
	    sys.exit("File exists:"+output)
	le8 = ee.ImageCollection("LC8_L1T_TOA").filterDate(datetime.datetime(startyear, 11, 1),
		                  datetime.datetime(endyear, 11, 1));  
	le8new=le8.mean().select([0], ['le1']).multiply(ee.Image(1000)).int16();

	print(output+' Processing....      Coords:'+strregion)
	path =le8new.getDownloadUrl({
		'name': output,  
		'scale': 500,                             
		'crs': 'EPSG:4326',                        
		'region': strregion                        
		});
	print("Downloading "+output) 
	wget.download(path)
	zipstatus=call("unzip "+output+".zip",shell=True)    
	if(zipstatus==9):
	    sys.exit("File exists:"+output)    
	os.remove(output+".zip")    
	print(output+' Finished!')

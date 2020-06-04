from osgeo import gdal
import numpy as np
import struct
from osgeo import ogr
from osgeo import osr
from osgeo import gdal_array
from osgeo.gdalconst import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
t = np.float32
ds = gdal.Open(L8)
red = ds.GetRasterBand(1)
nir = ds.GetRasterBand(2)
red_L8 = red.ReadAsArray(0,0,ds.RasterXSize,ds.RasterYSize)
nir_L8 = nir.ReadAsArray(0,0,ds.RasterXSize,ds.RasterYSize)

red1 = red_L8.astype(np.float64)
nir1 = nir_L8.astype(np.float64)
e = red1 + nir1
d = red1 - nir1
np.any(e==0)
ndvi = d / e
print (ndvi)
plt.imshow(ndvi, cmap='RdYlGn') 
  
plt.colorbar()	
plt.show()

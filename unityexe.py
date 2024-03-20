#!/usr/bin/env python
# coding: utf-8

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import numpy as np
import math
import os
import shapely
import shapely.vectorized

def main():
    # nishi = gpd.read_file('./area_extracted/______220526.shp')
    chiba = gpd.read_file('C:/Users/chiba/OneDrive/kimitsu/Model/gis/area.shp') # Absolute path only
    table = pd.read_csv('C:/Users/chiba/OneDrive/kimitsu/Model/scripts/unity.csv',encoding='shift-jis')
    chiba = chiba.merge(table,on='SHOZAI')
    # Polygons mode
    for i in range(1,61):
        polygon = chiba[['field_1', 'Density{}'.format(i), 'Age{}'.format(i), 'geometry']]
    #     exec("polygon.iloc[:,0] = np.ceil(polygon['Age{}']/5)".format(i))
    #     exec("polygon.iloc[:,0] = 'forest_'+polygon['Age{}'].astype(int).astype(str)".format(i))
    #     polygon.insert(0,'id',polygon.index+1)
    #     exec("polygon = polygon.rename(columns={{'Age{}':'natural'}})".format(i))
        polygon = polygon.rename(columns={'field_1':'ID','Density{}'.format(i):'Density1','Age{}'.format(i):'Age1'})
        polygon = polygon.to_crs('epsg:4326')
        dname = 'C:/Users/chiba/OneDrive/kimitsu/Model/scripts/polygons/polygon{}'.format(i)
        if not os.path.exists(dname):
            os.makedirs(dname)
        polygon.to_file('{}/polygons.shp'.format(dname))
        unity = 'C:/Users/chiba/Unity/Chiba/Assets/TestData/Resources/GIS Terrains/Chiba_Year{}/Chiba_Year{}_VectorData/Polygons'.format(i,i)
        polygon.to_file('{}/polygons.shp'.format(unity))

if __name__ == '__main__':
    main()
"""
Developer: Harrison Hughes, Truman State University 2024

Creates a dictionary of all Violette Hall location entryways, and path intersections. Each location is represented
by a string key and a list of tuples that correspond to the entry/exit coordinates of that specific classroom
on the SVG file. Every other dictionary entry corresponds to a specific node on the comprehensive building path network, 
either as a door or intersection amongst paths. This file is to be called by AStar.py to serve as the 
data with which to operate on when either the source or destination object is specified as Violette Hall.
"""

nodes = {}
#Entrances
nodes[(708,703)] = ['l -2,0', 'l14,0']
nodes[(756.5,643.5)] = ['l 0,-12.32', 'l0,15.5']
nodes[(805,703)] = ['l 22.5,0', 'l-14,0']
nodes[(756.5,762.5)] = ['l0,8', 'l0,-31.5']

#Classrooms
nodes["VH1000"] = [(756.5,691)]
nodes[(756.5,691)] = ['l-3.91,-5']
nodes["VH1010"] = [(744,715.5), (769.75,709.75)]
nodes[(744,715.5)] = ['l0,-1']
nodes[(769.75,709.75)] = ['l3.25,0', 'l3.25,-3.25']

nodes["VH1436"] = [(722,710)]
nodes[(722,710)] = ['l0,-7']
nodes["VH1432"] = [(736.5,726),(726.5,726)]
nodes[(736.5,726)] = ['l0,3.25']
nodes[(726.5,726)] = ['l0,3.25']
nodes["VH1430"] = [(724,726)]
nodes[(724,726)] = ['l1.25,3.25']
nodes["VH1428"] = [(723,736)]
nodes[(723,736)] = ['l2.25,0']
nodes["VH1424"] = [(723,745)]
nodes[(723,745)] = ['l2.25,0']
nodes["VH1420"] = [(722,749.5)]
nodes[(722,749.5)] = ['l3.25,-3.25']
nodes["VH1416"] = [(726.5,748.5)]
nodes[(726.5,748.5)] = ['l0,-2.25']
nodes["VH1412"] = [(734.5,748.5)]
nodes[(734.5,748.5)] = ['l0,-2.25']
nodes["VH1408"] = [(745.5,747.5)]
nodes[(745.5,747.5)] = ['l-4,-1.25']
nodes["VH1404"] = [(745.5,745)]
nodes[(745.5,745)] = ['l-4,0']
nodes["VH1400"] = [(729.5,733.5),(738.5,742)]
nodes[(729.5,733.5)] = ['l0,-4.25', 'l-3,-4.25']
nodes[(738.5,742)] = ['l3,0', 'l3,4.25']

nodes["VH1332"] = [(767.5,745)]
nodes[(767.5,745)] = ['l4.5,0']
nodes["VH1328"] = [(767.5,747.5)]
nodes[(767.5,747.5)] = ['l4.5,-1.25']
nodes["VH1324"] = [(772,748.5)]
nodes[(772,748.5)] = ['l0,-2.25']
nodes["VH1320"] = [(792,749.5)]
nodes[(792,749.5)] = ['l-3.25,-3.25']
nodes["VH1316"] = [(793,741)]
nodes[(793,741)] = ['l-4.25,0']
nodes["VH1314"] = [(793,738.5)]
nodes[(793,738.5)] = ['l-4.25,0']
nodes["VH1312"] = [(793,724)]
nodes[(793,724)] = ['l-3.25,0']
nodes["VH1310"] = [(793,721.5)]
nodes[(793,721.5)] = ['l-3.25,0']
nodes["VH1308"] = [(793,707.5)]
nodes[(793,707.5)] = ['l-3.25,0']
nodes["VH1304"] = [(776.5,726),(786.5,726)]
nodes[(776.5,726)] = ['l0,3.25']
nodes[(786.5,726)] = ['l0,3.25']
nodes["VH1300"] = [(775.5,742), (784.5,733.5)]
nodes[(775.5,742)] = ['l-3.5,0', 'l-3.5,4.25']
nodes[(784.5,733.5)] = ['l4.25,-4.25','l0,-4.25']

nodes["VH1236"] = [(791,695)]
nodes[(791,695)] = ['l0,8']
nodes["VH1232"] = [(776.5,678.5),(787.5,678.5)]
nodes[(776.5,678.5)] = ['l0,-2.75']
nodes[(787.5,678.5)] = ['l0,-2.75']
nodes["VH1228"] = [(790,672)]
nodes[(790,672)] = ['l-2.25,0']
nodes["VH1224"] = [(790,661)]
nodes[(790,661)] = ['l-2.25,0']
nodes["VH1220"] = [(791,656.5)]
nodes[(791,656.5)] = ['l-3.25,3']
nodes["VH1216"] = [(786.5,657.5)]
nodes[(786.5,657.5)] = ['l0,2']
nodes["VH1212"] = [(780.5,657.5)]
nodes[(780.5,657.5)] = ['l0,2']
nodes["VH1208"] = [(768.5,657.5)]
nodes[(768.5,657.5)] = ['l2.75,1.5']
nodes["VH1204"] = [(767,659)]
nodes[(767,659)] = ['l4.25,0']
nodes["VH1200"] = [(783.5,672), (774.5,663.5)]
nodes[(783.5,672)] = ['l0,3.75', 'l4.25,3.75']
nodes[(774.5,663.5)] = ['l-3.25,-4', 'l-3.25,0']

nodes["VH1148"] = [(750,657.5)]
nodes[(750,657.5)] = ['l0,1.5']
nodes["VH1146"] = [(734.5,657.5)]
nodes[(734.5,657.5)] = ['l0,1.5']
nodes["VH1144"] = [(728.5,658.5)]
nodes[(728.5,658.5)] = ['l1.5,0.5']
nodes["VH1142"] = [(726.25,660.75)]
nodes[(726.25,660.75)] = ['l3.75,3']
nodes["VH1140"] = [(725,663.75)]
nodes[(725,663.75)] = ['l5,0']

#Paths
#West/1400 Wing
nodes[(722,703)] = ['l-14,0', 'l18.25,0', 'l0,7']
nodes[(740.25,703)] = ['l-18.25,0', 'l0,4.5', 'l0,-17']
nodes[(740.25,707.5)] = ['l0,-4.5', 'l3.75,7', 'l0,7']
nodes[(744,714.5)] = ['l-3.75,0', 'l-3.75,-7', 'l0,1']
nodes[(740.25,714.5)] = ['l3.75,0', 'l0,-7', 'l0,8']
nodes[(740.25,722.5)] = ['l8.25,8.5', 'l0,-8', 'l0,6.75']
nodes[(740.25,729.25)] = ['l0,-6.75', 'l-3.75,0', 'l1.25,1.75']
nodes[(736.5,729.25)] = ['l3.75,0', 'l0,-3.25', 'l-7,0']
nodes[(729.5,729.25)] = ['l7,0', 'l0,4.25', 'l-3,0']
nodes[(726.5,729.25)] = ['l0,-3.25', 'l3,0', 'l-1.25,0', 'l3,4.25']
nodes[(725.25,729.25)] = ['l1.25,0', 'l0,6.75', 'l-1.25,-3.25']
nodes[(725.25,736)] = ['l-2.25,0', 'l0,-6.75', 'l0,9']
nodes[(725.25,745)] = ['l-2.25,0', 'l0,-9', 'l0,1.25']
nodes[(725.25,746.25)] = ['l0,-1.25', 'l-3.25,3.25', 'l1.25,0']
nodes[(726.5,746.25)] = ['l-1.25,0', 'l0,2.25', 'l8,0']
nodes[(734.5,746.25)] = ['l0,2.25', 'l-8,0', 'l7,0']
nodes[(741.5,746.25)] = ['l-7,0', 'l4,1.25', 'l0,-1.25', 'l-3,-4.25']
nodes[(741.5,745)] = ['l4,0', 'l0,1.25', 'l0,-3']
nodes[(741.5,742)] = ['l-3,0', 'l0,3', 'l0,-11']
nodes[(741.5,731)] = ['l7,0', 'l0,11', 'l-1.25,-1.75']
nodes[(748.5,731)] = ['l-7,0', 'l8,0', 'l-8.25,-8.5']

#South/1300 Wing
nodes[(756.5,731)] = ['l0,31.5', 'l-8,0', 'l8.5,0']
nodes[(765,731)] = ['l-8.5,0', 'l8,-8', 'l7,0']
nodes[(772,731)] = ['l-7,0', 'l0,11', 'l1,-1.75']
nodes[(772,742)] = ['l3.5,0', 'l0,-11', 'l0,3']
nodes[(772,745)] = ['l-4.5,0', 'l0,-3', 'l0,1.25']
nodes[(772,746.25)] = ['l0,-1.25', 'l-4.5,1.25', 'l0,2.25', 'l16.75,0', 'l3.5,-4.25']
nodes[(788.75,746.25)] = ['l-16.75,0', 'l0,-5.25','l3.25,3.25']
nodes[(788.75,741)] = ['l4.25,0', 'l0,5.25', 'l0,-2.5']
nodes[(788.75,738.5)] = ['l4.25,0', 'l0,2.5', 'l0,-9.25']
nodes[(788.75,729.25)] = ['l0,9.25', 'l-2.25,0', 'l1,0', 'l-4.25,4.25']
nodes[(789.75,729.25)] = ['l-1,0', 'l0,-5.25']
nodes[(789.75,724)] = ['l3.25,0', 'l0,5.25', 'l0,-2.5']
nodes[(789.75,721.5)] = ['l3.25,0','l0,2.5', 'l0,-14']
nodes[(789.75,707.5)] = ['l3.25,0','l0,14', 'l0,-4.5']
nodes[(786.5,729.25)] = ['l0,-3.25', 'l2.25,0', 'l-2,0']
nodes[(784.5,729.25)] = ['l0,4.25', 'l2,0', 'l-8,0']
nodes[(776.5,729.25)] = ['l0-3.25', 'l8,0', 'l-3.5,0']
nodes[(773,729.25)] = ['l3.5,0', 'l-1,1.75', 'l0,-6.25']
nodes[(773,723)] = ['l-8,8', 'l0,6.25', 'l0,-13.25']

#West/1200 Wing
nodes[(773,709.75)] = ['l-3.25,0', 'l0,13.25','l0,-3.25']
nodes[(773,706.5)] = ['l-3.25,3.25', 'l0,3.25', 'l0,-3.5']
nodes[(773,703)] = ['l16.75,0', 'l0,3.5', 'l0,-19.5']
nodes[(773,683.5)] = ['l0,-7.75', 'l-9.75,-9.75', 'l0,19.5']
nodes[(789.75,703)] = ['l1.25,0', 'l0,4.5', 'l-16.75,0']
nodes[(791,703)] = ['l14,0', 'l0,-8', 'l-1.25,0']
nodes[(773,675.75)] = ['l0,7.75', 'l3.5,0', 'l-1.75,-2']
nodes[(776.5,675.75)] = ['l0,2.75', 'l-3.5,0', 'l7,0']
nodes[(783.5,675.75)] = ['l-7,0', 'l0,-3.75', 'l4,0']
nodes[(787.5,675.75)] = ['l0,2.75', 'l-4,0', 'l.25,0']
nodes[(787.75,675.75)] = ['l-.25,0', 'l0,-3.75', 'l-4.25,-3.75']
nodes[(787.75,672)] = ['l0,3.75', 'l2.25,0', 'l0,-11']
nodes[(787.75,661)] = ['l2.25,0', 'l0,11', 'l0,-1.5']
nodes[(787.75,659.5)] = ['l0,1.5', 'l3.25,-3', 'l-1.25,0']
nodes[(786.5,659.5)] = ['l0,-2', 'l1.25,0', 'l-6,0']
nodes[(780.5,659.5)] = ['l0,-2', 'l-9.25,0', 'l6,0']
nodes[(771.25,659.5)] = ['l9.25,0', 'l0,4', 'l3.25,4', 'l0,-0.5']
nodes[(771.25,659)] = ['l-4.25,0', 'l0,0.5', 'l-2.75,-1.5']
nodes[(771.25,663.5)] = ['l3.25,0', 'l0,-4', 'l0,10.25']
nodes[(771.25,673.75)] = ['l1.75,2', 'l0,-10.25', 'l-8,0']
nodes[(763.25,673.75)] = ['l9.75,9.75', 'l-6.75,0', 'l8,0']

#North/1100 Wing
nodes[(756.5,659)] = ['l0,-15.5', 'l0,5', 'l-6.5,0', 'l-16.25,14.75']
nodes[(756.5,664)] = ['l0,-5', 'l0,9.75']
nodes[(756.5,673.75)] = ['l6.75,0', 'l0,-9.75', 'l-3.91,0']
nodes[(750,659)] = ['l0,-1.5', 'l6.5,0', 'l-15.5,0']
nodes[(734.5,659)] = ['l0,-1.5','l15.5,0', 'l-4.5,0']
nodes[(730,659)] = ['l0,4.75', 'l4.5,0', 'l-1.5,-0.5']
nodes[(740.25,673.75)] = ['l12.34,0', 'l0,12.25', 'l-10.25,-10', 'l12.34,12.25', 'l16.25,-14.75']
nodes[(730,663.75)] = ['l10.25,10', 'l-3.75,-3', 'l0,-4.75', 'l-5,0']
nodes[(752.59,686)] = ['l0,-12.25', 'l-12.34,0', 'l-12.34,-12.25', 'l3.91,5']
nodes[(752.59,673.75)] = ['l0,12.25', 'l-12.34,12.25', 'l3.91,0', 'l-12.34,0']
nodes[(740.25,686)] = ['l12.34,0', 'l12.34,-12.25', 'l0,-12.25', 'l0,17']
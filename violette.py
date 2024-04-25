import drawsvg as draw
import svgpathtools as pathTools
import AStar

d = draw.Drawing(120,140)
    
buildings = []
#violette
buildings.append([10,10, '''M0,0 L16,0 L16,1 L39,1 L39,0 L58,0 L58,1 L81,1 L81,0 L97,0 L97,15 L95,15
L95,49 L97,49 L97,70 L95,70 L95,104 L97,104 L97,119 L81,119 L81,118 L58,118 L58,119 L39,119 L39,118
L16,118 L16,119 L0,119 L0,104 L2,104 L2,70 L0,70 L0,49 L2,49 L2,15 L0,15 L0,0 L15,0'''])

classroom = []
#1400
classroom.append([22.5,89, '''M0,0 L5,0 L9,4 L9,8.5 L6,11.5 L1,11.5 L-3,7.5 L-3,3 L0,0 L5,0'''])
#1404
classroom.append([35.5,92.5, '''M0,0 L1,0 L1,-2 L10,-2 L10,10 L2,10 L2,8 L0,8 L0,0 L1,0'''])
#1408
classroom.append([35.5,105, '''M0,0 L2,0 L2,-2 L4.5,-2 L4.5,0 L11.5,0 L11.5,13 L4.5,13 L4.5,12 L0,12 L0,0 L2,0'''])
#1412
classroom.append([25.5,105, '''M0,0 L9.5,0 L9.5,12 L0,12 L0,0 L9.5,0'''])
#1416
classroom.append([15.5,107, '''M0,0 L2,-2 L9.5,-2 L9.5,10 L0,10 L0,0 L2,-2'''])
#1420
classroom.append([1,105, '''M0,0 L12,0 L14,2 L14,13 L0,13 L0,0 L12,0'''])
#1424
classroom.append([3,94, '''M0,0 L12,0 L12,8.5 L10,10.5 L0,10.5 L0,0 L12,0'''])
#1428
classroom.append([3,83, '''M0,0 L12,0 L12,10.5 L0,10.5 L0,0 L12,0'''])
#1430
classroom.append([3,74, '''M0,0 L12,0 L12,6.5 L14,6.5 L14,8.5 L0,8.5 L0,0 L12,0'''])
#1432
classroom.append([15.5,64.5, '''M0,0 L14,0 L14,18 L2,18 L2,15.5 L0,15.5 L0,0 L14,0'''])
#1436
classroom.append([3,64.5, '''M0,0 L10,0 L10,2 L12,2 L12,9 L0,9 L0,4.5 L-2,4.5 L-2,0 L10,0''']) 

#1300
classroom.append([70.5,89, '''M0,0 L5,0 L8,3 L8,7.5 L4,11.5 L-1,11.5 L-4,8.5 L-4,4 L0,0 L5,0'''])
#1304
classroom.append([67.5,64, '''M0,0 L13,0 L13,18.5 L0,18.5 L0,0 L13,0'''])
#1308
classroom.append([85,63, '''M0,0 L11,0 L11,6 L9,6 L9,8 L-2,8 L-2,2 L0,2 L0,0 L9,0'''])
#1310
classroom.append([83,71.5, '''M0,0 L11,0 L11,7.5 L2,7.5 L2,5.5 L0,5.5 L0,0 L11,0'''])
#1312
classroom.append([85,79.5, '''M0,0 L9,0 L9,8.5 L-2,8.5 L-2,2 L0,2 L0,0 L9,0'''])
#1314
classroom.append([83,88.5, '''M0,0 L11,0 L11,7.5 L2,7.5 L2,5.5 L0,5.5 L0,0 L11,0'''])
#1316
classroom.append([85,96.5, '''M0,0 L9,0 L9,8 L0,8 L-2,6 L-2,2 L0,2 L0,0 L9,0'''])
#1320
classroom.append([85,105, '''M0,0 L11,0 L11,13 L-2,13 L-2,2 L0,0 L11,0'''])
#1324
classroom.append([62,105, '''M0,0 L18.5,0 L20.5,2 L20.5,12 L0,12 L0,0 L17.5,0'''])
#1328
classroom.append([50,105, '''M0,0 L7,0 L7,-2 L9.5,-2 L9.5,0 L11.5,0 L11.5,12, L7,12 L7,13 L0,13 L0,0 L7,0'''])
#1332
classroom.append([51.5,90.5, '''M0,0 L9,0 L9,2 L10,2 L10,10, L8,10 L8,12 L0,12 L0,0 L9,0'''])

#1236
classroom.append([82,39.5, '''M0,0 L12,0 L12,10.5 L14,10.5 L14,15.5 L2,15.5 L2,12 L-2,12 L-2,10 L0,10 L0,0 L12,0'''])
#1232
classroom.append([67.5,35, '''M0,0 L14,0 L14,14 L12,14 L12,19 L0,19 L0,0 L14,0'''])
#1228
classroom.append([82,27.5, '''M0,0 L12,0 L12,11.5 L0,11.5 L0,0 L12,0'''])
#1224
classroom.append([84,14.5, '''M0,0 L10,0 L10,12.5 L-2,12.5 L-2,2 L0,0 L10,0'''])
#1220
classroom.append([82,1, '''M0,0 L14,0 L14,13 L2,13 L0,11 L0,0 L14,0'''])
#1216
classroom.append([74,2, '''M0,0 L7.5,0 L7.5,10 L5.5,12 L0,12 L0,0 L7.5,0'''])
#1212
classroom.append([62,2, '''M0,0 L11.5,0 L11.5,12 L0,12 L0,0 L11.5,0'''])
#1208
classroom.append([52,2, '''M0,-1 L5,-1 5,0 L9.5,0 L9.5,12 L0,12 L0,-1'''])
#1204
classroom.append([52,14.5, '''M0,0 L7,0 L7,2 L9,2 L9,11 L7.5,11 L7.5,13.5 L0,13.5 L0,0 L7,0'''])
#1200
classroom.append([68.5,18, '''M0,0 L5,0 L9,4 L9,8.5 L6,11.5 L1,11.5 L-3,7.5 L-3,3 L0,0 L5,0'''])

#Testing Room
classroom.append([3,14.5, '''M0,0 L10,0 L14,4 L14,7 L0,7 L0,0 L10,0'''])
#1142
classroom.append([1,1, '''M0,0 L14,0 L14,11.25 L18.25,15.25 L16.25,17.25 L12.25,13 L0,13 L0,0 L14,0'''])
#1144
classroom.append([15.5,2, '''M0,0 L9.5,0 L9.5,12 L6,12 L4,14 L0,10 L0,0 L9.5,0'''])
#1146
classroom.append([25.5,2, '''M0,0 L9.5,0 L9.5,12 L0,12 L0,0 L9.5,0'''])
#1148
classroom.append([35.5,2, '''M0,0 L4.5,0 L4.5,-1 L9.5,-1 L9.5,10 L7.5,10 L7.5,12 L0,12 L0,0 L4.5,0'''])

#1000
classroom.append([35,50, '''M0,0 L5,-2.5 L22,-2.5 L27,0 L27,13.5 L23,17.5 L20,17.5 L19.5,19 L7.5,19 L7,17.5 L4,17.5 L0,13.5 L0,0 L5,-2.5'''])
#1010
classroom.append([35,72, '''M0,0 L6.5,0 L6.5,-2 L25.5,-2 L25.5,-4 L24.5,-5 L26,-6.5 L27.5,-5, L27.5,0 Q27.5,8,18.5,12.5 L9,12.5 Q0,8,0,0 L6.5,0'''])
#Stairs
classroom.append([48,36.5, '''M0,0 A10,10,360,0,1,10,10 L14,10 A14,14,360,0,0,0,-4'''])

#Extra
classroom.append([25,17, '''M0,0 L15,0 L15,3.5 L11.5,3.5 L12.5,6 L5,8 L0,3 L0,0 L15,0'''])
classroom.append([19,23.5, '''M0,0 L0,15 L3.5,15 L3.5,11 L6,12.5 L8,5 L3,0 L0,0 L0,15'''])
classroom.append([3,22, '''M0,0 L15.5,0 L15.5,16.5 L13,16.5 L13,20 L20,20 L20,29 L10.5,29 L10.5,31.5 L-2,31.5 L-2,28 L0,28 L0,0 L12,0'''])
classroom.append([40.5,47.5, '''M0,0 L9,-11'''])

for i in range(len(buildings)):
    position = 'translate(' + str(buildings[i][0]) + ',' + str(buildings[i][1]) + ')'
    path = draw.Path(d=buildings[i][2], fill='grey', stroke='black', stroke_width='.5', transform=position)
    d.append(path)

d.set_pixel_scale(3.588)  # Set number of pixels per geometry unit
d.save_png('violette.png')
d.save_svg('violette.svg')


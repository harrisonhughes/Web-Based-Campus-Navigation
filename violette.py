import drawsvg as draw
import svgpathtools as pathTools
import AStar

d = draw.Drawing(100,120)
    
buildings = []
#violette
buildings.append([0,0, '''M0,0 L16,0 L16,1 L39,1 L39,0 L58,0 L58,1 L81,1 L81,0 L97,0 L97,15 L95,15
L95,49 L97,49 L97,70 L95,70 L95,104 L97,104 L97,119 L81,119 L81,118 L58,118 L58,119 L39,119 L39,118
L16,118 L16,119 L0,119 L0,104 L2,104 L2,70 L0,70 L0,49 L2,49 L2,15 L0,15 L0,0 L15,0'''])

classroom = []
#1420
classroom.append([1,105, '''M0,0 L12,0 L14,2 L14,13 L0,13 L0,0 L12,0'''])
#1424
classroom.append([3,94, '''M0,0 L12,0 L12,8.5 L10,10.5 L0,10.5 L0,0 L12,0'''])
#1428
classroom.append([3,83, '''M0,0 L12,0 L12,10.5 L0,10.5 L0,0 L12,0'''])
#1432
classroom.append([3,74, '''M0,0 L12,0 L12,6.5 L14,6.5 L14,8.5 L0,8.5 L0,0 L12,0'''])

#1236
classroom.append([82,39.5, '''M0,0 L12,0 L12,14 L10,14 L10,15.5 L2,15.5 L2,12 L-2,12 L-2,10 L0,10 L0,0 L12,0'''])
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
classroom.append([52,2, '''M2,2 L2,0 L9.5,0 L9.5,12 L0,12 L0,2 L2,2 L2,0'''])
#1204
classroom.append([52,16, '''M0,0 L7,0 L7,2 L9,2 L9,10 L7.5,10 L7.5,12 L0,12 L0,0 L7,0'''])
#1200
classroom.append([68.5,18, '''M0,0 L5,0 L9,4 L9,8.5 L6,11.5 L1,11.5 L-3,7.5 L-3,3 L0,0 L5,0'''])

#1110
classroom.append([14,42, '''M0,0 L6,0 L6,1 L9,1 L9,9 L0,9 L0,0 L6,0'''])
#Testing Room
classroom.append([3,14.5, '''M0,0 L10,0 L14,3.5 L14,7 L0,7 L0,0 L10,0'''])
#1142
classroom.append([1,1, '''M0,0 L14,0 L14,11 L12,13 L0,13 L0,0 L14,0'''])
#1144
classroom.append([15.5,2, '''M0,0 L9.5,0 L9.5,12 L5.5,12 L4,14 L0,10 L0,0 L9.5,0'''])
#1146
classroom.append([25.5,2, '''M0,0 L9.5,0 L9.5,12 L0,12 L0,0 L9.5,0'''])
#1148
classroom.append([35.5,2, '''M0,0 L8.5,0 L8.5,1.5 L9.5,1.5 L9.5,10 L7.5,10 L7.5,12 L0,12 L0,0 L8.5,0'''])

#1000
classroom.append([34.5,50, '''M0,0 L5,-2.5 L22,-2.5 L27,0 L27,13.5 L23,17.5 L20,17.5 L19.5,19 L7.5,19 L7,17.5 L4,17.5 L0,13.5 L0,0 L5,-2.5'''])
#1010
classroom.append([34.5,72, '''M0,0 L6.5,0 L6.5,-2 L25.5,-2 L25.5,-4 L24.5,-5 L26,-6.5 L27.5,-5, L27.5,0 Q27.5,8,18.5,12.5 L9,12.5 Q0,8,0,0 L6.5,0'''])
#Stairs
classroom.append([48,36.5, '''M0,0 A10.5,10.5,360,0,1,10.5,10.5 L14.5,10.5 A14.5,14.5,360,0,0,0,-4'''])

#Extra
classroom.append([25,17, '''M0,0 L15,0 L15,3.5 L11.5,3.5 L12.5,6 L5,8 L0,3 L0,0 L15,0'''])
classroom.append([19,23.5, '''M0,0 L0,15 L3.5,15 L3.5,11 L6,12.5 L8,5 L3,0 L0,0 L0,15'''])
classroom.append([3,22, '''M0,0 L12,0 L12,7 L15.5,7 L15.5,15.5 L13,15.5 L13,19.5 L10.5,19.5 L10.5,31.5 L0,31.5 L0,0 L12,0'''])
classroom.append([40.5,47.5, '''M0,0 L9,-11'''])

for i in range(len(classroom)):
    position = 'translate(' + str(classroom[i][0]) + ',' + str(classroom[i][1]) + ')'
    path = draw.Path(d=classroom[i][2], fill='none', stroke='blue', stroke_width='.25', transform=position)
    d.append(path)

for i in range(len(buildings)):
    position = 'translate(' + str(buildings[i][0]) + ',' + str(buildings[i][1]) + ')'
    path = draw.Path(d=buildings[i][2], fill='none', stroke='blue', stroke_width='.5', transform=position)
    d.append(path)

d.set_pixel_scale(3.588)  # Set number of pixels per geometry unit
d.save_png('violette.png')
d.save_svg('violette.svg')


import drawsvg as draw
import svgpathtools as pathTools
import AStar

d = draw.Drawing(1093,1117)
s = draw.Rectangle(0, 0, 1093, 1117, fill='#EEEEEE')
d.append(s)

filePath = "paths.txt"
paths = []

fileLot = "lots.txt"
lots = []

fileBlock = "blocks.txt"
blocks = []

fileBuild = "buildings.txt"
buildings = []

with open(fileBlock, "r") as file:
    for line in file:
        if not line.startswith("#"):
            block = line.strip().split("/")
            blocks.append(block)
            
for block in blocks:  
    newBlock = draw.Path(d=block[2], fill='white', stroke='black', stroke_width='.3', transform="translate(" + block[0] + "," + block[1] + ")")
    d.append(newBlock)

with open(filePath, "r") as file:
    for line in file:
        if not line.startswith("#"):
            path = line.strip().split("/")
            paths.append(path)
            
for path in paths:  
    newPath = draw.Path(d=path[3], fill='none', stroke='black', stroke_width=float(path[0]) + .3, transform="translate(" + path[1] + "," + path[2] + ")")
    d.append(newPath)
    newPath = draw.Path(d=path[3], fill='none', stroke='white', stroke_width=path[0], transform="translate(" + path[1] + "," + path[2] + ")")
    d.append(newPath)
    
with open(fileLot, "r") as file:
    for line in file:
        if not line.startswith("#"):
            lot = line.strip().split("/")
            lots.append(lot)
            
for lot in lots:  
    newLot = draw.Path(d=lot[3], fill='white', stroke='black', stroke_width=.3, transform="translate(" + lot[1] + "," + lot[2] + ")")
    d.append(newLot)

with open(fileBuild, "r") as file:
    for line in file:
        if not line.startswith("#"):
            build = line.strip().split("/")
            buildings.append(build)
            
for building in buildings:  
    newBuild = draw.Path(d=building[4], fill='#BBBBBB', stroke='black', stroke_width=.3, transform="translate(" + building[2] + "," + building[3] + ")")
    d.append(newBuild)

nodes = {}
for key in nodes:
    for i in nodes[key]:
        path = draw.Path(d='M0,0' + i, stroke='navy', stroke_width=2, fill='none', transform='translate' + str(key))
        d.append(path)

for key in nodes:
    d.append(draw.Circle(0, 0, 2, fill='red', stroke='none', transform='translate' + str(key)))



d.set_pixel_scale(1.512)  # Set number of pixels per geometry unit
#d.set_render_size(400, 200)  # Alternative to set_pixel_scale
d.save_svg('example.svg')
d.save_png('example.png')

# Display in Jupyter notebook
#d.rasterize()  # Display as PNG
d  # Display as SVG

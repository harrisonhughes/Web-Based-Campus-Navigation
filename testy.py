import drawsvg as draw
import svgpathtools as pathTools
import AStar

d = draw.Drawing(645,610)
s = draw.Rectangle(8.5, 8, 650, 576, fill='#EEEEEE')
d.append(s)

paths = []
paths.append([6, 'translate(3,0)', 'M0,0 L0,588 L0,0'])
paths.append([4, 'translate(0,578)', 'M0,0 L208,8.5 L341.5,17 L517,21 L650,22 L517,21'])
paths.append([4, 'translate(638,0)', 'M0,0 L0,448.5 L0,0'])
#Normal
paths.append([6, 'translate(275,25)', 'M0,0 L0,-33 L0,0'])
#ResLots
paths.append([5, 'translate(522,25)', 'M0,0 L0,431.98 L0,0'])
paths.append([30, 'translate(512,186.5)', 'M0,0 L12,0 L0,0'])
paths.append([4, 'translate(491,170)', 'M0,0 L31,0 L0,0'])
paths.append([4, 'translate(491,203)', 'M0,0 L31,0 L0,0'])
paths.append([5, 'translate(517,456.88)', 'M0,0 L0,142.12 L0,0'])
paths.append([4, 'translate(500,492)', 'M0,0 L8,0 L0,0'])
paths.append([4, 'translate(508,492)', 'M0,0 L9,10 L0,0'])
paths.append([4, 'translate(508,492)', 'M0,0 L9,-10 L0,0'])
paths.append([4, 'translate(500,524)', 'M0,0 L17,-8 L0,0'])
paths.append([4, 'translate(502,524)', 'M0,0 L0,4 L0,0'])
paths.append([4, 'translate(500,528)', 'M0,0 L17,8 L0,0'])
paths.append([4, 'translate(517,536)', 'M0,0 L12.5,0 L0,0'])
paths.append([4, 'translate(517,551)', 'M0,0 L12.5,-15 L0,0'])
paths.append([4, 'translate(517,468)', 'M0,0 L15.5,15 L0,0'])
paths.append([4, 'translate(517,504)', 'M0,0 L12.5,-12 L0,0'])
paths.append([4, 'translate(517,480)', 'M0,0 L12.5,12 L0,0'])
paths.append([4, 'translate(517,562)', 'M0,0 L15,-18 L0,0'])
paths.append([4, 'translate(500,571)', 'M0,0 L8,0 L0,0'])
paths.append([4, 'translate(508,571)', 'M0,0 L9,9 L0,0'])
paths.append([4, 'translate(508,571)', 'M0,0 L9,-9 L0,0'])
paths.append([4, 'translate(565,454.5)', 'M0,0 Q0,-6,7,-6 L108,-3 Q0,-6,7,-6'])
#Union/Lib/Mcclain
paths.append([6, 'translate(115,145)', 'M0,0 L0,170 L0,0'])
paths.append([5, 'translate(3,186.5)', 'M0,0 L132,0 L0,0'])
paths.append([5, 'translate(57,119)', 'M0,0 L0,100 L0,0'])
paths.append([5, 'translate(57,141)', 'M0,0 L-45.5,45.5 L0,0'])
paths.append([5, 'translate(57,145)', 'M0,0 L162,0 L0,0'])
paths.append([5, 'translate(57,137)', 'M0,0 L58,49.5 L0,0'])
paths.append([5, 'translate(115,178)', 'M0,0 L25,0 L104,-37 L24,0'])
paths.append([4, 'translate(103,337)', 'M0,0 L0,-43 Q-14,-62,-9,-92 Q-7,-102,-17,-107'])
paths.append([4, 'translate(86,186.5)', 'M0,0 L0,97 L24,117 L29,117 L24,117'])
paths.append([5, 'translate(3,205)', 'M0,0 L83,0 L0,0'])
paths.append([4, 'translate(33,278)', 'M0,0 L-30,18 L0,0'])
paths.append([10, 'translate(0,326)', 'M0,0 L13,0 L0,0'])
paths.append([8, 'translate(0,299)', 'M0,0 L18,0 L0,0'])
#Baldwin
paths.append([5, 'translate(152,134)', 'M0,0 L0,11 L0,0'])
paths.append([5, 'translate(190,134)', 'M0,0 L0,20.58 L0,0'])
paths.append([5, 'translate(190,145)', 'M0,0 L29,38 L0,0'])
paths.append([5, 'translate(207.5,186.5)', 'M0,0 L0,-18.57 L0,0'])
paths.append([5, 'translate(207.5,186.5)', 'M0,0 L206.5,0 L0,0'])
paths.append([10, 'translate(203,85)', 'M0,0 L16,0 L0,0'])
paths.append([6, 'translate(219,85)', 'M0,0 L166,0 L0,0'])
#Baldwin/OP
paths.append([4, 'translate(349,98)', 'M0,0 L0,270, L0,0'])
paths.append([4, 'translate(367,85)', 'M0,0 Q-14,2,-18,16 Q-14,2,0,0'])
paths.append([4, 'translate(331,85)', 'M0,0 Q14,2,18,16 Q14,2,0,0'])
paths.append([4, 'translate(349,131)', 'M0,0 L8,0 L0,0'])
paths.append([5, 'translate(219,141)', 'M0,0 L96,-56 L0,0'])
paths.append([5, 'translate(120,25)', 'M0,0 L518,0 L0,0'])
paths.append([5, 'translate(320.5,25)', 'M0,0 L0,60 L0,0'])
paths.append([5, 'translate(219,85)', 'M0,0 Q3,-56,56,-60 Q3,-56,0,0'])
paths.append([5, 'translate(275,25)', 'M0,0 Q43.5,0,45.5,60 Q43.5,0,0,0'])
paths.append([6, 'translate(320.5,54)', 'M0,0 L5.5,0 L0,0'])
#Missouri/OP/Kirk
paths.append([6, 'translate(407.5,84)', 'M0,0 L0,75 L0,0'])
paths.append([5, 'translate(407.5,111)', 'M0,0 L115.5,0 L0,0'])
paths.append([5, 'translate(414,259)', 'M0,0 L224,0 L0,0'])
paths.append([5, 'translate(414,149)', 'M0,0 L25,25 L0,0'])
paths.append([5, 'translate(414,186.5)', 'M0,0 Q20,0,25,-12.5 Q20,0,0,0'])
paths.append([5, 'translate(439,174)', 'M0,0 L-2,8 L-25,48 L-2,8'])
paths.append([4, 'translate(429,137.5)', 'M0,0 L-15,-15 L0,0'])
paths.append([4, 'translate(468.5,123)', 'M0,0 L0,-12 L0,0'])
paths.append([4, 'translate(429,235.5)', 'M0,0 L-15,15 L0,0'])
paths.append([4, 'translate(468.5,250)', 'M0,0 L0,9 L0,0'])
paths.append([4, 'translate(508,137.5)', 'M0,0 L14,-14 L0,0'])
paths.append([4, 'translate(508,235.5)', 'M0,0 L7,7 L14,7 L7,7'])
paths.append([4, 'translate(448,230)', 'M0,0 L3,3 L3,29 L3,3'])
paths.append([21, 'translate(378.5,247.5)', 'M0,0 L0,6.5, L0,0'])
paths.append([5, 'translate(349,247.5)', 'M0,0 L64,0, L0,0'])
#Union/Magruder
paths.append([5, 'translate(3,450)', 'M0,0 L131,0 L0,0'])
paths.append([5, 'translate(3,435)', 'M0,0 L124,0 L0,0'])
paths.append([5, 'translate(127,435)', 'M0,0 L7,15 L0,0'])
paths.append([4, 'translate(115,435)', 'M0,0 L0,147.58 L0,0'])
paths.append([6, 'translate(127,394.5)', 'M0,0 L5,0 L0,0'])
paths.append([4, 'translate(106,475)', 'M0,0 L9,0 L28,-25 L9,0'])
paths.append([4, 'translate(106,494)', 'M0,0 L9,0 L0,0'])
paths.append([5, 'translate(36.5,401)', 'M0,0 L0,64 L0,0'])
paths.append([4, 'translate(36.5,403)', 'M0,0 L-33.5,24 L0,0'])
paths.append([4, 'translate(86,435)', 'M0,0 L0,30 L0,0'])
paths.append([4, 'translate(115,494)', 'M0,0 L14,20.5 L27,20.5 L14,20.5'])
paths.append([5, 'translate(155.5,542)', 'M0,0 L0,42.23 L0,0'])
paths.append([5, 'translate(92,564)', 'M0,0 L0,17.64 L0,0'])
paths.append([10, 'translate(72,551)', 'M0,0 L0,29.82 L0,0'])
paths.append([10, 'translate(67,546)', 'M0,0 L19,0 L0,0'])
#Violette/Magruder
paths.append([6, 'translate(219,25)', 'M0,0 L0,425 L0,0'])
paths.append([5, 'translate(211,526)', 'M0,0 L-3,26 L-3,60.5'])
paths.append([9, 'translate(209,526)', 'M0,0 L71,0 L0,0'])
paths.append([15, 'translate(273,528.5)', 'M0,0 L20,0 L0,0'])
paths.append([5, 'translate(290,526)', 'M0,0 L0,65.72 L0,0'])
paths.append([7, 'translate(273,452)', 'M0,0 L0,74.5 L0,0'])
paths.append([5, 'translate(219,452)', 'M0,0 Q5,47,54,74 Q5,47,0,0'])
paths.append([5, 'translate(213,526)', 'M0,0 Q14,-60,60,-74 Q14,-60,0,0'])
paths.append([5, 'translate(273,452)', 'M0,0 Q18,25,17,74 Q18,25,0,0'])
paths.append([6, 'translate(219,452)', 'M0,0 L54,0 L354,6 L54,0'])
paths.append([8, 'translate(205,396)', 'M0,0 L0,12 L0,0'])
paths.append([5, 'translate(206.5,407)', 'M0,0 L12.5,45 L0,0'])
paths.append([5, 'translate(216,441)', 'M0,0 Q2.5,15,4,30 Q2.5,15,0,0'])
paths.append([5, 'translate(219,452)', 'M0,0 Q3,38,-6,74 Q3,38,0,0'])
paths.append([17, 'translate(341.5,453.38)', 'M0,0 L0,15.62 L0,0'])
paths.append([13, 'translate(341.5,588)', 'M0,0 L0,7 L0,0'])
#Union/Lib/Magruder
paths.append([5, 'translate(203,401)', 'M0,0 L16,-13 L0,0'])
paths.append([5, 'translate(162,365)', 'M0,0 Q35,8,57,23 Q35,8,0,0'])
paths.append([4, 'translate(205,353)', 'M0,0 L0,21 L0,0'])
paths.append([5, 'translate(150,387.5)', 'M0,0 L31,0 L69,-20.5 L31,0'])
paths.append([6, 'translate(127,315)', 'M0,0 L0,120 L0,0'])
paths.append([4, 'translate(127,387.5)', 'M0,0 L12,0 A14,14,360,1,1,25,0'])
paths.append([6, 'translate(127,372)', 'M0,0 Q11,-26,35,-7 Q13,-26,0,0'])
paths.append([5, 'translate(127,319.5)', 'M0,0 L78,0 L0,0'])
paths.append([5, 'translate(127,315)', 'M0,0 L52,50 L0,0'])
paths.append([5, 'translate(179,319.5)', 'M0,0 L0,45.5 L0,0'])
paths.append([5, 'translate(127,337)', 'M0,0 Q30,3,52,28 Q30,3,0,0'])
paths.append([5, 'translate(98,315)', 'M0,0 L29,0 L0,0'])
paths.append([5, 'translate(98,337)', 'M0,0 L29,0 L0,0'])
#Dobson/Violette
paths.append([8, 'translate(414,111)', 'M0,0 L0,485.65 L0,0'])
paths.append([12, 'translate(390,528.5)', 'M0,0 L24,0 L0,0'])
paths.append([5, 'translate(414,531.5)', 'M0,0 L69,0 L0,0'])
paths.append([5, 'translate(414,487)', 'M0,0 L14,0 L0,0'])
paths.append([5, 'translate(414,576)', 'M0,0 L14,0 L0,0'])
paths.append([5, 'translate(440.5,526.5)', 'M0,0 L0,10 L7,17 L17,17 L24,10 L24,0 L17,-7 L7,-7 L0,0 L0,10'])
paths.append([5, 'translate(452.5,496)', 'M0,0 L0,23.5 L0,0'])
paths.append([5, 'translate(444,540)', 'M0,0 L-30,27.5 L0,0'])
#Power/Health Center
paths.append([11, 'translate(284,431)', 'M0,0 L0,21 L0,0'])
paths.append([13, 'translate(252.5,414)', 'M0,0 L0,38 L0,0'])
paths.append([5, 'translate(219,430)', 'M0,0 Q10,15,36,22 Q10,15,0,0'])
paths.append([4, 'translate(342,435)', 'M0,0 L0,17 L0,0'])
paths.append([4, 'translate(335,435)', 'M0,0 L0,17 L0,0'])
#BNB
paths.append([5, 'translate(414,363.5)', 'M0,0 L82,0 L0,0'])
paths.append([5, 'translate(414,295.5)', 'M0,0 L14,0 L0,0'])
paths.append([5, 'translate(414,431.5)', 'M0,0 L14,0 L0,0'])
paths.append([5, 'translate(486.5,313.5)', 'M0,0 L0,100, L0,0'])
paths.append([5, 'translate(414,313.5)', 'M0,0 L72.5,0, L0,0'])
paths.append([5, 'translate(414,413.5)', 'M0,0 L72.5,0, L0,0'])
paths.append([5, 'translate(489.5,308.5)', 'M0,0 L-3,5, L0,0'])
paths.append([5, 'translate(486.5,413.5)', 'M0,0 L3,5, L0,0'])
paths.append([5, 'translate(423,313.5)', 'M0,0 L63.5,100, L0,0'])
paths.append([5, 'translate(486.5,313.5)', 'M0,0 L-63.5,100, L0,0'])
paths.append([6, 'translate(150,365)', 'M0,0 L264,0, L0,0'])
paths.append([4, 'translate(486.5,395)', 'M0,0 L9.5,0, L0,0'])
paths.append([4, 'translate(486.5,397)', 'M0,0 L-12,0, L0,0'])
paths.append([4, 'translate(472,259)', 'M0,0 L0,24, L52,24 L0,24' ])

#Health/Kirk
paths.append([5, 'translate(330,411)', 'M0,0 84,0, L0,0'])
paths.append([6, 'translate(330,411)', 'M0,0 0,4, L0,0'])
paths.append([6, 'translate(375,411)', 'M0,0 0,4, L0,0'])
paths.append([5, 'translate(310,365)', 'M0,0 L0,15 Q0,43,20,46 Q0,41,0,15'])
paths.append([5, 'translate(351.5,365)', 'M0,0 L0,15 Q0,43,-21.5,46 Q0,43,0,15'])
paths.append([5, 'translate(354,365)', 'M0,0 L0,15 Q0,43,21,46 Q0,43,0,15'])
paths.append([5, 'translate(414,365)', 'M0,0 Q-8,40,-34,46 Q-8,40,0,0'])
paths.append([5, 'translate(354,365)', 'M0,0 Q0,-24,24.5,-24 Q0,-24,0,0'])
paths.append([5, 'translate(414,365)', 'M0,0 Q-12,-24,-35.5,-24 Q-12,-24,0,0'])
paths.append([5, 'translate(349,341)', 'M0,0 L68,0 L0,0'])
paths.append([5, 'translate(268,365)', 'M0,0 L0,29 L0,0'])
paths.append([21, 'translate(378.5,336)', 'M0,0 L0,5 L0,0'])
#Lib/Kirk
paths.append([5, 'translate(208,283)', 'M0,0 L112,0 L0,0'])
paths.append([5, 'translate(208,314)', 'M0,0 L11,0 L0,0'])
paths.append([5, 'translate(208,250)', 'M0,0 L11,0 L0,0'])
paths.append([5, 'translate(208,220)', 'M0,0 L11,0 L0,0'])
paths.append([4, 'translate(234,283)', 'M0,0 Q0,31,-15,31 Q0,31,0,0'])
paths.append([4, 'translate(219,265)', 'M0,0 Q15,0,15,18 Q15,0,0,0'])
paths.append([4, 'translate(251,283)', 'M0,0 L0,49 L0,0'])
paths.append([4, 'translate(301,283)', 'M0,0 L0,49 L0,0'])
paths.append([4, 'translate(249,330)', 'M0,0 L54,0 L0,0'])
paths.append([14, 'translate(276,283)', 'M0,0 L0,6 L0,0'])
paths.append([4, 'translate(232.75,298.5)', 'M0,0 L22.25,-15.5, L0,0'])
paths.append([5, 'translate(320,283)', 'M0,0 Q14,3,29,20 Q14,3,0,0'])
paths.append([5, 'translate(320,283)', 'M0,0 Q14,-3,29,-20 Q14,-3,0,0'])



for i in range(len(paths)):  
    path = draw.Path(d=paths[i][2], fill='none', stroke='black', stroke_width=paths[i][0] + .3, transform=paths[i][1])
    d.append(path)

#Special path shapes
km = draw.Path(fill='white', stroke='black', stroke_width='.15', transform='translate(262,283)')
km.M(0,0).A(14,14,360,1,1,28,0).L(0,0)
d.append(km)

kirk = draw.Path(fill='white', stroke='black', stroke_width='.15', transform='translate(373,247.5)')
kirk.M(0,0).A(5.5,7.5,360,1,1,11,0).L(0,0)
d.append(kirk)

for i in range(len(paths)):  
    path = draw.Path(d=paths[i][2], fill='none', stroke='white', stroke_width=paths[i][0], transform=paths[i][1])
    d.append(path)
    
buildings = []
#mcclain
buildings.append([31, 27, '''M0,0 L21,0 L21,25 L31,25 L31,13 L39,13 L39,18 L78,18 L78,104 L31,104 L31,92
L21,92 L21,110 L0,131 L0,0 L21,0''']) 

#baldwin
buildings.append([117, 47, '''M0,0 L17,0 L17,-12 L86,-12 L86,87 L22,87 L22,74 L16,74 L16,21 L0,21 L0,0 L17,0'''])

#op
buildings.append([326, 35, '''M0,0 L72,0 L72,19 L85,19 L85,14 L100,14 L100,10 L190,10 L190,72
L87,72 L87,49 L73,49 L73,58 L76,58 L76,136 L74,136 L74,143 L33,143 L33,136 L31,136 L31,58 L59,58
L59,38 L0,38 L0,0 L71,0'''])

#violette
buildings.append([293, 469, '''M0,0 L16,0 L16,1 L39,1 L39,0 L58,0 L58,1 L81,1 L81,0 L97,0 L97,15 L95,15
L95,49 L97,49 L97,70 L95,70 L95,104 L97,104 L97,119 L81,119 L81,118 L58,118 L58,119 L39,119 L39,118
L16,118 L16,119 L0,119 L0,104 L2,104 L2,70 L0,70 L0,49 L2,49 L2,15 L0,15 L0,0 L15,0'''])

#magruder
buildings.append([132, 390, '''M0,0 L9,0 L9,-4 A12,12,360,1,1,18,-4 L18,0 L47,0 L72,0 L72,6 L71,6
L71,132 L77,132 L77,140 L71,140 L71,152 L69,152 L69,171 L26,171 L26,152 L10,152 L10,65 L2,65 L2,55
L10,55 L10,9 L0,9 L0,0 L9,0'''])

#dobson
buildings.append([428, 478, '''M0,0 L67,0 L72,5 L72,102 L67,107 L0,107 L0,89 L50,89 L55,84 L55,23 L50,18
L0,18 L0,0 L63,0'''])

#bnb
buildings.append([425, 287, '''M0,0 L31,0 L31,-6 L25,-6 L25,-24 L43,-24 L43,-6 L37,-6 L37,0 L82,0 L86,4
L86,38 L94.5,38 L94.5,50 L86,50 L86,149 L82,153 L0,153 L0,136 L60,136 L69,127 L69,83 L67,83 L67,71
L69,71 L69,26 L60,17 L0,17 L0,0 L31,0'''])

#missouri
buildings.append([420, 144, '''M0,0 L14,-13 L38,11 L38,-21 L55,-21 L55,11 L79,-13 L93,0 L69,24 L69,28 L90,28
L90,57 69,57 L69,61 L93,85 L79,98 L55,74 L55,106 L38,106 L38,74 L14,98 L0,85 L24,61 L17,55 L17,30 L24,24 L0,0, L14,-13'''])

#power
buildings.append([239, 394, '''M0,0 L44,0 L44,22 L55,22 L55,46 L42,46 L42,42 L20,42 L20,20 L0,20 L0,0 L42,0'''])

#health
buildings.append([296, 417, '''M0,0 L30,0 L30,-2 L38,-2 L38,0 L75,0 L75,-2 L83,-2 L83,0 L107,0 L107,21
L47,21 L47,19 L19,19 L19,21 L0,21 L0,0 L28,0'''])

#library
buildings.append([135, 183, '''M0,0 L69,0 A6,6,360,0,1,75,6 L75,104 A4.5,4,360,1,1,75,113 L75,175 L65,175
L65,165 L70,165 L70,134 L0,134 L0,0 L59,0'''])

#union
buildings.append([18, 294, '''M0,0 L70,0 L70,18 L80,18 L80,46 L70,46 L70,107 L39,107 L35,129 L21,129 L21,107 L0,107
L0,39 L-5,39 L-5,25 L0,25 L0,0 L63,0'''])

#kirk
buildings.append([368, 260, '''M0,0 L0,-6 L21,-6 L21,0 L33,0 L33,70 L21,70 L21,76 L0,76 L0,70 L-12,70 L-12,0 L0,0'''])

#memorial
buildings.append([269, 289, '''M0,0 L14,0 L14,10 L24,10 L24,26 L17,26 L17,36 L-3,36 L-3,26 L-10,26 L-10,10 L0,10 L0,0'''])

#Smith
buildings.append([86, 543, '''M0,0 L12,0 L12,10 L18,10 L18,21 L-6,21 L-6,8 L0,8 L0,0 L9,0'''])

#for i in range(len(buildings)):
#    position = 'translate(' + str(buildings[i][0]) + ',' + str(buildings[i][1] + 1) + ')'
#    path = draw.Path(d=buildings[i][2], fill='#999999', stroke='#6A3F93', stroke_width='.3', transform=position)
#    d.append(path)

for i in range(len(buildings)):
    position = 'translate(' + str(buildings[i][0]) + ',' + str(buildings[i][1]) + ')'
    path = draw.Path(d=buildings[i][2], fill='#BBBBBB', stroke='black', stroke_width='.3', transform=position)
    d.append(path)

vLot = draw.Path(fill='white', stroke='black', stroke_width='.3', transform='translate(216,530.5)')
vLot.M(9,0).L(63,0).L(63,58).L(44,58).L(44,54).L(0,54).L(0,10).L(9,10).L(9,0).L(63,0)
d.append(vLot)

macLot = draw.Path(fill='white', stroke='black', stroke_width='.3', transform='translate(20,465)')
macLot.M(0,0).L(40,0).L(40,-5).L(78,-5).L(86,5).L(86,40).L(47,40).L(47,125).L(37,125).L(37,93).L(32,88).L(0,88).L(0,0).L(25,0)
d.append(macLot)

unionLot = draw.Path(fill='white', stroke='black', stroke_width='.3', transform='translate(0,189)')
unionLot.M(0,0).L(84,0).L(84,95).L(33,95).L(33,89).L(23,89).L(23,23).L(31,23).L(31,13.5).L(0,13.5).L(0,0).L(82,0)
d.append(unionLot)

opLot = draw.Path(fill='white', stroke='black', stroke_width='.3', transform='translate(524.5,45)')
opLot.M(0,0).L(107.5,0).L(107.5,35).L(117.5,35).L(117.5,50).L(107.5,50).L(107.5,92).L(117.5,92).L(117.5,108).L(107.5,108).L(107.5,151).L(117.5,151).L(117.5,166).L(107.5,166).L(107.5,203).L(0,203).L(0,0).L(104.5,0)
d.append(opLot)

bnbLot = draw.Path(fill='white', stroke='black', stroke_width='.3', transform='translate(524.5,269)')
bnbLot.M(0,0).L(107.5,0).L(107.5,34).L(117.5,34).L(117.5,49).L(107.5,49).L(107.5,91).L(117.5,91).L(117.5,107).L(107.5,107).L(107.5,145).L(0,145).L(0,0).L(104.5,0)
d.append(bnbLot)

dobLot = draw.Path(fill='white', stroke='black', stroke_width='.3', transform='translate(529.5,471)')
dobLot.M(0,0).L(37,0).Q(37,-16,48,-16).L(148,-13).L(148,-4).L(55,-6).Q(46,-7,46,0).L(56,0).L(56,81).L(0,81).L(0,0).L(30,0)
d.append(dobLot)


for key in nodes:
    for i in nodes[key]:
        path = draw.Path(d='M0,0' + i, stroke='navy', stroke_width=2, fill='none', transform='translate' + str(key))
        d.append(path)

for key in nodes:
    d.append(draw.Circle(0, 0, 2, fill='red', stroke='none', transform='translate' + str(key)))


d.set_pixel_scale(2.392)  # Set number of pixels per geometry unit
#d.set_render_size(400, 200)  # Alternative to set_pixel_scale
d.save_svg('example.svg')
d.save_png('example.png')

# Display in Jupyter notebook
#d.rasterize()  # Display as PNG
d  # Display as SVG

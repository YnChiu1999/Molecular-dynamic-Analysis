# -*- coding: utf-8 -*-
# Structural evolution ====================================
# for i in range(1, 788):
#     Al = 0
#     Zn = 0
#     Mg = 0
#     filename = './Comp_F5V_600K_1000ps_S/POSCAR/POSCAR_1x1x1.lammps_' + str(i)
#     f = open(filename)
#     lines = f.readlines()
#     for line in lines:
#         if (lines.index(line)) >11:
#             line = line.split()
#             if line[1] == '1':
#                 Mg += 1
#             elif line[1] == '2':
#                 Al += 1
#             elif line[1] == '3':
#                 Zn += 1
#     print("Al: %.d" % Al)
#     print("Mg: %.d" % Mg)
#     print("Zn: %.d" % Zn)
#     f.close()

def atomNum(i, filefolder):
    Al = 0
    Zn = 0
    Mg = 0
    filename = filefolder+'/POSCAR/POSCAR_1x1x1.lammps_' + str(i)
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        if (lines.index(line)) >11:
            line = line.split()
            if line[1] == '1':
                Mg += 1
            elif line[1] == '2':
                Al += 1
            elif line[1] == '3':
                Zn += 1
    f.close()
    return Mg, Al, Zn




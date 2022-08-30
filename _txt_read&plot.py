# -*- coding: utf-8 -*-

col = []
Step = []
Time = []
Temp = []
KinEng = []
PotEng = []
TotEng = []
Press = []
Pxx = []
Pyy = []
Pzz = []
Lx = []
Ly = []
Lz = []
Volume = []

from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
import originpro as op

df_temp = pd.DataFrame()
# Compositonal evolution ====================================
# for i in range(1, 38):
#     filename = './Test2/log.lammps_' + str(i)
#     df = pd.read_csv(filename, sep='\s+', header=87, on_bad_lines='skip')
#     df = df.drop(labels=range(2002, 2030), axis=0)
#     df = df.astype(float, errors='raise')
#     df['Time'] = df['Time'].map(lambda x: x + 1000.000 * (i - 1))
#     df['TotEng'] = df['TotEng'].map(lambda x: x -(-716.377664306472) + ((-13.1645841692724) - (-12.6466222342153/9) - (-2.42554830997194/2*3)) * (i - 1))
#     df = pd.concat([df_temp, df], axis=0)
#     df_temp = df.copy()

# # Lattice Constant ====================================
# for i in range(1001, 1002):
#     filename = './Test2/log.lammps_' + str(i)
#     df = pd.read_csv(filename, sep='\s+', header=87, on_bad_lines='skip')
#     df = df.drop(labels=range(20002, 20030), axis=0)
#     df = df.astype(float, errors='raise')
#     df['Time'] = df['Time'].map(lambda x: x + 1000.000 * (i - 1))
#     df['TotEng'] = df['TotEng'].map(lambda x: x - (-542.829948887566) )
#     df = pd.concat([df_temp, df], axis=0)
#     df_temp = df.copy()

# Structural evolution ====================================
for i in range(1, 200):
    filename = './Test_5V_600K/log.lammps_' + str(i)
    df = pd.read_csv(filename, sep='\s+', header=87, on_bad_lines='skip')
    df = df.drop(labels=range(2002, 2030), axis=0)
    df = df.astype(float, errors='raise')
    df['Time'] = df['Time'].map(lambda x: x + 1000.000 * (i - 1))
    #df['TotEng'] = df['TotEng'].map(lambda x: x -(-716.377664306472) + ((-13.1645841692724) - (-12.6466222342153/9) - (-2.42554830997194/2*3)) * (i - 1))
    df = pd.concat([df_temp, df], axis=0)
    df_temp = df.copy()

df['Total Energy'] = df['TotEng'].rolling(1000, min_periods=1).mean()
df['Moving Average'] = df['TotEng'].rolling(10000, min_periods=1).mean()
print(df['Moving Average'])
ax = df.plot(x='Time', y='Total Energy', figsize=(15,5), color='g', alpha=0.5)
df.plot(x='Time', y='Moving Average', figsize=(15,5), color='k', linewidth=2.5, ax=ax)
# df.plot(x='Time', y='KinEng', title='Total Energy')
# df.plot(x='Time', y='PotEng', title='Total Energy')
# plt.title('Total energy (eV/lattice)', fontsize=25)
# plt.xticks([0, 1, 2])
# plt.legend().remove()
# plt.xlim(0, 100000)
# plt.yticks([-700, -710, -720, -730], fontname = 'Helvetica')
plt.xlabel('Simulation time (fs)', fontsize=18, fontname = 'Helvetica')
plt.ylabel('Total energy (eV/lattice)', fontsize=18, fontname = 'Helvetica')
plt.show()

# op.set_show()
# wks = op.new_sheet('w')
# wks.from_list(0, df['Time'].tolist(), 'X Values')
# wks.from_list(1, df['Total Energy'].tolist(), 'Y Values')
# wks.from_list(2, df['Moving Average'].tolist(), 'Y Values')


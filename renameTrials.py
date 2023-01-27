import os
import re

workDir = 'C:\\Users\\teachinglab\\Desktop\\S10_org'
workDir = 'C:\\Users\\teachinglab\\Desktop\\MarMarProject\\S11_hyungju'

(_,_,filelist) = next(os.walk(workDir))
for fn in filelist:
    id = int(re.split('S10_trial_([0-9]+).csv', fn)[1])
    newName = f'S11_trial_{id-359:04d}.csv'
    os.rename(os.path.join(workDir, fn), os.path.join(workDir,newName))
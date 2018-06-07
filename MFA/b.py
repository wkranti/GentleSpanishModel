import sys
import subprocess
import argparse
import shutil
import glob
import re
import os

parser = argparse.ArgumentParser(description="Aligner")
parser.add_argument("audiofile",type=str,help="Audiofile to be aligned")
parser.add_argument("textfile",type=str,help="transcript to be aligned")

args = parser.parse_args()

shutil.copy(args.audiofile , 'MFA/MFATestWav')
shutil.copy(args.textfile , 'MFA/MFATestWav')

#process=subprocess.Popen(['MFA/bin/mfa_align','MFA/MFATestWav','MFA/spanishdict.txt','MFA/Models/spanish.zip','output'])
process=subprocess.call(['MFA/bin/mfa_align','MFA/MFATestWav','MFA/spanishdict.txt','MFA/Models/spanish.zip','output'])
if process != 0:
    raise RuntimeError("Unable to align")

list = glob.glob("output/MFATestWav/*.TextGrid")
str = ''.join(list)
process2=subprocess.call(['python3','textgrid2csv.py','-o','output.csv',str])
if process2 != 0:
    raise RuntimeError("unable to do conversion from TextGrid to CSV")
list1 = glob.glob("*.csv")
str2 = ''.join(list1)
process3=subprocess.call(['python3','csv2json.py','-i',str2,'-o','output.json'])
if process3 != 0:
    raise RuntimeError("Unable to do parse from CSV to JSON")
#File cleaning operation
pattern = "^"
path  = "MFA/MFATestWav/"
path2 = "output/MFATestWav"
#Cleans test wav file we copied from user source to MFATestWav
for root, dirs, files in os.walk(path):
    for file in filter(lambda x: re.match(pattern, x), files):
          shutil.os.remove(os.path.join(root, file))
#Cleans Textgrid output of MFA Alignment Process , We won't need that now after getting
#csv and JSON file          
for root,dirs,files in os.walk(path2):
    for file in filter(lambda x: re.match(pattern,x),files):
          shutil.os.remove(os.path.join(root,file))

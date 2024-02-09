import os
import glob

path = os.chdir('D:\\Picture')
rootdir = 'D:\\Picture\\'

i = 1
for file in glob.glob(f'{rootdir}/*.jpg', recursive=True):
    if i < 10:
        new_file_name = "00{}.jpg".format(i)
        os.rename(file, new_file_name)
    elif i < 100:
        new_file_name = "0{}.jpg".format(i)
        os.rename(file, new_file_name)
    else:
        new_file_name = "{}.jpg".format(i)
        os.rename(file, new_file_name)
    i += 1
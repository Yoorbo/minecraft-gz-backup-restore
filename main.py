import json
import gzip
import binascii
import os
import shutil


def is_gz_file(filepath):
    with open(filepath, 'rb') as test_f:
        return binascii.hexlify(test_f.read(2)) == b'1f8b'


rootDir = '.'
usercommand = input()
if "unzip" in usercommand:
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            filepath = os.path.join(dirName,fname)
            if is_gz_file(filepath):
                with gzip.open(filepath, 'rb') as f_in:
                    with open(filepath[:-2], 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                        print(f"Unzipped {f_out}")
if "deletegz" in usercommand:
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            filepath = os.path.join(dirName,fname)
            if is_gz_file(filepath):
                os.remove(filepath)
                print(f"Deleted {filepath}")
print("Finished")

# Imports the Google Cloud client library
from google.cloud import storage
import os
import sys
import subprocess

bucket_name = "clasick"
source_file_name = ""
args = sys.argv
storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)


print("[CREATE] HLS")
comArgs = [
    'mediafilesegmenter', 
    '-f', 
    'output/' + args[1], 
    '-i', 
    args[2], 
    '-B', 
    args[3], 
    'music/' + args[1] + '/source/' + args[2]
    ]
try:
    res = subprocess.check_call(comArgs)
except:
    print("Error.")

print("[UPLOAD] Music Source")
hlsDirectory = os.listdir(os.getcwd()+"/output/"+ args[1] + "/")
for a in hlsDirectory:
    destination_blob_name = "music/sources/" + args[1] + "/" + a
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename("./output/" + args[1] + "/" + a)
    print("[Done] "+ a)

print("[UPLOAD] Music Icon")
iconDirectory = os.listdir(os.getcwd()+"/music/"+ args[1] + "/icon/")
for a in iconDirectory:
    destination_blob_name = "music/icons/" + args[1] + "/" + a
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename("./music/" + args[1] + "/icon/" + a)
    print("[Done] "+ a)
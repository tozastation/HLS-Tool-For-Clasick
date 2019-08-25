# Imports the Google Cloud client library
from google.cloud import storage
import os
import sys
import subprocess

bucket_name = "clasick"
source_file_name = ""
args = sys.argv
project_name = "tozastation"
storage_client = storage.Client(project_name)
bucket = storage_client.get_bucket(bucket_name)


print("[UPLOAD] Music Source")
hlsDirectory = os.listdir(os.getcwd()+"/src/"+ args[1] + "/")
for a in hlsDirectory:
    destination_blob_name = "music/" + args[2] + "/" + a
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename("./src/" + args[1] + "/" + a)
    print("[Done] "+ a)

# print("[UPLOAD] Music Icon")
# iconDirectory = os.listdir(os.getcwd()+"/music/"+ args[1] + "/icon/")
# for a in iconDirectory:
#     destination_blob_name = "music/icons/" + args[1] + "/" + a
#     blob = bucket.blob(destination_blob_name)
#     blob.upload_from_filename("./music/" + args[1] + "/icon/" + a)
#     print("[Done] "+ a)
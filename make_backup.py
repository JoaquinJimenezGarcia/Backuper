import os
import yaml
import pyminizip
import datetime

with open("config.yaml", "r") as f:
    config = yaml.load(f)

x = datetime.datetime.now()
backup_folder = " backup."+x.strftime("%Y")+x.strftime("%m")+x.strftime("%d")
backup_folder_zip = "backup."+x.strftime("%Y")+x.strftime("%m")+x.strftime("%d") + ".zip"
backup_folder_encrypted = backup_folder_zip + ".encr"
backup_destiny = config["destiny"]
compression_level = 5

os.system("mkdir " + backup_folder)

for path in config["paths"]:
    print("Copying " + path + " in backup folder...")
    os.system("cp -r " + path + backup_folder)

print("Compressing backup...")
os.system("zip -r " +  backup_folder_zip + backup_folder)

if config["encrypted"]:
    print("Encrypting backup file...")
    pyminizip.compress(backup_folder_zip, "", backup_folder_encrypted, config["encrypting_password"], compression_level)

    print("Moving backup to " + backup_destiny)
    os.system("mv " + backup_folder_encrypted + " " + backup_destiny)
    os.system("rm -rf " + backup_folder_zip)

else:    
    print("Moving backup to " + backup_destiny)
    os.system("mv" + backup_folder + ".zip " + backup_destiny)

os.system("rm -rf" + backup_folder)
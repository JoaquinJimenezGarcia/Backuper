import os
import yaml

with open("config.yaml", "r") as f:
    config = yaml.load(f)

backup_folder = " backup.$(date +%Y%m%d)" 
backup_destiny = config["destiny"]

os.system("mkdir " + backup_folder)

for path in config["paths"]:
    print("Copying " + path + " in backup folder...")
    os.system("cp -r " + path + backup_folder)

print("Compressing backup...")
os.system("zip -r" +  backup_folder + ".zip" + backup_folder)
print("Moving backup to " + backup_destiny)
os.system("mv" + backup_folder + ".zip " + backup_destiny)

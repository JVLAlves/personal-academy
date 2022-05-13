from configparser import ConfigParser
File = "../config.ini"
config = ConfigParser()
config.read(File)

liskarm = config["liskarm"]
print(list(liskarm.values()))
for lisk in liskarm:
    print(liskarm[lisk])


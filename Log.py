import logging
from Config import read_config

loggingConfig = read_config(section='logging')
loggingDict = {'NOTSET':0,'DEBUG':10,'INFO':20,'WARNING':30,'ERROR':40,'CRITICAL':50}
logging.basicConfig(format='%(asctime)s %(name)-6s %(levelname)-8s %(message)s',**loggingConfig)

formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
console.setFormatter(formatter)

logging.getLogger('').addHandler(console) #This is the root logger

Logdb = logging.getLogger('database.py')#define a new logger for each area your logging this is just an example

Log = logging






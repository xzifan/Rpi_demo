import os, glob,time

os.system("modprobs w1_gpio")
os.system("modprobs w1_therm")

devicelist = glob.glob("/sys/bus/w1/devices/28*")

devicefile = devicelist[0]+"/w1_slave"

while True:
    file = open(devicefile,'r')
    lines = file.readlines()
    file.close()

    print lines[0][:-1]
    print lines[1][:-1]

    tempdata = lines[1].split["="]

    temp = float(tempdata[1])

    temp = temp/1000
    print temp

    time.sleep(1)
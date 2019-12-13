import os, glob,time, requests

os.system("modprobs w1_gpio")
os.system("modprobs w1_therm")

devicelist = glob.glob("/sys/bus/w1/devices/28*")

devicefile = devicelist[0]+"/w1_slave"

url = "http://130.243.35.37"# ip of the main RPi

while True:
    file = open(devicefile,'r')
    lines = file.readlines()
    file.close()

    print lines[0][:-1]
    print lines[1][:-1]

    tempdata = lines[1].split("=")

    temp = float(tempdata[1])

    temp = temp/1000

    dat = datetime.datetime.now()
    timestamp = dat.strftime("%Y-%m-%d;%H:%M:%S")

    data = "{str:"+timestamp+temp+"}"
    print "Request:",json_encode(data)
    r = requests.get(url=url,params = data)

    time.sleep(5)
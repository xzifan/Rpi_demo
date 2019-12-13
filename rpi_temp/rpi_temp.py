import os, glob,time, requests, datetime, smtplib
from email.mime.text import MIMEText
from email.header import Header

os.system("modprobs w1_gpio")
os.system("modprobs w1_therm")

devicelist = glob.glob("/sys/bus/w1/devices/28*")

devicefile = devicelist[0]+"/w1_slave"

url = "http://130.243.35.86/center_http_handle.php"# ip of the main RPi

mail_host = "smtp.gmail.com"  # Set smtp server
mail_user = "c547028957@gmail.com"  # username and pw
mail_pass = "transactmax00r"

sender = 'c547028957@gmail.com'
receivers = 'h19zifxi@du.se'

while True:
    file = open(devicefile,'r')
    lines = file.readlines()
    file.close()

    ##print lines[1][:-1]

    tempdata = lines[1].split("=")

    temp = float(tempdata[1])

    temp = temp/1000
    if (temp>getTemp())
        msg = MIMEText(dateTxt+" "+dat2Txt+": There are"+numOfCars+" in red. "+"The No2 content is "+ NitrogenDioxide)
        #msg = MIMEText("There are "+str(numOfCars)+" cars in red")
        subject = 'This is the python email'
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = Header('Taoren', 'utf-8')
        msg['To'] = Header('Taoren', 'utf-8')
        try:
            smtpObj = smtplib.SMTP(mail_host,587)
            smtpObj.starttls()
            smtpObj.set_debuglevel(1)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, msg.as_string())
            print ("Email successfully sent")
        except smtplib.SMTPException:
            print ("Error: Cannot send email")

    dat = datetime.datetime.now()
    timestamp = dat.strftime("%Y-%m-%d;%H:%M:%S")

    data = timestamp+";"+str(temp)
    print data
    r = requests.get(url=url+"?str="+data)

    time.sleep(5)

def getTemp(){
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?id=2715459&key=5cd561acef24305af40d29a6c9e0469c")
    print r
}
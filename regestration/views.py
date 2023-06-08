from django.shortcuts import render, HttpResponse
import random as rand
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
from twilio.rest import Client
import mysql.connector as mysql

def regestration(request):
    
    return render(request,"C:/Python311/octawebapp/regestration/templates/regestration.html")


def get_data(request,reg_name,otp_num):
    
       print(otp_num)
       
       conn = mysql.connect(
        host="localhost",
        user="root",
        passwd = "",
        database = "octaweb"
       )
       
       cursor = conn.cursor()
       
       txt = "select * from otpsave where OTP = {} ".format(str(otp_num))
       
       cursor.execute(txt)
       
       data = cursor.fetchall()
       
       if len(data) > 0:
                  del_sql = "delete from otpsave where OTP = {}".format(otp_num)
                  
                  cursor.execute(del_sql)
                  conn.commit()
                  
                  return render(request,"C:/Python311/octawebapp/regestration/templates/demo.html",{'name':"OTP success"})
              
       else:
                  return render(request,"C:/Python311/octawebapp/regestration/templates/demo.html",{'name':"incorrect OTP"})     

           

   
def otp_generate():
        otp_num = rand.randrange(10000,99999)
        return otp_num
    
def OTP_verify(request,option):
    
    
    
    x = re.findall("@",str(option))
    sender = "pynatic079@gmail.com"
    password = "eixjxaldkjscgqgz"
    
    otp_number = otp_generate()
    print(otp_number)
    
    
    
    conn = mysql.connect(
        host="localhost",
        user="root",
        passwd = "",
        database = "octaweb"
    )
    cursor = conn.cursor()
    run = True
    while run:
        txt = "select * from otpsave where OTP = {}".format(str(otp_number))
        cursor.execute(txt)
        dom = cursor.fetchall()
        print(dom)
    
        if(len(dom) > 0):
            otp_number = otp_generate()
            print(otp_number)
        else:
            txt = "INSERT into otpsave(OTP) value({})".format(otp_number)
            cursor.execute(txt)
            conn.commit()
            run = False
            
                
        
        
    
    #email_otp
    if len(x) > 0:
        
        msg = MIMEMultipart()
        msg['From'] = str(sender)
        msg['To'] = str(option)
        msg['Subject'] = "OTP verification"
        
        msg.attach(MIMEText(str(otp_number),'plain'))
        
        try:
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            
            server.login(sender,password)
            
            server.sendmail(sender,option,msg.as_string())
            
            print("Email send sucess")
        except Exception as e:
            print(e)
    else:
        acc_sid = "AC062fce8b68afcaa7e0c627872c4a0a89" 
        auth_token = "66961659497c9878ec9018b1faa3b535"
        
        t_phone = "++13203318436"
        r_phone = "+91"+str(option)
        try:
            client = Client(acc_sid,auth_token)
            
            meg = client.messages.create(
                body=str(otp_number),
                from_ = t_phone,
                to = r_phone
                
            )
                
            print("otp send")      
        except Exception as e:
            print(e)     
                
        
    
    
        
    return render(request,"C:/Python311/octawebapp/regestration/templates/demo.html",{'name':option})       
''' 16/03/2020 '''

import smtplib, os

email_from = "youremail@gmail.com" #remember! activate this to work : https://support.google.com/accounts/answer/6010255?authuser=1 
email_from_pw= "yourpassword"
email_list = open('./email_list.txt')

for email in email_list:
    email_to = email #lines

    smtp = "smtp.gmail.com" #server

    server = smtplib.SMTP(smtp, 587) #server and port server of google
    server.starttls() #start ttls required by google server
    server.login(email_from,email_from_pw) #login in email to addr

    email_content = "enter your message here"

    server.sendmail(email_from, email_to, email_content)
    server.quit()

    print(f"success send to :  {email} ")

os.system('pause')
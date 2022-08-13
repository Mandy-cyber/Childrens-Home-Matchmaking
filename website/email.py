import smtplib
import sqlite3
import string

conn = sqlite3.connect('jseScrape.db')
cursor = conn.cursor()



## getting 'emails' column from the table
cursor.execute("SELECT name FROM students")

## fetching all usernames from the 'cursor' object
emails = cursor.fetchall()

## function for sending the emails
# def send_email(message): 
#     for email in emails:
#         strippedText = str(email).replace('(','').replace(')','').replace(',','').replace('\"','')
#         server = smtplib.SMTP_SSL("smtp.gmail.com",465)
#         server.login("examplw@gmail.com", "password")
#         server.sendmail(f"example@gmail.com",
#                         {email},
#                         {message})

        # server.quit()

def send_email(message): 
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login("emailfortesting2345@gmail.com", "orangejuice123!")
        server.sendmail(f"emailfortesting2345@gmail.com",
                        "parchiejosh@gmail.com",
                        {message})

        server.quit()

message = input("Please insert email you would like to send")
send_email(message)
    

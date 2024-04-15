# needed to send emails
import smtplib
#to randomly select a quote
import random
#to find the current date to determine if it's the correct day to email a quote
import datetime
SENDER_EMAIL = "nolabbjj@gmail.com"
RECIEVER_EMAIL = 'nolabbjj@gmail.com'
SENDER_PASSWORD = "uxgn zgzc lqqp sbtm"

#grab the current date
current_date = datetime.datetime.now()
#from the current date we can grab the day 0-6, 0 being monday, 6 being sunday
current_day = current_date.weekday()

#statement whether to evaluate if today is Monday
if current_day == 0:
   #converts txt file into a list containing each quote as its own index
   with open("quotes.txt", encoding='utf-8') as data_file:
      read_data = data_file.readlines()
      #randomly choose a quote
      quote = random.choice(read_data)

      #connection procols to send email
      connection = smtplib.SMTP(host="smtp.gmail.com")
      connection.starttls()
      connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)

      #had to encode the message since it was failing due to this 'ascii' codec can't encode character '\u201c'
      MESSAGE = f"Subject: Monday Quote\n\n{quote}"
      MESSAGE = MESSAGE.encode('utf-8')

      connection.sendmail(
         from_addr=SENDER_EMAIL, 
         to_addrs=RECIEVER_EMAIL, 
         msg=MESSAGE)
      
      connection.quit()
      
      












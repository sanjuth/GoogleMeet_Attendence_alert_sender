# GoogleMeet_Attendence_alert_sender
A cool PYTHON script to receive alerts in WhatsApp to your number when your called in the class or attendance is being taken

Ok LET US SEE HOW THIS ACTUALLY WORKS
Firstly we do this mainly with Google Meet , because it has in build captions feature which displays whatever is beign said to text

GAME PLAN :
1) take a screen shot of the google meet window or exactly the part where the captions are displayed 
2) convert the image to text using Tesseract OCR and store the text
3) convert the text to a word wise list 
4) go through the list and check for the required words
 NOTE: when you want to recive the attendence alerts then we ckeck for the words like "Attendence" or "Roll call"
        you may check whatever words you want
5) Then whenever we find the required words we sent a Whatsapp alert to your number or a list of numbers.
6) and done then go and answer your attendence.


PROCEDURE :
firstly download the tessarct OCR
download link : https://sourceforge.net/projects/tesseract-ocr/
then place the tesseract.exe file path in the code (follow the comments in the code to know where to place it)
Ex. pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'


Then for sending the whatsApp messages we use twillo API for WhatsApp
NOTE :if you are not femiliar with twillo here is the link to its official documentation: https://www.twilio.com/docs/whatsapp
place your twillo account sid and token in the main.p file (I added some comments in the code to guide you)
also place your twillo whatsapp number u get in the main.py code file
add all the whatsapp numbers in the phno dictionary with person name for reference (you may add multiple numbers as it is a dictionary)

Create a txt file named recognized.txt in the same folder where main.py is present

In the main.py file find the set of if statements and add whatever words you want to check and you may even edit what message you want to receive in whatsapp
Ex:             if i.upper()=='ATTENDANCE' or i.upper()=='ATTENDANCE.':
                print(i+'.......sent.......')
                for a,b in phno.items():
                    msg = clt.messages.create(body='ALERT!!! Attendence', from_=f, to=b)
                    time.sleep(1)
                #USING THE phno DICTIONARY WE ARE SENDING AN ALERT TO ALL THE NUMBERS
                if i.upper()=='QUIZ' or i.upper()=='QUIZ.':
                  print(i+'.......sent.......')
                  for a,b in phno.items():
                      msg = clt.messages.create(body='ALERT!!! Quiz', from_=f, to=b)
                      time.sleep(1)
               if i=='NAME' or i=='NAME.':
                    print(i+'.......sent.......')
                    msg = clt.messages.create(body=' You r called', from_=f, to=phno['NAME'])
                    #HERE WE ARE ONLY SENDING THE MESSAGE TO THE PERSON WHOSE NAME IS CALLED
                    
You are all set ..

now When you have a class in google meet and it is boring then open the ide where you run main.py and minimize the IDE so the screen of the google meet can get captured
and leave it as it is..

Thank me later...

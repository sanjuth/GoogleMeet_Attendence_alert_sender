# Program to take screenshot
import time
import pyscreenshot
import cv2
import pytesseract
from twilio.rest import Client

account_sid = 'XXXXXXXXXXXXXXX' #place your twillo account author sid here
auth_token = 'XXXXXXXXXXXXXXX' #place oyur twillo account token here
f='whatsapp:+XXXXXXXXXXX' #place your twillo number here from which the messages will be sent
clt = Client(account_sid, auth_token)
#Adding the phone numbers which will recive the alert with name in a dictionary
#NOTE: including country code (Eg. India +911234567890)
phno={'ABC':'whatsapp:+XXXXXXXXX','XYZ':'whatsapp:+XXXXXXXXXX'}

while True :
    time.sleep(5) #we use sleep timer so that the caption wont repeat
    #you can decrease the time if you want to decrease it
    print("----------------------------------------------------------------------------------")
    # The cordinates in the bbox varry for each laptop please find the correct cordinates which covers the captions
    # section on your screen
    image = pyscreenshot.grab(bbox=(500,600,1500,900))
    # To display the captured screenshot


    # To save the screenshot
    image.save("image.png")
    # YOUR REQUIRED TO INSTALL THE TESSERACT-OCR IN YOUR SYSTEM
    # Mention the installed location of Tesseract-OCR in your system
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

    # Read image from which text needs to be extracted
    img = cv2.imread("image.png")

    # Preprocessing the image starts
    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Performing OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

    # Appplying dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

    # Finding contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)

    # Creating a copy of image
    im2 = img.copy()

    # A text file is created and flushed
    file = open("recognized.txt", "w+")
    file.write("")
    file.close()

    # Looping through the identified contours
    # Then rectangular part is cropped and passed on
    # to pytesseract for extracting text from it
    # Extracted text is then written into the text file
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)

        # Drawing a rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]

        # Open the file in append mode
        file = open("recognized.txt", "a", encoding="utf-8")

        # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)

        # IN THE NEXT STEPS THE TEXT IS BROKEN DOWN BY EACH WORD AND CONVERTED TO A LIST
        # SO WE GET A LIST OF WORDS IN li
        text.replace(',',' ')
        text.replace('.',' ')
        li=list(map(str,text.split(' ')))
        # ITERATING THROUGH EACH WORD IN THE LIST AND CHECKING IF OUR REQUIRED WORD IS PRESENT
        # YOU MAY ADD ANY NUMBER OF IF's BUT IT WILL INCREASE THE TIME SO KEEP THAT IN MIND
        # FOR EXAMPLE I HAVE PUT THE WORDS LIKE QUIZ, ATTENDENCE AND A NAME TO SHOW HOW IT WORKS
        # YOU MAY ADD YOUR NAME OR ANY WORD YOUR PROFESSOR USES IN THE CLASS
        for i in li:
            print(i)
            if i.upper()=='ATTENDANCE' or i.upper()=='ATTENDANCE.':
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


        # Appending the text into file
        file.write((text))
        file.write("\n")

        # Close the file
        file.close()

        #WE ARE USING AN FILE TO BACKUP THE TEXT IN A FILE YOU MAY EVEN NOT USE THE FILE AND IT STILL WORKS
        



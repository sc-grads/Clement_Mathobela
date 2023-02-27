import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Python <masterpythonprogramming@gmail.com>'
email['to'] = 'andrei.cma@protonmail.com'
email['subject'] = 'Good job Python!'


email.set_content('Wow! Congratulations! \n This email is send with Python.')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('masterpythonprogramming@gmail.com', 'GdSRJMsAS7')   #username & password
    smtp.send_message(email)
    print('The mail was sent!')


from email.message import EmailMessage
import ssl
import smtplib

sender_email = "samuelsuescarios@gmail.com"
receiver_email = "assuescar@eafit.edu.co"
subject = "Correo de Prueba desde Python"
body = "Este es un correo de prueba enviado desde un script de Python."

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "samuelsuescarios@gmail.com"
smtp_password = "qvnx etyp erwy txmq"

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.set_content(body)


context = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(sender_email,smtp_password) 
    smtp.sendmail(sender_email,receiver_email,message.as_string())




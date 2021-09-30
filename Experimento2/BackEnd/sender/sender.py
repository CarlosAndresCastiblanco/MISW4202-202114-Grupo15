import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "arquitecturagilgrupo15@gmail.com"
password = "@A8p6WiY4PRozHbihtqDRv3d"

message = MIMEMultipart("alternative")
message["From"] = sender_email


def send_email(user, ip, browser, datetime):
    receiver_email = [
        'dantecortesm6@gmail.com']
    message["To"] = ", ".join(receiver_email)

    message["Subject"] = "Inicio de sesión "

    html = """
    <html>
<body>
    <h4>Ingreso de usuario USER</h4>
    <p> Ip de ingreso: IP<br>
        Hora y fecha de ingreso: DATETIME<br>
        Navegador: BROWSER<br>
    </p>
</body>
</html>
    """
    html = html.replace("USER", user)
    html = html.replace("IP", ip)
    html = html.replace("DATETIME", datetime)
    html = html.replace("BROWSER", browser)

    part = MIMEText(html, "html")

    message.attach(part)

    # Create secure connection with server and send sender
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
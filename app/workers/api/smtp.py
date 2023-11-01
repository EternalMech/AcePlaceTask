import smtplib
from app.conf import settings


def send_mail(email: str, message: str) -> None:
    print(settings)
    letter = f"""\
    From: {settings.smtp_name}
    To: {email}
    Subject: Ace place
    Content-Type: text/plain; charset="UTF-8";

    {message}"""
    letter = letter.encode("UTF-8")

    server = smtplib.SMTP_SSL(f'{settings.smtp_host}:{settings.smtp_port}')
    server.login(settings.smtp_login, settings.smtp_password)
    server.sendmail(settings.smtp_email, email, letter)
    server.quit()
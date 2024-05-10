import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from google_auth import get_authenticated_service

def send_email(sender_email, recipient_emails, subject, message, attachments=[]):
    """
    Envia um email com anexo(s) para os destinatários especificados.

    Args:
        sender_email (str): Endereço de email do remetente.
        recipient_emails (list): Lista de endereços de email dos destinatários.
        subject (str): Assunto do email.
        message (str): Corpo do email (texto).
        attachments (list): Lista de tuplas contendo (nome do arquivo, conteúdo do arquivo em base64).

    Returns:
        None
    """

    service = get_authenticated_service(['https://www.googleapis.com/auth/gmail.send'])
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(recipient_emails)
    message['Subject'] = subject

    message_text = MIMEText(message, 'plain')
    message.attach(message_text)

    for attachment_name, attachment_content in attachments:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment_content)
        part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(attachment_name))
        message.attach(part)

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    raw_message = {'raw': encoded_message}
    service.users().messages().send(userId='me', body=raw_message).execute()

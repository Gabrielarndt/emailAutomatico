import os
from google.oauth2 import id_token
from google.auth.transport.requests import Request
from email_sender import send_email

# Carregue as credenciais do Google
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

# Obtenha o token de autenticação do Google
client_id = os.environ['GOOGLE_CLIENT_ID']
auth_uri = 'https://accounts.google.com/o/oauth2/auth'
token_uri = 'https://accounts.google.com/o/oauth2/token'
redirect_uri = 'http://localhost:8080'
response = Request(client_id, redirect_uri).uri_for('signin', scopes=['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/gmail.send'])
print(response)

# Obtenha o email do usuário
id_info = id_token.verify_oauth2_token(response.get('access_token'), None)
user_email = id_info['email']

# Tela principal para inserir dados do email
def main():
    recipient_emails = input("Digite os emails dos destinatários (separados por vírgula): ")
    subject = input("Digite o assunto do email: ")
    message = input("Digite a mensagem do email: ")
    attachments = []

    while True:
        attachment_name = input("Digite o nome do anexo (ou pressione Enter para finalizar): ")
        if not attachment_name:
            break

        attachment_content = input("Digite o conteúdo do anexo em base64: ")
        attachments.append((attachment_name, attachment_content))

    send_email(user_email, recipient_emails.split(','), subject, message, attachments)
    print("Email enviado com sucesso!")

if __name__ == "__main__":
    main()
    
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'c:\Users\gabri\Downloads\email-automaticos-r01-0dde53319742.json'
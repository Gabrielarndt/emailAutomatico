import os
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

def get_authenticated_service(scopes):
    """
    Obtém um objeto de serviço autenticado do Google APIs Client Library.

    Args:
        scopes (list): Lista de escopos de API necessários.

    Returns:
        googleapiclient.discovery.Resource: Objeto de serviço autenticado.
    """


import json

from httplib2 import Http

from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build

scopes = ['https://www.googleapis.com/auth/sqlservice.admin']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'service-account.json', scopes)

sqladmin = build('sqladmin', 'v1beta3', credentials=credentials)
response = sqladmin.instances().list(project='examinable-example-123').execute()

print response

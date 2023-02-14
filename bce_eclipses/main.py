from pathlib import Path
import ee
import json

# Init Credentials
with open(str(Path(__file__).parent.parent)+"/service_account.json", 'rb') as service_account_file:
    service_account_dict = json.load(service_account_file)
service_account = service_account_dict["service_account"]
key_file = str(Path(__file__).parent.parent)+"/auth.json"
credentials = ee.ServiceAccountCredentials(email=service_account, key_file=key_file)
ee.Initialize(credentials)

print("ayyyyyy")
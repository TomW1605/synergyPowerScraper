import datetime
import requests
import json
import sys

username = sys.argv[1]
password = sys.argv[2]

startDate = (datetime.date.today() - datetime.timedelta(days=3)).strftime("%Y-%m-%d")
endDate = (datetime.date.today() - datetime.timedelta(days=2)).strftime("%Y-%m-%d")

loginURL = "https://selfserve.synergy.net.au/apps/rest/session/login.json"
loginPayload = {'username': username, 'password': password}
loginResponse = requests.request("POST", loginURL, data=loginPayload)
loginData = loginResponse.json()

accountURL = "https://selfserve.synergy.net.au/apps/rest/account/" + loginData['accountList'][0]['contractAccountNumber'] + "/show.json"
accountResponse = requests.request("POST", accountURL, cookies=loginResponse.cookies, data={})
accountData = accountResponse.json()

dataURL = "https://selfserve.synergy.net.au/apps/rest/intervalData/" + loginData['accountList'][0]['contractAccountNumber'] + \
          "/getDailyElecIntervalData?intervalDeviceIds=" + accountData['installationDetails']['intervalDevices'][0]['deviceId'] + \
          "&startDate=" + startDate + "&endDate=" + endDate

dataResponse = requests.request("GET", dataURL, cookies=loginResponse.cookies, data={})

print(json.dumps(dataResponse.json(), indent=2))

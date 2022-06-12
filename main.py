import datetime
import requests
import json
import sys

username = sys.argv[1]
password = sys.argv[2]

startDate = (datetime.date.today() - datetime.timedelta(days=2))
startTime = datetime.datetime.combine(startDate, datetime.datetime.min.time())
endDate = datetime.date.today()

loginURL = "https://selfserve.synergy.net.au/apps/rest/session/login.json"
loginPayload = {'username': username, 'password': password}
loginResponse = requests.request("POST", loginURL, data=loginPayload)
loginData = loginResponse.json()

accountURL = "https://selfserve.synergy.net.au/apps/rest/account/" + loginData['accountList'][0]['contractAccountNumber'] + "/show.json"
accountResponse = requests.request("POST", accountURL, cookies=loginResponse.cookies, data={})
accountData = accountResponse.json()

dataURL = "https://selfserve.synergy.net.au/apps/rest/intervalData/" + loginData['accountList'][0]['contractAccountNumber'] + \
          "/getHalfHourlyElecIntervalData?intervalDeviceIds=" + accountData['installationDetails']['intervalDevices'][0]['deviceId'] + \
          "&startDate=" + startDate.strftime("%Y-%m-%d") + "&endDate=" + endDate.strftime("%Y-%m-%d")

dataResponse = requests.request("GET", dataURL, cookies=loginResponse.cookies, data={})

#print(json.dumps(dataResponse.json(), indent=2))

time = startTime
usage = {}
rawUsage = dataResponse.json()["kwHalfHourlyValues"]
rawGeneration = dataResponse.json()["kwhHalfHourlyValuesGeneration"]
print("time\tkwhHalfHourlyValues\tkwhHalfHourlyValuesGeneration")
for ii in range(0, len(rawUsage)):
    print(f"{time.strftime('%Y-%m-%dT%H:%M')}\t{round(rawUsage[ii]*0.5,2)}\t{round(rawGeneration[ii],2)}")
    time += datetime.timedelta(minutes=30)

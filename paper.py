import requests
import json

version = "1.16"

r = requests.get("https://papermc.io/api/v2/projects/paper/version_group/" + version + "/builds")
# r = requests.get("https://papermc.io/api/v2/projects")
rJSON = r.json()

lastBuild = rJSON['builds'][-1]

buildVersion = str(lastBuild['version'])
buildNumber = str(lastBuild['build'])
buildDownload = str(lastBuild['downloads']['application']['name'])

print("https://papermc.io/api/v2/projects/paper/versions/" + buildVersion + "/builds/" + buildNumber + "/downloads/" + buildDownload)
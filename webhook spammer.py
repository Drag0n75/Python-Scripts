import time
import requests

url = "webhook url""

data = {
    "content": "here your messagr"
}
while True:
	time.sleep(0.8)
	response = requests.post(url, json=data)
end
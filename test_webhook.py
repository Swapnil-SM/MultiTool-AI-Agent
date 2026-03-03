import requests


user_message = "Can you tell me about black holes in 3-4 lines"

request_message = {"message": user_message}

url = "http://localhost:5678/webhook-test/1670df40-6cf6-46e1-87b5-fef3a11db943e"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])
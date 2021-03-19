import json
import requests

"""
Imports 10 True/False questions from the open test database API
"""

QUIZ_URL = "https://opentdb.com/api.php"
parameters = {
        "amount": "10",
        "type": "boolean"
    }

try:
    request = requests.get(QUIZ_URL, params=parameters)
    response = json.loads(request.text)

except Exception as ex:
    raise Exception(f"Unable to retrieve dad joke from {QUIZ_URL}: {ex}")

question_data = response['results']

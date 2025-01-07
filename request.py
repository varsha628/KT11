import json

import requests

#logging.basicConfig(level=logging.DEBUG,   filename="output.log",filemode="w")
token='2/1209045127935737/1209069025122973:47adc1feb9976525c53622a9e388f0dd'
def request_get_training():
    '''Get request'''
    response = requests.get('https://app.asana.com/api/1.0/workspaces',headers={'Authorization':f'Bearer {token}'})
    print(response.status_code)
request_get_training()
#requests.get("https://app.asana.com/api/1.0")


def request_post_training():
    headers = {"content-type": "application/json"}
    payload = {
            "name": "new task",
            "data": {
            "name": "gmail",
            "resource_subtype": "default_task",
            "approval_status": "pending",
            "assignee_status": "upcoming",
            "completed": False,
            "due_on": "2019-09-15",
            "external": {
            "gid": "my_gid1",
            "data": "A blob of information"
            },
            "html_notes": "<body>Mittens <em>really</em> likes the stuff from Humboldt.</body>",
            "liked": True,
            "notes": "Mittens really likes the stuff from Humboldt.",
            "start_on": "2019-09-14",
            "projects": [
            "1209045124382645"
            ],
            "workspace": "1200440712055293"
                   }
            }
    response = requests.post("https://app.asana.com/api/1.0/tasks", headers={'Authorization':f'Bearer {token}'})
    response.status_code
request_get_training()

def request_put_training():
    headers = {"content-type": "application/json"}
    payload = {
            "name": "new task",
            "data": {
            "name": "postman",
            "resource_subtype": "default_task",
            "approval_status": "pending",
            "assignee_status": "upcoming",
            "completed": False,
            "due_on": "2019-09-15",
            "external": {
            "gid": "my_gid1",
            "data": "A blob of information"
            },
            "html_notes": "<body>Mittens <em>really</em> likes the stuff from Humboldt.</body>",
            "liked": True,
            "notes": "Mittens really likes the stuff from Humboldt.",
            "start_on": "2019-09-14",
            "projects": [
            "1209045124382645"
            ],
            "workspace": "1200440712055293"
            }
            }
    response = requests.put("https://api.restful-api.dev/objects/ff808181932badb60194253ee0125487", headers={'Authorization':f'Bearer {token}'})
request_get_training()

def request_patch_training():
    '''Patch request'''
    payload = {
            "data": {
                "completed": True,
            }
    }
    response = requests.patch("https://api.restful-api.dev/objects/ff808181932badb60194253ee0125487", headers={'Authorization':f'Bearer {token}'})
request_patch_training

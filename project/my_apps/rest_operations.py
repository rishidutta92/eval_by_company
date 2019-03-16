import requests


resp = requests.get('www.test.com/res')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))

task = {"summary": "Take out trash", "description": "" }
resp = requests.post('https://todolist.example.com/tasks/', json=task)
if resp.status_code != 201:
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))

resp = requests.post('https://todolist.example.com/tasks/', json=task)

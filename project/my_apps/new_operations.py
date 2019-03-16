import requests

def _url(path):
    return 'https://todo.example.com' + path

class Operations:
    
    def get_tasks(self):
        return requests.get(_url('/tasks/'))    #To get reuest for particular asset of task

    def add_task(self, summary, description=""):  #send data for task in json format
        return requests.post(_url('/tasks/'), json={
            'summary': summary,
            'description': description,
            })

    def task_done(self, task_id): #Delete request to particulat asset
        return requests.delete(_url('/tasks/{:d}/'.format(task_id)))

    def update_task(self, task_id, summary, description): #update using put request
        url = _url('/tasks/{:d}/'.format(task_id))
        return requests.put(url, json={
            'summary': summary,
            'description': description,
            })
import requests
from dotenv import load_dotenv
import os


class ProjectYouGile:
    def __init__(self, url):
        self.url = url
        load_dotenv()

    def create_new_project(self, title, user_id):
        url = f'{self.url}/projects'
        key = os.getenv('API_KEY')
        token = f'Bearer {key}'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }
        data = {
            "title": title,
            "users": {user_id: 'admin'}
        }
        response = requests.post(url, headers=headers, json=data)
        status_code = response.status_code
        project = response.json()
        return status_code, project

    def change_new_project(self, id_project, title2, user_id):
        url = f'{self.url}/projects/{id_project}'
        key = os.getenv('API_KEY')
        token = f'Bearer {key}'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }
        data = {'title': title2, 'users': {user_id: "admin"}
                }
        response = requests.put(url, headers=headers, json=data)
        status_code = response.status_code
        new_project = response.json()
        return status_code, new_project

    def get_new_project(self, id_project):
        url = f'{self.url}/projects/{id_project}'
        key = os.getenv('API_KEY')
        token = f'Bearer {key}'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }
        response = requests.get(url, headers=headers)
        status_code = response.status_code
        project_id = response.json()
        return status_code, project_id

    def delete_project(self, id_project):
        url = f'{self.url}/projects/{id_project}'
        key = os.getenv('API_KEY')
        token = f'Bearer {key}'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }
        response = requests.delete(url, headers=headers)
        status_code = response.status_code
        det = response.json()
        return status_code, det

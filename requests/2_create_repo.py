import requests
from pprint import pprint


def create_repo(url):
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {auth}'
    }

    data = {
        'name': 'repo-created-with-api',
        'private': True,
        'has_wiki': False
    }

    response = requests.post(url, headers=headers, json=data)
    print(f"Response status code: {response.status_code}")
    return response.json()


if __name__ == '__main__':
    url = 'https://api.github.com/HelgaMark/repos'
    auth = '' # my generated authorization token

    repo = create_repo(url)
    pprint(repo)
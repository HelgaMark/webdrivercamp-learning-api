import requests

def update_repo(url):
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        'authorization': f'Bearer {auth}'
    }

    data = {
        'description':  'I know Python Requests!'
    }

    response = requests.patch(url,headers=headers,json=data)
    print(f"Response status code: {response.status_code}")
    return response.json()


if __name__ == '__main__':
    url = 'https://api.github.com/repos/HelgaMark/repo-created-with-api'
    auth = ''  # my generated authorization token

    repo = update_repo(url)
    assert repo['description'] == 'I know Python Requests!'


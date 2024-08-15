import requests


def get_created_repo(url):
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f'Bearer {auth}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repo = response.json()

        assert repo['has_wiki'] == False
        assert repo['private'] == True
        assert repo['name'] == 'repo-created-with-api'
        assert repo['owner']['login'] == 'HelgaMark'

        print(f"Response status code: {response.status_code}")
        return repo
    else:
        print(f"Failed to get repo. Status code: {response.status_code}")
        return None


if __name__ == "__main__":
    url = "https://api.github.com/repos/HelgaMark/repo-created-with-api"
    auth = '' # my generated authorization token
    repo = get_created_repo(url)

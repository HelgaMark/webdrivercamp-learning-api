import requests

def delete_repo(url):
    headers = {
        'Accept': '"application/json',
        'Authorization': f'Bearer {auth}'
    }

    response = requests.delete(url,headers=headers)
    print(f"Response status code: {response.status_code}")
    return response.json()


if __name__ == "__main__":
    url = f'https://api.github.com/repos/HelgaMark/repo-created-with-api'
    auth = ''  # my generated authorization token
    delete_repo(url)

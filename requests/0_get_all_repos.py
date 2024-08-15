import requests


def get_repos(url):
    response = requests.get(url)
    print(f"Response status code: {response.status_code}")

    data = response.json()

    print(f"Total count of found items: {data['total_count']}")
    return data['items']


if __name__ == "__main__":
    url = 'https://api.github.com/search/repositories?q=webdrivercamp-learning-python'
    list_of_items = get_repos(url)
    print()

    for item in list_of_items:
        user = item['owner']['login']
        repo = item['name']

        print(f"{user:15}", repo)

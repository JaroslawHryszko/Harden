import requests
import subprocess
import os

# Constants
GITHUB_TOKEN = 'your_github_personal_access_token'  # Your GitHub personal access token
BASE_PATH = '/path/to/save/repositories'  # Where to save the cloned repositories
SEARCH_CRITERIA = {
    'language': 'Python',
    'stars': '>=100',
    'sort': 'updated',  # Sort by recently updated
    'order': 'desc'
}
SEARCH_URL = 'https://api.github.com/search/repositories'

def search_github_repositories():
    """Search for repositories on GitHub based on predefined criteria."""
    query = f'language:{SEARCH_CRITERIA["language"]} stars:{SEARCH_CRITERIA["stars"]}'
    params = {
        'q': query,
        'sort': SEARCH_CRITERIA['sort'],
        'order': SEARCH_CRITERIA['order']
    }
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(SEARCH_URL, headers=headers, params=params)
    response.raise_for_status()  # Will raise an exception for HTTP error codes
    return response.json()['items']

def clone_repository(repo_url):
    """Clone a GitHub repository to the specified local path."""
    repo_name = repo_url.split('/')[-1]
    local_path = os.path.join(BASE_PATH, repo_name)
    subprocess.run(['git', 'clone', repo_url, local_path], check=True)
    return local_path

def main():
    # Step 1: Search for repositories
    repositories = search_github_repositories()
    if not repositories:
        print("No repositories found matching the criteria.")
        return
    
    # Step 2: Clone the first suitable repository
    repo_url = repositories[0]['clone_url']  # Use the first repository
    local_repo_path = clone_repository(repo_url)
    print(f'Repository cloned to {local_repo_path}')
    
    # Step 3: Run the harden.py script on the cloned repository
    os.environ['REPO_PATH'] = local_repo_path  # Assuming the other script uses REPO_PATH environment variable
    subprocess.run(['python', 'harden.py'], check=True)

if __name__ == '__main__':
    main()

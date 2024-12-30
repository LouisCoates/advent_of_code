import requests
import os

def download_data(url, session_cookie, output_path):
    headers = {
        'Cookie': f'session={session_cookie}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(output_path, 'w') as file:
            file.write(response.text)
        print(f"Data downloaded successfully and saved to {output_path}")
    else:
        print(f"Failed to download data. Status code: {response.status_code}")

if __name__ == "__main__":
    session_cookie = os.getenv('AOC_SESSION_COOKIE')  # Make sure to set this environment variable
    os.makedirs('data', exist_ok=True)    
    if session_cookie:
        for day in range(1, 26):
            url = "https://adventofcode.com/2024/day/{}/input".format(day)
            output_path = "data/day{}_input.txt".format(day)
            download_data(url, session_cookie, output_path)
    else:
        print("Session cookie not found. Please set the AOC_SESSION_COOKIE environment variable.")
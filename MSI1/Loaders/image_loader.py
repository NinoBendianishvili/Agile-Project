import requests

def fetch_image_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Check content type if needed: response.headers['Content-Type']
            return response.content
        else:
            print(f"Failed to fetch image: {response.status_code}")
    except Exception as e:
        print(f"Failed to fetch image: {str(e)}")

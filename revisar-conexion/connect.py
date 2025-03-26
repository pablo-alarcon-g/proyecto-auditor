import requests

def check_website_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return(True)
        else:
            return(False)
    except requests.exceptions.RequestException as e:
        return(False)

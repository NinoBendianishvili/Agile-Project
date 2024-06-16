import requests

def fetch_quote():
    url = 'https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        quote = data['quoteText']  # Access directly if the structure allows
        return quote
    except Exception as e:
        print(f"Failed to fetch quote: {str(e)}")
        return None

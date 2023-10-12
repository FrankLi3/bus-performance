import requests

def fetch_mbta_schedules(api_key, filters=None):
    base_url = ""https://api-v3.mbta.com/schedules""
    headers = {
        "x-api-key": "353b7541b2fa4b089132b0ae5bb90890"  # Your API key should be passed here
    }
    
    params = {}
    if filters:
        params["filter"] = filters

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Use the function
api_key = "353b7541b2fa4b089132b0ae5bb90890"  # Replace with your actual API key
data = fetch_mbta_schedules(api_key)

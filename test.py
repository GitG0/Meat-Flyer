import requests

def scrape_data(url):
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the content of the response (HTML or JSON data)
            print(response.text)
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Example usage: scrape data from a specific URL
    target_url = "https://api.com"
    scrape_data(target_url)



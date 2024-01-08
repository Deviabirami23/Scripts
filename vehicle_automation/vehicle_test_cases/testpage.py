import requests
from bs4 import BeautifulSoup

url = "https://demo.parivahaneye.com"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('div',id='root')

    if not links:
        print("No links found on the page.")
    else:
        for link in links:
            print(link)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

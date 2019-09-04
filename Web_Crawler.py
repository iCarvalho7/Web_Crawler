import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

photos = ['http://manauaratech.com.br']
visits = set()

def acessImg(url, visits):
	html = requests.get(url).text
	html_bs = BeautifulSoup(html, 'html.parser')
	news = []

	for img in html_bs.find_all("img"):
		src = img.get("src")

		if src is None: 
			continue
		
		full_url = urljoin(url, src)

		if full_url in visits:
			continue

		news.append(full_url)
	return news
try:
	while photos:
		to_visit = photos.pop()
		visits.add(to_visit)
		print(f"Acessing: {to_visit}")
		news = acessImg(to_visit,visits)
		photos += news
except Exception as error:
	print(f"Problem: {error}")
pass
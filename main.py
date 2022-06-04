import pickle, sys
from GoogleNews import GoogleNews
from bs4 import BeautifulSoup
from urllib.request import urlopen


# returns a BeautifulSoup object from a URL
def get_soup(link):
	url = link
	page = urlopen(url)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")

	# extract direct link IF source URL is from Google News
	soup_split = soup.get_text().split()
	if(soup_split[0] == 'Google' and soup_split[1] == 'News'):
		for word in soup_split:
			if "http" in word and "CloseSearchClear" in word:
				return get_soup(word.replace("CloseSearchClear", ""))

	# else return original
	return soup


# get news links of a "Search Term" from Google News
def get_news(search_term):
	try:
		with open(search_term, 'rb') as file:
			return pickle.load(file)
	except:
		googlenews = GoogleNews(period='1d', encode='utf-8')
		googlenews.get_news(search_term)

		Recursion_Limit = 0

		# save search results to disk for later use
		while True:
			Recursion_Limit += 1000
			sys.setrecursionlimit(Recursion_Limit)
			try:
				with open(search_term, 'wb') as file:
					pickle.dump(googlenews, file)
				break
			except:
				pass

		print("Success at Limit: " +str(Recursion_Limit))		
		return googlenews
		

# search = 'bitcoin'
# googlenews = get_news(search)


url = "https://news.google.com/./articles/CAIiEAVez1rX28izq9CLKm3JUGQqMwgEKioIACIQVUfMNPchx9tcFFSwReSP7CoUCAoiEFVHzDT3IcfbXBRUsEXkj-wwkeKnBw?uo=CAUiemh0dHBzOi8vd3d3LmNvaW5kZXNrLmNvbS9idXNpbmVzcy8yMDIyLzA2LzAzL21pZGRsZS1lYXN0LW9pbC1wcm9kdWNlcnMtbW92ZS1pbnRvLWJpdGNvaW4tbWluaW5nLXdpdGgtY3J1c29lLWVuZ"

soup = get_soup(url)
print(soup.get_text())























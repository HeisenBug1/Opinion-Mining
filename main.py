import pickle, sys
from GoogleNews import GoogleNews
from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_soup(link):
	url = link
	page = urlopen(url)
	html = page.read().decode("utf-8")
	soup = BeautifulSoup(html, "html.parser")

	soup_split = soup.get_text().split()
	if(soup_split[0] == 'Google' and soup_split[1] == 'News'):
		for word in soup_split:
			if "http" in word and "CloseSearchClear" in word:
				return get_soup(word.replace("CloseSearchClear", ""))
	return soup


def initialize(search):
	try:
		with open(search, 'rb') as file:
			return pickle.load(file)
	except:
		googlenews = GoogleNews(period='1d', encode='utf-8')
		googlenews.get_news(search)

		Recursion_Limit = 0

		while True:
			Recursion_Limit += 1000
			sys.setrecursionlimit(Recursion_Limit)
			try:
				with open(search, 'wb') as file:
					pickle.dump(googlenews, file)
				break
			except:
				pass

		print("Success at Limit: " +str(Recursion_Limit))		
		return googlenews
		

# print (sys.getrecursionlimit())

# print (sys.getrecursionlimit())

search = 'bitcoin'
# googlenews = initialize(search)


# with open(search, 'rb') as file:
# 	googlenews = pickle.load(file)

# print(googlenews.get_links())

# for link in googlenews.get_links():
# 	print(link)

# for title in googlenews.get_texts():
# 	print(title)

# print(googlenews.total_count())

# i = 1
# st = ""
# for res in googlenews.results():
# 	# st += str(i) +" "
# 	# st += res['site'] +": "+ res['title'] +"\n"
# 	st += res['title'] +": "+ res['link'] +"\n"
# 	# i += 1

# print(st)


url = "https://news.google.com/./articles/CAIiEAVez1rX28izq9CLKm3JUGQqMwgEKioIACIQVUfMNPchx9tcFFSwReSP7CoUCAoiEFVHzDT3IcfbXBRUsEXkj-wwkeKnBw?uo=CAUiemh0dHBzOi8vd3d3LmNvaW5kZXNrLmNvbS9idXNpbmVzcy8yMDIyLzA2LzAzL21pZGRsZS1lYXN0LW9pbC1wcm9kdWNlcnMtbW92ZS1pbnRvLWJpdGNvaW4tbWluaW5nLXdpdGgtY3J1c29lLWVuZ"

soup = get_soup(url)
print(soup.get_text())























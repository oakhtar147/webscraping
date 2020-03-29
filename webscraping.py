import requests
from bs4 import BeautifulSoup
from pprint import pprint

def create_url_soup(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'lxml')
	return soup


def extract_prices(soup, div_list):
	unlockers = [unlocker.h2.text.strip() for unlocker in div_list] # finding a tag by the id the tag has 
	return unlockers
	

def get_bundle(soup, divs):
	spans = []

	for div in divs:
		books = div.find_all('span', class_='front-page-art-image-text') # list containing names of all the books in bundles
		bundle = []
		for book in books:
			bundle.append(book.text)
		spans.append(', '.join(bundle))	

	return spans	

def info_dict(prices, bundles):

	tiers = {
			'tier1': {

					'price': prices[0],
					'books': []
			},
		

			'tier2': {
					
					'price': prices[1],
					'books': []

			},


			'tier3': {
					
					'price': prices[2],
					'books': []

		}
}

	for i, key in enumerate(tiers.keys()):
		tiers[key]['books'].append(bundles[i])

	return tiers	


# print(pprint(tiers, sort_dicts=False))	

url_soup = create_url_soup('https://www.humblebundle.com/books/tech-job-for-dummies-2-books?hmb_source=humble_home&hmb_medium=product_tile&hmb_campaign=mosaic_section_2_layout_index_2_layout_type_twos_tile_index_1_c_landatechjob2_bookbundle')

div_list = url_soup.find_all('div', class_='main-content-row dd-game-row js-nav-row')
divs = url_soup.find_all('div', class_='main-content-row dd-game-row js-nav-row')

prices = extract_prices(url_soup, div_list)
bundles = get_bundle(url_soup, divs)
info   = info_dict(prices, bundles)
print(pprint(info, sort_dicts=False))


## bs4 basics

# print(len(soup.find_all('p')))	# find all basically returns the a list containing all the tags of p, there are 7 p tags in this url

# print(soup.prettify()) # this prints out the whole markup 

# print(soup.a['class']) # this prints out the first a tag that it finds

# print(soup.find(class_='navbar-item logo-navbar-item desktop')) # finding the first tag by the class the tag has 


## #




# front_page_texts = [span.text for span in soup.find_all('span', class_='front-page-art-image-text')]

# # front_page_texts = [span.text for span in front_page_texts]
# print(front_page_texts)

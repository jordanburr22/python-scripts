#! /usr/bin/env python3

import bs4, requests

def getAmazonPrice(productUrl):
	res = requests.get(productUrl)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text)
	elems = soup.select('#price_inside_buybox')
	return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.com/Scraper-Stainless-Polished-Measuring-Multipurpose/dp/B01D1GE1KE')
print('The price is ' + price)

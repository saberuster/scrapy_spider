import requests

from scrapy.selector import Selector

r = requests.get('http://www.yw11.com/html/mi/3-6-1-1.htm')
r.encoding = 'UTF-8'

s = Selector(text=r.text)

print(s.css('.listbox1_text ul li::text').extract_first().strip())

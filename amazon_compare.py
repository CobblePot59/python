import requests
from lxml import html

search = input("Enter your object name: ")
page=requests.get('https://www.amazon.com/s?k='+search)

tree = html.fromstring(page.content)

product_list=tree.xpath('//*[@class="a-size-medium a-color-base a-text-normal"]/text()')
p1=tree.xpath('//*[@class="a-price-whole"]/text()')
p2=tree.xpath('//*[@class="a-price-fraction"]/text()')
price_list=[]
for x,y in zip(p1,p2):
	a=x+','+y
	price_list.append(a)

for i in range(1,len(product_list)):
	print(product_list[i])
	print(price_list[i])

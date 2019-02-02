# scrapy_tripadvisor
Get hotels' info from the city you choose by using the scrapy python framework

1- INTRODUCTION
Scrapy is a python framework for web scraping. In other words, it allows us to get info from the website we want.
In this case, we are extracting information about hotels from several cities (Madrid, Barcelona, Seville and Berlin). 
The software can be easily modified to get info from other cities by creating new spiders.

2- REQUIREMENTS
  - Python 3.0 and upwards. To download it visit: https://www.python.org/downloads/
  - Scrapy: Visit https://scrapy.org/ or type on your terminal 'pip install scrapy'
  
3- GETTING INFORMATION FROM THE WEB
In order to retrieve data from any site, we need analyze the html and CSS structure of the site. 
In order to do that and test our code, we will use the scrapy shell:
'scrapy shell' can be typed in the terminal to open it.

  3.1- OPEN THE PAGE YOU WANT TO SCRAPE
  We need to type the following command to load the page we are going to be working with:
  fetch('https://www.tripadvisor.com/Hotels-g187497-Barcelona_Catalonia-Hotels.html')
  
  Type 'View(response)' or 'print(response.text)' to check if it loaded successfully.
  
  3.2- EXTRACTING INFO USING XPATH
  Xpath is a query language to select nodes in an HTML or XML document. In order to learn how to use it, visit the following tutorial:
  https://www.w3schools.com/xml/xpath_intro.asp
  
  In this case, we used the following command to get the name of each hotel:
  response.xpath('//a[@class="review_count"]/text()').extract()

4- CREATING SPIDERS:
In order to automatize the informatin extraction, we need to create spiders using the following commands:
  - Firstly, we need to create a project: 'scrapy startproject tripadvisor'
  - Secondly, we can create each spider: 'scrapy genspider tripadvisor_barcelona https://www.tripadvisor.com/Hotels-g187497-Barcelona_Catalonia-Hotels.html'

5- RUNNING THE SPIDERS
We need to launch the scrapper by typing this command: 'scrapy crawl tripadvisor_barcelona'

6- EXPORTING THE DATA AS A CSV FILE:
This script exxports the data as a csv file. In order to set it, we just needed to modify two variables in the settings.py file:
  - FEED_FORMAT='csv'
  - FEED_URI= '%(time)s_%(name)s.csv'




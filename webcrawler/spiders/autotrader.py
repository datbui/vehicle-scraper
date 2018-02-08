import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError, TCPTimedOutError

from webcrawler.items import Vehicle

DOMAIN = "www.autotrader.com"

ROOT_PATH = 'https://www.autotrader.com%s'

NEXT_PAGE_SELECTOR = 'ul.pagination > li:nth-last-child(2) > .pagination-link'

MAPPING = {'Exterior': 'exterior', 'Interior': 'interior', 'Drive Type': 'drive', 'Fuel': 'fuel', 'Engine': 'engine', 'Transmission': 'transmission', 'VIN': 'vin', 'MPG': 'mpg', 'Mileage': 'mileage'}


class AutotraderSpider(scrapy.Spider):
    name = "autotrader"
    start_urls = [
        'https://www.autotrader.com/cars-for-sale/Used+Cars/Acura/Whitewater+WI-53190?zip=53190&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=ACURA&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/mazda/Whitewater+WI-53190?zip=53190&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=MAZDA&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/honda/Whitewater+WI-53190?zip=53190&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=HONDA&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/nissan/Whitewater+WI-53190?zip=53190&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=NISSAN&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/toyota/Whitewater+WI-53190?zip=53190&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=TOYOTA&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/lexus/Whitewater+WI-53190?zip=53190&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=LEXUS&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/hyundai/Whitewater+WI-53190?zip=53190&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=HYUNDAI&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/kia/Whitewater+WI-53190?zip=53190&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=KIA&searchRadius=25',
        #
        'https://www.autotrader.com/cars-for-sale/Used+Cars/Acura/Madison+WI-53701?zip=53701&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=ACURA&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/mazda/Madison+WI-53701?zip=53701&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=MAZDA&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/honda/Madison+WI-53701?zip=53701&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=HONDA&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/nissan/Madison+WI-53701?zip=53701&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=NISSAN&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/toyota/Madison+WI-53701?zip=53701&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=TOYOTA&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/lexus/Madison+WI-53701?zip=53701&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=LEXUS&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/hyundai/Madison+WI-53701?zip=53701&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=HYUNDAI&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/kia/Madison+WI-53701?zip=53701&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=ACURA&searchRadius=25',
        #
        'https://www.autotrader.com/cars-for-sale/Used+Cars/Acura/Milwaukee+WI-53201?zip=53201&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=ACURA&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/mazda/Milwaukee+WI-53201?zip=53201&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=MAZDA&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/honda/Milwaukee+WI-53201?zip=53201&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=HONDA&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/nissan/Milwaukee+WI-53201?zip=53201&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=NISSAN&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/toyota/Milwaukee+WI-53201?zip=53201&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=TOYOTA&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/lexus/Milwaukee+WI-53201?zip=53201&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=LEXUS&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/hyundai/Milwaukee+WI-53201?zip=53201&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=HYUNDAI&searchRadius=25',
        'https://www.autotrader.com/cars-for-sale/Used+Cars/kia/Milwaukee+WI-53201?zip=53201&listingTypes=used&startYear=2006&filterName=LISTING_TYPES&numRecords=100&sortBy=derivedpriceASC&firstRecord=0&endYear=2014&makeCodeList=KIA&searchRadius=25'
    ]

    allowed_domains = [DOMAIN]

    def parse(self, response):
        if response.status != 404:
            self.logger.info('Processing ... %s' % response.url)
            cars = response.css('.container:nth-child(2) a.text-md')
            self.logger.info("Founded cars %s", len(cars))
            for car in cars:
                a = car.css('::attr(href)').extract_first()
                url = ROOT_PATH % a
                self.logger.debug("url  %s", url)
                title = car.css('strong::text').extract_first()
                item = Vehicle()
                item['name'] = title
                self.logger.debug("name  %s", title)
                title = title.split(' ', 3)
                item['url'] = url
                year = title[1]
                item['year'] = year
                self.logger.debug("year  %s", year)
                make = title[2]
                item['make'] = make
                self.logger.debug("make  %s", make)
                model = title[3]
                item['model'] = model
                self.logger.debug("model  %s", model)
                yield item
                request = scrapy.Request(response.urljoin(url), callback=self.parse_details, errback=self.errback_httpbin)
                request.meta['item'] = item
                yield request
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield scrapy.Request(response.urljoin(next_page), callback=self.parse, errback=self.errback_httpbin)

    def parse_details(self, response):
        item = response.meta['item']
        self.logger.info("Visited %s", response.url)
        item['price'] = response.css('span[data-qaid=cntnr-lstng-price1] strong::text').extract_first()
        self.logger.debug("price %s", item['price'])
        location = response.css('span[itemprop=addressLocality]').extract_first()
        if location:
            location = location.replace('<span itemprop="addressLocality"> <!-- -->', '').replace('</span>', '')
        item['location'] = location
        self.logger.debug("location %s", location)
        exterior = response.css('div[data-qaid=cntnr-exteriorColor] strong::text').extract_first()
        item['exterior'] = exterior
        self.logger.debug("exterior %s", exterior)
        interior = response.css('div[data-qaid=cntnr-interiorColor] strong::text').extract_first()
        item['interior'] = interior
        self.logger.debug("interior %s", interior)

        overview = response.css('div.table-responsive tr')
        for prop in overview:
            key = prop.css('.text-gray::text').extract_first()
            value = prop.css('td:nth-child(2) > span > span::text').extract_first()
            value = prop.css('td:nth-child(2)::text').extract_first() if not value else value
            self.logger.debug("prop %s  %s", key, value)
            key = MAPPING.get(key)
            if key:
                item[key.lower()] = value
        yield item

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

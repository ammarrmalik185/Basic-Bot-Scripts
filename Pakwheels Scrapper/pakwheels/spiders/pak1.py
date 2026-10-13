import scrapy


class CarAdData:
    ref_no = ""
    name = ""
    price = ""
    year = ""
    location = ""
    mileage = ""
    register_city = ""
    engine_type = ""
    capacity = ""
    transmission = ""
    color = ""
    assembly = ""
    body_type = ""
    features = ""
    updated = ""
    url = ""

    def getString(self):
        
        return ('"' + str(self.ref_no) + '","' + str(self.name) + '","' + str(self.price) + '","' + str(self.year) + '","' \
               + str(self.location) + '","' + str(self.mileage) + '","' + str(self.register_city) + '","' + str(self.engine_type) + '","' \
               + str(self.capacity) + '","' + str(self.transmission) + '","' + str(self.color) + '","' + str(self.assembly) + '","' \
               + str(self.body_type) + '","' + str(self.features) + '","' + str(self.updated) + '","' +str(self.url) + '"').replace("\n", "\\n") + "\n"


class Pak1Spider(scrapy.Spider):
    name = 'pak1'
    allowed_domains = ['pakwheels.com']
    start_urls = ['https://www.pakwheels.com/used-cars/search/-/']

    csv_string = "Ad No,Name,Price,Model Year,Location,Mileage,Registered City,Engine Type,Engine Capacity,Transmission,Color,Assembly,Body Type,Features,Last Updated,URL\n"
    file_path = "./test.csv"
    curr_count = 0
    page_count = 50

    def parse(self, response):
        urls = response.xpath('//div[@class="search-title"]/a/@href').extract()
        for url in urls:
            comp_url = 'https://www.pakwheels.com' + url
            yield scrapy.Request(comp_url, callback=self.parse_car)

        # Next Page
        next_page = response.xpath('//li[@class="next_page"]/a/@href').extract_first()
        if next_page:
            self.curr_count += 1
            if self.curr_count < self.page_count:
                comp_url = 'https://www.pakwheels.com' + next_page
                yield scrapy.Request(comp_url, callback=self.parse)



    def parse_car(self, response):

        # Name tag of AD
        name = response.xpath('//h1/text()').extract_first()

        url = response.request.url
        # Price
        price = response.xpath('//div[@class="price-box"]/strong/text()').extract_first()
        unit = response.xpath('//div[@class="price-box"]/strong/span/text()').extract_first()
        if (unit == 'lacs'):
            price = float(price.strip().split('PKR')[1]) * 100000
        elif (unit == 'crore'):
            price = float(price.strip().split('PKR')[1]) * 10000000

        # Model Year
        year = response.xpath('//span[@class="engine-icon year"]/../p/a/text()').extract_first()

        # Ad Location
        location = response.xpath('//p[@class="detail-sub-heading"]/a/text()').extract_first()

        # mileage
        mileage = response.xpath('//span[@class="engine-icon millage"]/../p/text()').extract_first()
        mileage = int(mileage.replace('km', '').replace(',', ''))

        # Engine Type
        engine_type = response.xpath('//span[@class="engine-icon type"]/../p/a/text()').extract_first()

        # Transmission
        transmission = response.xpath('//span[@class="engine-icon transmission"]/../p/a/text()').extract_first()
        if (transmission is None):
            transmission = response.xpath('//span[@class="engine-icon transmission"]/../p/text()').extract_first()

            # Registered City
        register_city = response.xpath(
            "//*[contains(text(),'Registered City')]/following-sibling::li/text()").extract_first()

        # Color
        color = response.xpath("//*[contains(text(),'Color')]/following-sibling::li/text()").extract_first()

        # Assembly
        assembly = response.xpath("//*[contains(text(),'Assembly')]/following-sibling::li/a/text()").extract_first()
        if (assembly != 'Local') and (assembly != 'Imported'):
            assembly = response.xpath("//*[contains(text(),'Assembly')]/following-sibling::li/text()").extract_first()

            # Body Type
        body_type = response.xpath("//*[contains(text(),'Body Type')]/following-sibling::li/a/text()").extract_first()

        # Engine Capacity 
        capacity = response.xpath(
            "//*[contains(text(),'Engine Capacity')]/following-sibling::li/text()").extract_first()

        # last updated
        updated = response.xpath("//*[contains(text(),'Last Updated')]/following-sibling::li/text()").extract_first()

        # Refrence Number
        ref_no = response.xpath("//*[contains(text(),'Ad Ref #')]/following-sibling::li/text()").extract_first()

        # Feature List
        features = response.xpath('//ul[@class="list-unstyled car-feature-list nomargin"]/li/text()').extract()
        features = ','.join(features)

        new_data = CarAdData()
        new_data.ref_no = ref_no
        new_data.name = name
        new_data.price = price
        new_data.year = year
        new_data.location = location
        new_data.mileage = mileage
        new_data.register_city = register_city
        new_data.engine_type = engine_type
        new_data.capacity = capacity
        new_data.transmission = transmission
        new_data.color = color
        new_data.assembly = assembly
        new_data.body_type = body_type
        new_data.features = features
        new_data.updated = updated
        new_data.url = url

        self.csv_string += new_data.getString()

        with open(self.file_path, "w") as f:
            f.write(self.csv_string)

        yield None

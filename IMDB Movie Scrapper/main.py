from selenium import webdriver

url = "https://www.imdb.com/list/ls079111388/"

driver = webdriver.Edge()
driver.get(url)
movie_containers = driver.find_elements_by_class_name("mode-detail")

print(len(movie_containers))

for i in range(len(movie_containers)):
    name = movie_containers[i].find_element_by_class_name("lister-item-header").find_element_by_tag_name("a").text
    year = movie_containers[i].find_element_by_class_name("lister-item-header").find_element_by_class_name("lister-item-year").text
    print(name + " - " + year)

driver.close()

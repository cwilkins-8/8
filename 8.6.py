#8.6 City Names
 #Write a function called city_country() that takes in the name
 #a city and its country. The function should return a string formatted like this:

def city_country (city, country):
    return (city.title() + ", " + country.title())

city = city_country('manchester', 'england')
print(city)

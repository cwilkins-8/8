#8.3 Write a function called make_shirt() that accepts a size and the
#text of a message that should be printed on the shirt. The function should print
#a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional argume

def make_shirt(size, message):
    print("Please can I have a Manchester City shirt size " + size + " printing " + message + " on the back")

make_shirt('large', 'bronze')
make_shirt('large', 'I love Python')

#8.5 Cities: Write a function called describe_city() that accepts the name of
#a city and its country. The function should print a simple sentence, such as
#Reykjavik is in Iceland. Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the
#default country

def describe_city(city, country):
    print(city + "is in the country " + country)

describe_city(city='Reykjavik', country='Iceland')

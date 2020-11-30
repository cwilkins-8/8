#8.9 Magicians Make a list of magician’s names. Pass the list to a function
#called show_magicians(), which prints the name of each magician in the list.

def show_magicians(magicians):
    for magician in magicians:
        print(magician)



#8.10 Great Magicians: Start with a copy of your program from Exercise 8-9.
#Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to
#see that the list has actually been modified.

def make_great(magicians):
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)
        
magicians = ['taylor swift' ' lucy bronze' ' david beckham']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)

#8.12 Sandwiches

def make_sandwich(*items):
    print("I'll make you a sandwich:")
    for item in items:
        print("I will add " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('beef', 'cheese', 'lettuce')
make_sandwich('ham', 'beetroot')
make_sandwich('peanut butter', 'jam')

# Python classes review graded

### Problem 1:
# Create a Movie class with the following properties/attributes: ```movieName```, ```rating```, and ```yearReleased```.
# * Override the default ```str``` (to-String) method and implement the code that will print the value of all the properties/attributes of the Movie class
# * In your ```main``` function create *two* instances of the Product class
#     * Assign a value of your choosing for each property/attribute
#     * Print all properties to the console.
# Remember, this is the basic model of a Python file with a class
# ```
# class Movie:
#     def __init__(self):
#     # Class constructor code and property handling
#     OTHER PROPERTIES AND METHODS HERE
# def main():
# Create class instance(s) and perform other activities in/from this function
# }
#
# main()
# ```
# Movie Class
class Movie:
    # Setup properties
    def __init__(self, movieName, rating, yearReleased):
        # properties created
        self.movieName_p = movieName
        self.rating_p = rating
        self.yearReleased = yearReleased
    # set up the string overwitting function
    def __str__(self):
        return f'my movie is {self.movieName_p}\n the rating is: {self.rating_p}\n and it was released {self.yearReleased}\n'
# Create function to call class
def main():
    #inputting attributes to the class
    myMovie = Movie('James Bond', 'R', '2000')
    myMovie2 = Movie('Jerry McGuire', 'A', '1998')
    #print class with product information
    print(myMovie, myMovie2)
# Call function
main()


### Problem 2:
# Create a class Product that represents a product sold online.
# A Product has ```price```, ```quantity``` and ```name``` properties/attributes.
# * Override the default ```str``` (to-String) method and implement the code that will print the value of all the properties/attributes of the Product class
# * In your ```main``` function create *two* instances of the Product class
#     * Assign a value of your choosing for each property/attribute
#     * Print all properties to the console.

# Class: product class
class Product:
    #setup the properties
    def __init__(self,price, quantity, name):
        #properties created
        self.price = price
        self.qty = quantity
        self.name = name
    # set up the string overwitting function
    def __str__(self):
        return f'The price is: {self.price}\n Qty: {self.qty}\n Name: {self.name}\n'
# Create function to call class
def main2():
    #inputting attributes to the class
    product1=Product(17,37,'Buns')
    product2=Product(24,96,'Shoe Laces')
    #print class with product information
    print(product1,product2)
# Call function
main2()
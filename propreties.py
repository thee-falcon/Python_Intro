class Product:
    def __init__(self, price) -> None:
        print("constructor")
        self.price = price # calls the sitter here, @price.sitter method because price is a proprety

    @property
    def price(self):
        print("geter")
        return self.__price

    @price.setter
    def price(self, value):
        print("seter")
        if (value < 0):
            raise ValueError("Price cannot be negative.")
        self.__price = value

# initialization
product = Product(32)
product.price = -1 # this will throw an exception, because is negative and will update the value of price using setter method
# accessing price, when you access product.price, python calls the @proprety method (getter)
print(product.price)

class Customer:
    allCustomers = []

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.reviews = []
        Customer.allCustomers.append(self)

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    @classmethod
    def all(cls):
        return cls.allCustomers

    def reviewedRestaurants(self):
        return list({review.getRestaurant() for review in self.reviews})

    def writeReview(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self.reviews.append(review)
        restaurant.receiveReview(review)

    def totalReviews(self):
        return len(self.reviews)

    @classmethod
    def findByName(cls, name):
        return next((customer for customer in cls.allCustomers if customer.fullName() == name), None)

    @classmethod
    def findAllByFirstName(cls, firstName):
        return [customer for customer in cls.allCustomers if customer.getFirstName() == firstName]


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def getName(self):
        return self.name

    def getReviews(self):
        return self.reviews

    def averageRating(self):
        if not self.reviews:
            return 0.0
        totalRating = sum(review.getRating() for review in self.reviews)
        return totalRating / len(self.reviews)

    def customers(self):
        return list({review.getCustomer() for review in self.reviews})

    def receiveReview(self, review):
        self.reviews.append(review)


class Review:
    allReviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.allReviews.append(self)

    def getRating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.allReviews

    def getCustomer(self):
        return self.customer

    def getRestaurant(self):
        return self.restaurant


customer1 = Customer("Makmende", "Izbak")
customer2 = Customer("Kadinal", "Mutuku")

restaurant1 = Restaurant("Sweet Indulgence Foods")
restaurant2 = Restaurant("Kale Heaven")

customer1.writeReview(restaurant1, 5)
customer1.writeReview(restaurant2, 4)

customer2.writeReview(restaurant1, 4)
customer2.writeReview(restaurant2, 5)

print("Average rating for Sweet Indulgence Foods:", restaurant1.averageRating())
print("Average rating for Kale Heaven:", restaurant2.averageRating())

print("All customers:")
for customer in Customer.all():
    print(customer.fullName())

print("Customers who reviewed Sweet Indulgence Foods:")
for customer in restaurant1.customers():
    print(customer.fullName())

for customer in restaurant2.customers():
    print(customer.fullName())

print("Customers with first name 'Makmende':")
for customer in Customer.findAllByFirstName("Makmende"):
    print(customer.fullName())

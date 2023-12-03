# Define the Customer class
class Customer:
    all_customers = []  # A list to store all customer instances

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []  # A list to store reviews associated with this customer
        Customer.all_customers.append(self)  # Add the instance to the list

     # Methods to access customer attributes
    def get_given_name(self):
        return self.given_name

    def get_family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"    
    
    # Class method to get all customer instances
    @classmethod
    def all(cls):
        return cls.all_customers
    
    # Method to associate a review with this customer
    def add_review(self, review):
        self.reviews.append(review)
        
    def get_reviews(self):
        return self.reviews

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name == name]



# Define the Restaurant class
class Restaurant:
    all_restaurants = []  # A list to store all restaurant instances

    def __init__(self, name):
        self.restaurant_name = name
        self.restaurant_reviews = []  # A list to store reviews associated with this restaurant
        Restaurant.all_restaurants.append(self)  # Add the instance to the list

    # Method to get the restaurant name
    def get_name(self):
        return self.restaurant_name
    
     # Method to associate a review with this restaurant
    def add_review(self, review):
        self.restaurant_reviews.append(review)

     # Method to get all reviews associated with this restaurant
    def get_reviews(self):
        return self.restaurant_reviews
    
    # Method to get all customers who reviewed this restaurant
    def get_customers(self):
        return [review.customer for review in self.restaurant_reviews]
    
    # Method to calculate average star rating of the restaurant
    def average_star_rating(self):
        total_ratings = sum([review.rating for review in self.restaurant_reviews])
        num_ratings = len(self.restaurant_reviews)
        if num_ratings == 0:
            return 0
        return total_ratings / num_ratings
    
# Define the Review class
class Review:
    all_reviews = []  # A list to store all review instances

    def __init__(self, customer, restaurant, rating_value):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating_value
        Review.all_reviews.append(self)  # Add the instance to the list
        customer.add_review(self)  # Associate the review with the customer
        restaurant.add_review(self)  # Associate the review with the restaurant

    # Method to get the rating of the review
    def get_rating(self):
        return self.rating
    
    # Class method to get all review instances
    @classmethod
    def all(cls):
        return cls.all_reviews
    
    # Method to get the customer associated with the review
    def get_customer(self):
        return self.customer
    
    # Method to get the restaurant associated with the review
    def get_restaurant(self):
        return self.restaurant


#Usage
if __name__ == "__main__":
    # Create instances of customers, restaurants, and reviews
    customer1 = Customer("Kennedy", "Rotich")
    customer2 = Customer("Maingi", "Layersonn")
    
    restaurant1 = Restaurant("Prestige Grill")
    restaurant2 = Restaurant("Choma Grill")
    
    review1 = Review(customer1, restaurant1, 4)
    review2 = Review(customer2, restaurant1, 5)
    review3 = Review(customer1, restaurant2, 3)


    # Print usage and deliverables
    print(customer1.full_name())
    print(restaurant1.get_name())
    print(review1.get_rating())
    print(Review.all())
    print(restaurant1.get_customers())
    print(customer1.get_reviews())
    print(customer1.num_reviews())
    found_customer = Customer.find_by_name("Kennedy Rotich")
    if found_customer:
        print("Found:", found_customer.full_name())
    else:
        print("Customer not found")
        
    customers_with_given_name = Customer.find_all_by_given_name("Maingi")
    print("Customers with given name Maingi:", [customer.full_name() for customer in customers_with_given_name])

    print(restaurant1.average_star_rating())
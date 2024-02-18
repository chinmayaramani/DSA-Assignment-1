import time
import random

class Product:
    def __init__(self, product_id, name, price, category):
        # Initialize a product with provided attributes
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        # String representation of the product
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Category: {self.category}"

class ProductManager:
    def __init__(self):
        # Initialize ProductManager with an empty list of products
        self._products = []

    def load_data(self, file_path):
        try:
            # Load product data from a file and populate the list of products
            with open(file_path, 'r') as file:
                for line in file:
                    data = line.strip().split(', ')
                    product = Product(int(data[0]), data[1], float(data[2]), data[3])
                    self._products.append(product)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def display_products(self):
        # Display all products in the list
        for product in self._products:
            print(product)

    def insert_product(self, product):
        # Add a new product to the list
        self._products.append(product)

    def update_product(self, product_id, new_price):
        # Update the price of a product with a specific ID
        for product in self._products:
            if product.product_id == product_id:
                product.price = new_price
                break

    def delete_product(self, product_id):
        # Delete a product with a specific ID from the list
        if any(product.product_id == product_id for product in self._products):
            self._products = [product for product in self._products if product.product_id != product_id]
            print("Product deleted successfully.")
        else:
            print(f"No product found with ID {product_id}.")

    def search_product(self, key, value):
        # Search for products based on a specific attribute and its value
        results = []
        for product in self._products:
            try:
                if hasattr(product, key):
                    attribute_value = getattr(product, key)
                    if str(attribute_value).lower() == str(value).lower():
                        results.append(product)
            except AttributeError:
                print(f"Invalid search key: {key}")
        return results

    def bubble_sort(self, data):
        # Bubble sort implementation to sort products by price
        n = len(data)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if data[j].price > data[j + 1].price:
                    data[j], data[j + 1] = data[j + 1], data[j]

    def analyze_sorting_complexity(self, data, algorithm='bubble'):
        # Analyze the sorting complexity using different scenarios
        print(f"\nAnalyzing Sorting Complexity ({algorithm} Sort):")

        # Measure time for sorting already sorted data
        start_time_sorted = time.time()
        self.bubble_sort(data)
        end_time_sorted = time.time()
        elapsed_time_sorted = end_time_sorted - start_time_sorted
        print(f"Time taken to sort already sorted data: {elapsed_time_sorted:.6f} seconds")

        # Shuffle the data for random order
        random.shuffle(data)

        # Measure time for sorting data in reverse order
        start_time_reverse = time.time()
        self.bubble_sort(data)
        end_time_reverse = time.time()
        elapsed_time_reverse = end_time_reverse - start_time_reverse
        print(f"Time taken to sort data in reverse order: {elapsed_time_reverse:.6f} seconds")

    def sort_products_by_price(self, algorithm='bubble'):
        # Sort the list of products by price using a specified sorting algorithm
        start_time_random = time.time()
        self.bubble_sort(self._products)
        end_time_random = time.time()
        elapsed_time_random = end_time_random - start_time_random
        print(f"Time taken to sort random data: {elapsed_time_random:.6f} seconds")

    def generate_sorted_data(self, size):
        # Generate sorted data for testing
        return [Product(i, f"Product {i}", random.uniform(1, 1000), f"Category {i}") for i in range(1, size + 1)]

    def generate_reverse_sorted_data(self, size):
        # Generate reverse sorted data for testing
        return [Product(i, f"Product {i}", random.uniform(1, 1000), f"Category {i}") for i in range(size, 0, -1)]

    def generate_test_datasets(self, size):
        # Generate random, sorted, and reverse-sorted datasets for testing
        random_data = [Product(i, f"Product {i}", random.uniform(1, 1000), f"Category {i}") for i in range(1, size + 1)]
        sorted_data = self.generate_sorted_data(size)
        reverse_sorted_data = self.generate_reverse_sorted_data(size)
        return random_data, sorted_data, reverse_sorted_data

if __name__ == "__main__":
    # Instantiate ProductManager
    manager = ProductManager()
    file_path = "product_data.txt"  
    manager.load_data(file_path)

    # Size for generating test data
    test_size = 1000

    # Generate datasets for testing
    random_data, sorted_data, reverse_sorted_data = manager.generate_test_datasets(test_size)

    # Analyze sorting complexity for all datasets
    manager.analyze_sorting_complexity(random_data)
    manager.analyze_sorting_complexity(sorted_data)
    manager.analyze_sorting_complexity(reverse_sorted_data)

    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Display Products")
        print("2. Insert Product")
        print("3. Update Product Price")
        print("4. Delete Product")
        print("5. Search Products")
        print("6. Sort Products by Price (Bubble Sort)")
        print("7. Exit")

        # Accept user input
        choice = input("Enter your choice: ")

        if choice == '1':
            # Display all products
            print("\nDisplaying Products:")
            manager.display_products()

        elif choice == '2':
            # Insert a new product
            try:
                product_id = int(input("Enter Product ID: "))
                name = input("Enter Product Name: ")
                price = float(input("Enter Product Price: "))
                category = input("Enter Product Category: ")
                new_product = Product(product_id, name, price, category)
                manager.insert_product(new_product)
                print("Product added successfully.")
            except ValueError:
                print("Invalid input. Please enter numeric values for Product ID and Price.")

        elif choice == '3':
            # Update product price
            try:
                product_id = int(input("Enter Product ID to update price: "))
                new_price = float(input("Enter New Price: "))
                manager.update_product(product_id, new_price)
                print("Product price updated successfully.")
            except ValueError:
                print("Invalid input. Please enter numeric values for Product ID and New Price.")

        elif choice == '4':
            # Delete a product
            try:
                product_id = int(input("Enter Product ID to delete: "))
                manager.delete_product(product_id)
            except ValueError:
                print("Invalid input. Please enter numeric values for Product ID.")

        elif choice == '5':
            # Search for products based on a specified attribute and value
            search_key = input("Enter Search Key (e.g., Name): ").lower()
            search_value = input(f"Enter {search_key.capitalize()} to search: ")
            search_results = manager.search_product(search_key, search_value)
            if search_results:
                print("\nSearch Results:")
                for result in search_results:
                    print(result)
            else:
                print("No matching products found.")

        elif choice == '6':
            # Sort products by price using bubble sort
            manager.sort_products_by_price()
            print("\nProducts Sorted by Price (Bubble Sort):")
            manager.display_products()

        elif choice == '7':
            # Exit the program
            print("Successfully exited the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

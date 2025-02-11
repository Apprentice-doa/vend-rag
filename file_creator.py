# import csv

# # List of product dictionaries with prices
# products = [
#     {"category": "Food", "sub-category": "Fruits", "product": "Apple", "price (USD)": 0.60},
#     {"category": "Food", "sub-category": "Fruits", "product": "Banana", "price (USD)": 0.30},
#     {"category": "Food", "sub-category": "Vegetables", "product": "Carrot", "price (USD)": 0.25},
#     {"category": "Food", "sub-category": "Vegetables", "product": "Broccoli", "price (USD)": 1.50},
#     {"category": "Food", "sub-category": "Grains", "product": "Rice (1 lb)", "price (USD)": 2.00},
#     {"category": "Food", "sub-category": "Grains", "product": "Quinoa (1 lb)", "price (USD)": 4.00},
#     {"category": "Food", "sub-category": "Proteins", "product": "Chicken Breast (1 lb)", "price (USD)": 5.50},
#     {"category": "Food", "sub-category": "Proteins", "product": "Tofu (14 oz)", "price (USD)": 2.00},
#     {"category": "Food", "sub-category": "Dairy", "product": "Milk (1 gallon)", "price (USD)": 3.99},
#     {"category": "Food", "sub-category": "Dairy", "product": "Cheddar Cheese (1 lb)", "price (USD)": 5.86},
#     {"category": "Drinks", "sub-category": "Soft Drinks", "product": "Coca-Cola (12 oz)", "price (USD)": 1.50},
#     {"category": "Drinks", "sub-category": "Soft Drinks", "product": "Pepsi (12 oz)", "price (USD)": 1.50},
#     {"category": "Drinks", "sub-category": "Juices", "product": "Orange Juice (1 gallon)", "price (USD)": 6.00},
#     {"category": "Drinks", "sub-category": "Juices", "product": "Apple Juice (1 gallon)", "price (USD)": 5.50},
#     {"category": "Drinks", "sub-category": "Tea", "product": "Green Tea (20 bags)", "price (USD)": 3.00},
#     {"category": "Drinks", "sub-category": "Tea", "product": "Black Tea (20 bags)", "price (USD)": 2.50},
#     {"category": "Drinks", "sub-category": "Coffee", "product": "Espresso (1 shot)", "price (USD)": 2.00},
#     {"category": "Drinks", "sub-category": "Coffee", "product": "Latte (12 oz)", "price (USD)": 4.00},
#     {"category": "Drinks", "sub-category": "Water", "product": "Evian Water (1.5 liters)", "price (USD)": 2.00},
#     {"category": "Drinks", "sub-category": "Water", "product": "Spring Water (1.5 liters)", "price (USD)": 1.00}
# ]

# # Specify the CSV file name
# csv_file = 'products.csv'

# # Write the data to the CSV file
# with open(csv_file, mode='w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=["category", "sub-category", "product", "price (USD)"])
#     writer.writeheader()
#     writer.writerows(products)

# print(f"CSV file '{csv_file}' has been created successfully.")


import pandas as pd

def product_order(user_name: str, products: list) -> pd.DataFrame:
    """
    Create a DataFrame with user name, product, and order status for each product in the list.

    Parameters:
    user_name (str): The name of the user placing the order.
    products (list): A list of product names.

    Returns:
    pd.DataFrame: DataFrame containing the order details.
    """
    # Initialize the order status
    order_status = "Pending"

    # Create a list of dictionaries, each representing an order
    orders = [{"user_name": user_name, "product": product, "order_status": order_status} for product in products]

    # Convert the list of dictionaries into a DataFrame
    orders_df = pd.DataFrame(orders)

    return orders_df

# Example usage:
user = "John Doe"
product_list = ["Apple", "Banana", "Carrot"]
order_df = product_order(user, product_list)
print(order_df)

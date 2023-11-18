import pandas as pd
pip install pandas
total_orders_by_customer = order_data.groupby('customer_id')['order_date'].count()
average_order_quantity_by_product = order_data.groupby('product_name')['order_quantity'].mean()
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()
print("1. Total orders by each customer:")
print(total_orders_by_customer)

print("\n2. Average order quantity for each product:")
print(average_order_quantity_by_product)

print("\n3. Earliest and latest order dates:")
print("Earliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)

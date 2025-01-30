
This repository leverages the NexusRaven model with Ollama to execute SQL queries through function calls.  
## Prompt
```
Function
def select_products_with_biggest_popularity_return_diff()

    Retrieve products with the largest absolute difference between popularity 
    index and return rate from the database.

    Returns:
        list: A list of tuples representing the selected records, where each  
        tuple corresponds to a row in the result set.

Function
def select_top_supplier_for_standard_shipping()

    Retrieve the supplier who has shipped the most products via the standard
    shipping method.

    Returns:
        list: A list of tuples representing the supplier(s) with the highest
        number of products shipped using the standard shipping method. Each tuple
        contains a record for the supplier and the total number of products shipped.

Function
def select_most_popular_category()

    Retrieve the category with the highest number of sells within a specific
    popularity index range from the database.

    Returns:
        tuple: A tuple representing the category with the most products in the
        specified popularity range, or None if no data is found.

Function
def select_top_supplier_by_net_profit()

    Retrieve the supplier with the highest net profit after consideration of tax and discount
    from the database.

    Returns:
        list: A list of tuples representing the supplier(s) with the highest
        net profit. Each tuple contains a record for the supplier's net profit.

User Query: Who has the highest profit?<human_end>
```
## Response
```select_top_supplier_by_net_profit()```

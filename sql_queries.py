
__all__ = [
    "biggest_popularity_return_difference_query", 
           "most_popular_category_query",
           'top_supplier_for_standard_shipping_query',
           'top_supplier_by_net_profit_query'
           ]

biggest_popularity_return_difference_query = """
SELECT 
    "Product Name",
    ABS("Popularity Index" - "Return Rate") AS abs_difference
FROM 
    purchase
ORDER BY 
    abs_difference DESC
LIMIT 5;
"""

most_popular_category_query = """
SELECT 
    "Category",
    COUNT(*) AS total_sales
FROM 
    purchase
WHERE 
    "Popularity Index" BETWEEN 50 AND 70
GROUP BY 
    "Category"
ORDER BY 
    total_sales DESC
LIMIT 1;
"""

top_supplier_for_standard_shipping_query = """
SELECT 
    "Supplier ID",
    COUNT(*) AS total_standard_shipments
FROM 
    purchase
WHERE 
    "Shipping Method" = 'Standard'
GROUP BY 
    "Supplier ID"
ORDER BY 
    total_standard_shipments DESC
LIMIT 1;
"""
top_supplier_by_net_profit_query = """
SELECT 
    "Supplier ID",
    SUM(("Price" - ("Price" * "Discount" / 100)) * (1 - "Tax Rate" / 100)) AS net_profit
FROM 
    your_table_name
GROUP BY 
    "Supplier ID"
ORDER BY 
    net_profit DESC
LIMIT 1;
"""


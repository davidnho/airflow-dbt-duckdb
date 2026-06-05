select
    order_id,
    customer_id,
    product,
    quantity,
    price,
    quantity * price as total_amount,
    order_date
from bronze_sales
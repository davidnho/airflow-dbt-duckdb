select
    product,
    count(*) as total_orders,
    sum(quantity) as total_qty,
    sum(total_amount) as total_sales
from {{ ref('stg_sales') }}
group by product
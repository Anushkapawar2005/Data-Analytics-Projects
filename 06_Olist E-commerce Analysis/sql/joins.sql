use olist;
show tables;
DESCRIBE olist_orders_dataset;
SELECT * FROM olist_orders_dataset LIMIT 10;
SELECT DISTINCT order_status FROM olist_orders_dataset;
SELECT COUNT(*) FROM olist_orders_dataset;
desc olist_orders_dataset;
select order_status,count(*) as total_count from olist_orders_dataset group by order_status;
SELECT 
    p.product_category_name, t.product_category_name_english
FROM
    olist_products_dataset p
        INNER JOIN
    product_category_name_translation t ON p.product_category_name = t.product_category_name
LIMIT 10;


SELECT
    c.customer_state,
    SUM(oi.price) AS Total_Revenue

FROM olist_customers_dataset c

INNER JOIN olist_orders_dataset o
ON c.customer_id = o.customer_id

INNER JOIN olist_order_items_dataset oi
ON o.order_id = oi.order_id

GROUP BY c.customer_state

ORDER BY Total_Revenue DESC;


select order_id, order_status,
case 
when order_status = 'delivered' then 'Completed'
else 'not completed'
end as order_result
from olist_orders_dataset LIMIT 10;



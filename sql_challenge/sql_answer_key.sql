SELECT SUM(revenue) AS total_revenue, SUM(profit) AS total_profit FROM order_details;

SELECT substr(o.order_date,1,7) AS month, SUM(od.revenue) AS revenue FROM orders o JOIN order_details od ON o.order_id=od.order_id GROUP BY month ORDER BY month;

SELECT p.product_name, SUM(od.revenue) AS revenue FROM order_details od JOIN products p ON od.product_id=p.product_id GROUP BY p.product_name ORDER BY revenue DESC LIMIT 10;

SELECT o.region, SUM(od.revenue) AS revenue, SUM(t.target_revenue) AS target_revenue FROM orders o JOIN order_details od ON o.order_id=od.order_id JOIN sales_targets t ON substr(o.order_date,1,7)=t.month AND o.region=t.region GROUP BY o.region;

SELECT o.sales_channel, SUM(od.profit)*1.0/SUM(od.revenue) AS profit_margin FROM orders o JOIN order_details od ON o.order_id=od.order_id GROUP BY o.sales_channel;

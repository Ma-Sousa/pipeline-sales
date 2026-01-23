-- Total sold
SELECT SUM(total_amount) AS total_sales
FROM sales;

-- Sales by month
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(total_amount) AS total_sales
FROM sales
GROUP BY 1
ORDER BY 1;

-- Top products
SELECT product,
       SUM(total_amount) AS total_sales
FROM sales
GROUP BY product
ORDER BY total_sales DESC;

-- Sales by category
SELECT category,
       SUM(total_amount) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;

-- Average ticket per order
SELECT AVG(total_amount) AS avg_ticket
FROM sales;

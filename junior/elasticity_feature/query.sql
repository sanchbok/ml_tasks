select sku, dates, avg(price) as price, count(price) as qty
from transactions
group by sku, dates
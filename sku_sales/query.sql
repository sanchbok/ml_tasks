select cal_date as days, sum(cnt) as sku
from transactions_another_one
group by 1
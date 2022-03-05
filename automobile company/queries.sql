-- Queries

-- Find the top 2 brands by dollar-amount sold in the past year.

select b.brand_name, sum(o.price) s
from deal d,
     vehicle v,
     option o,
     model m,
     brand b
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and text(d.date) like '2021%'
group by b.brand_name order by s desc limit 2;

-- Find the top 2 brands by unit sales in the past year.

select b.brand_name, count(b.brand_name) c
from deal d,
     vehicle v,
     option o,
     model m,
     brand b
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and text(d.date) like '2021%'
group by b.brand_name order by c desc limit 2;


-- Find those dealers who keep a vehicle in inventory for the longest average time

select de.dealer_id, de.dealer_name, avg(d.date - v.date) avg_time
from vehicle v,
     deal d,
     dealer de
where v.vin = d.vin
  and v.dealer_id = de.dealer_id
group by de.dealer_id
order by avg_time desc;

-- Show sales trends for various brands over the past 3 years, by year, month, week. Then break
-- these data out by gender of the buyer and then by income range.

-- 3 years

select m.brand_name, m.model_name, count(m.model_name) c
from deal d,
     vehicle v,
     option o,
     model m,
     brand b
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and (text(d.date) like '2019%' or text(d.date) like '2020%' or text(d.date) like '2021%')
group by m.model_name
order by m.brand_name desc, c desc;


-- 1 year

select m.brand_name, m.model_name, count(m.model_name) c
from deal d,
     vehicle v,
     option o,
     model m,
     brand b
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and text(d.date) like '2021%'
group by m.model_name
order by m.brand_name desc, c desc;

-- 1 month

select m.brand_name, m.model_name, count(m.model_name) c
from deal d,
     vehicle v,
     option o,
     model m,
     brand b
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and text(d.date) like '2021-12%'
group by m.model_name
order by m.brand_name desc, c desc;


-- 1 week

select m.brand_name, m.model_name, count(m.model_name) c
from deal d,
     vehicle v,
     option o,
     model m,
     brand b
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and d.date between '2021-11-29 00:00:00.614060' and '2021-12-05 00:00:00.614060'
group by m.model_name
order by m.brand_name desc, c desc;


-- 3 years, gender

select m.brand_name, m.model_name, count(m.model_name) count, c.gender
from deal d,
     vehicle v,
     option o,
     model m,
     brand b,
     customer c
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and d.customer_id = c.customer_id
  and (text(d.date) like '2019%' or text(d.date) like '2020%' or text(d.date) like '2021%')
group by m.model_name, c.gender
order by m.brand_name desc, count desc;

-- 1 year, gender

select m.brand_name, m.model_name, count(m.model_name) count, c.gender
from deal d,
     vehicle v,
     option o,
     model m,
     brand b,
     customer c
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and d.customer_id = c.customer_id
  and text(d.date) like '2021%'
group by m.model_name, c.gender
order by m.brand_name desc, count desc;

-- 1 month, gender

select m.brand_name, m.model_name, count(m.model_name) count, c.gender
from deal d,
     vehicle v,
     option o,
     model m,
     brand b,
     customer c
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and d.customer_id = c.customer_id
  and text(d.date) like '2021-12%'
group by m.model_name, c.gender
order by m.brand_name desc, count desc;

-- 1 week, gender

select m.brand_name, m.model_name, count(m.model_name) count, c.gender
from deal d,
     vehicle v,
     option o,
     model m,
     brand b,
     customer c
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and d.customer_id = c.customer_id
  and d.date between '2021-11-29 00:00:00.614060' and '2021-12-05 00:00:00.614060'
group by m.model_name, c.gender
order by m.brand_name desc, count desc;

-- 3 years, annual income

select m.brand_name, m.model_name, count(m.model_name) count, c.annual_income
from deal d,
     vehicle v,
     option o,
     model m,
     brand b,
     customer c
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and d.customer_id = c.customer_id
  and (text(d.date) like '2019%' or text(d.date) like '2020%' or text(d.date) like '2021%')
group by m.model_name, c.annual_income
order by m.brand_name desc, count desc;

-- 1 year, annual income

select m.brand_name, m.model_name, count(m.model_name) count, c.annual_income
from deal d,
     vehicle v,
     option o,
     model m,
     brand b,
     customer c
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and d.customer_id = c.customer_id
  and text(d.date) like '2021%'
group by m.model_name, c.annual_income
order by m.brand_name desc, count desc;

-- 1 month, annual income

select m.brand_name, m.model_name, count(m.model_name) count, c.annual_income
from deal d,
     vehicle v,
     option o,
     model m,
     brand b,
     customer c
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and d.customer_id = c.customer_id
  and text(d.date) like '2021-12%'
group by m.model_name, c.annual_income
order by m.brand_name desc, count desc;

-- 1 week, annual income

select m.brand_name, m.model_name, count(m.model_name) count, c.annual_income
from deal d,
     vehicle v,
     option o,
     model m,
     brand b,
     customer c
where d.vin = v.vin
  and v.option_id = o.option_id
  and o.model_name = m.model_name
  and m.brand_name = b.brand_name
  and d.customer_id = c.customer_id
  and d.date between '2021-11-29 00:00:00.614060' and '2021-12-05 00:00:00.614060'
group by m.model_name, c.annual_income
order by m.brand_name desc, count desc;
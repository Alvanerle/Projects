create table company(
    company_name text PRIMARY KEY,
    country text NOT NULL
);

create table brand(
    brand_name text PRIMARY KEY,
    company_name text references company
);

create table model(
    model_name text PRIMARY KEY,
    brand_name text references brand
);

create table option(
    option_ID serial PRIMARY KEY,
    model_name text references model,
    color text NOT NULL,
    engine text NOT NULL,
    transmission text NOT NULL,
    price double precision check (price > 0) NOT NULL
);

create table dealer(
    dealer_ID serial PRIMARY KEY,
    dealer_name text NOT NULL,
    phone_number text NOT NULL,
    address text NOT NULL
);

create table vehicle(
    VIN serial PRIMARY KEY,
    date timestamp NOT NULL,
    option_ID serial references option,
    dealer_ID serial references dealer
);

create table customer(
    customer_ID serial PRIMARY KEY,
    customer_name text NOT NULL,
    phone_number text NOT NULL,
    gender varchar(1) NOT NULL,
    annual_income double precision NOT NULL
);

create table deal(
    VIN serial PRIMARY KEY references vehicle,
    date timestamp NOT NULL,
    customer_ID serial references customer
);

create index idx1 on deal(vin, customer_id);
create index idx2 on vehicle(vin, dealer_id);
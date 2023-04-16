drop database if exists umag_hacknu;
create database umag_hacknu;

CREATE TABLE umag_hacknu.sale
(
    id SERIAL PRIMARY KEY,
    barcode BIGINT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    price INT NOT NULL DEFAULT 0,
    sale_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE umag_hacknu.supply
(
    id SERIAL PRIMARY KEY,
    barcode BIGINT NOT NULL,
    quantity INT NOT NULL DEFAULT 1,
    price INT NOT NULL DEFAULT 0,
    supply_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX supply_barcode_time_idx ON umag_hacknu.supply (barcode, supply_time);
CREATE INDEX sale_barcode_time_idx ON umag_hacknu.sale (barcode, sale_time);
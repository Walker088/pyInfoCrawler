-- Create table types of data sources
CREATE TABLE IF NOT EXISTS public.types
(
    type_id character varying(3) NOT NULL,
    type_name character varying(40) NOT NULL,
    src text NOT NULL,
    PRIMARY KEY (type_id)
);
-- Sequence for department
CREATE SEQUENCE IF NOT EXISTS public.types_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 99
    CACHE 1;
ALTER SEQUENCE public.types_seq
    OWNER TO postgres;
COMMENT ON COLUMN public.types.type_id
    IS 'Format: T01 to T99';

-- Table for crawled records
CREATE TABLE IF NOT EXISTS public.crawled_records
(
    crawled_id character varying(10) NOT NULL,
    crawled_date date NOT NULL,
    source_type character varying(4) NOT NULL,
    crawled_at timestamp with time zone NOT NULL,
    PRIMARY KEY (crawled_id),
    FOREIGN KEY (source_type) REFERENCES types (type_id)
);
ALTER TABLE public.crawled_records
    OWNER to postgres;

-- Sequence for suspicious patients
CREATE SEQUENCE IF NOT EXISTS public.crawled_records_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 999999999
    CACHE 1;
ALTER SEQUENCE public.crawled_records_seq
    OWNER TO postgres;

COMMENT ON COLUMN public.crawled_records.crawled_id
    IS 'Format: C000000001 to C999999999';
COMMENT ON COLUMN public.crawled_records.crawled_date
    IS 'Day of a record be crawled. Format: YYYY/MM/DD';
COMMENT ON COLUMN public.crawled_records.source_type
    IS 'The data source type, relates to table types';

-- Insert default types
INSERT INTO public.types (
    type_id,
    type_name,
    src
)
VALUES(
    CONCAT('T0', nextval('types_seq')),
    'infocasa-alquiler',
    'https://www.infocasas.com.py/alquiler'
);

INSERT INTO public.types (
    type_id,
    type_name,
    src
)
VALUES(
    CONCAT('T0', nextval('types_seq')),
    'infocasa-venta',
    'https://www.infocasas.com.py/venta'
);
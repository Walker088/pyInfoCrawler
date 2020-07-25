-- Create table departamento for properties from infocasa.com.py
CREATE TABLE IF NOT EXISTS public.property_department
(
    department_id character varying(4),
    department_name character varying(40),
    infocasa_country_id integer,
    infocasa_dep_id integer,
    PRIMARY KEY (department_id)
);
ALTER TABLE public.property_department
    OWNER to postgres;
-- Sequence for department
CREATE SEQUENCE IF NOT EXISTS public.property_department_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 999
    CACHE 1;
ALTER SEQUENCE public.property_department_seq
    OWNER TO postgres;


-- Create table barrio for properties from infocasa.com.py
CREATE TABLE IF NOT EXISTS public.property_district
(
    department_id character varying(4),
    district_id character varying(4),
    district_name character varying(40),
    PRIMARY KEY (department_id, district_id)
);
ALTER TABLE public.property_district
    OWNER to postgres;
-- Sequence for district
CREATE SEQUENCE IF NOT EXISTS public.property_district_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 999
    CACHE 1;
ALTER SEQUENCE public.property_district_seq
    OWNER TO postgres;
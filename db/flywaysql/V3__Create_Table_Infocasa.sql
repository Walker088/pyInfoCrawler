-- Table of source infocasa
CREATE TABLE IF NOT EXISTS public.infocasa_alquiler
(
    crawled_id character varying(10) NOT NULL,
    property_id character varying(10) NOT NULL,
    property_name text NOT NULL,
    department_id character varying(4),
    district_id character varying(4),
    price integer,
    currency character varying(10),
    nroom text,
    nbath text,
    property_type text,
    property_state text,
    build_at smallint,
    area_meter integer,
    url text,
    PRIMARY KEY (crawled_id, property_id),
    FOREIGN KEY (crawled_id) REFERENCES crawled_records (crawled_id)
);

ALTER TABLE public.infocasa_alquiler
    OWNER to postgres;

COMMENT ON COLUMN public.infocasa_alquiler.crawled_id
    IS 'Relates to public.crawled_records.crawled_id';
COMMENT ON COLUMN public.infocasa_alquiler.property_id
    IS 'Crawled from infocasa';
COMMENT ON COLUMN public.infocasa_alquiler.department_id
    IS 'Relates to table property_rdepartment';
COMMENT ON COLUMN public.infocasa_alquiler.district_id
    IS 'Relates to table property_district';
COMMENT ON COLUMN public.infocasa_alquiler.nroom
    IS 'Number of rooms in a property';
COMMENT ON COLUMN public.infocasa_alquiler.nbath
    IS 'Number of bathrooms in a property';

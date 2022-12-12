-- Active: 1653768796327@@127.0.0.1@3306
-- Database: home_deco

-- DROP DATABASE IF EXISTS home_deco;

CREATE DATABASE home_deco
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Argentina.1252'
    LC_CTYPE = 'Spanish_Argentina.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE home_deco
    IS 'Base de datos para el prouyecto grupal Django Codo a Codo 2022';
    
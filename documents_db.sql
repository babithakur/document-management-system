--
-- PostgreSQL database dump
--

-- Dumped from database version 15.10 (Debian 15.10-0+deb12u1)
-- Dumped by pg_dump version 15.10 (Debian 15.10-0+deb12u1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: pdf_documents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pdf_documents (
    id integer NOT NULL,
    title text NOT NULL,
    author text,
    keywords text[],
    summary text,
    created_at timestamp without time zone DEFAULT (CURRENT_TIMESTAMP AT TIME ZONE 'Asia/Kathmandu'::text),
    filename text
);


ALTER TABLE public.pdf_documents OWNER TO postgres;

--
-- Name: pdf_documents_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pdf_documents_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pdf_documents_id_seq OWNER TO postgres;

--
-- Name: pdf_documents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pdf_documents_id_seq OWNED BY public.pdf_documents.id;


--
-- Name: pdf_documents id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pdf_documents ALTER COLUMN id SET DEFAULT nextval('public.pdf_documents_id_seq'::regclass);


--
-- Data for Name: pdf_documents; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pdf_documents (id, title, author, keywords, summary, created_at, filename) FROM stdin;
11	Goat	Babi Thakur	{goat,"domestic animal",cute}	None	2025-08-16 14:41:29.369647	goat.pdf
12	Python	Babi Thakur	{python,programming}	None	2025-08-16 14:41:55.891319	python.pdf
13	Healthy Lifestyle	Mehazabien	{health,lifestyle,healthy}	None	2025-08-16 15:53:16.013622	healthy_lifestyle.pdf
14	Flowers	Jasmine	{flowers,nature}	None	2025-08-16 15:53:40.92137	flowers.pdf
15	Ethical Hacking	Roshan	{security,hacking,tech}	None	2025-08-16 15:54:00.810174	ethical_hacking.pdf
16	Java	Simran	{"java programming"}	None	2025-08-16 15:36:00	java.pdf
19	Microsoft Word - Unit -4 Android Activity.docx	Unknown	{None}	None	2025-08-16 16:08:02.600922	Unit -4 Android Activity.pdf
21	Microsoft Word - Unit -7 Advanced Android Concepts.docx	Unknown	{None}	None	2025-08-16 16:10:41.770349	Unit -7 Advanced Android Concepts.pdf
23	Microsoft Word - Unit -2 Introduction to Android Programming.docx	Unknown	{None}	None	2025-08-16 19:29:53.940409	Unit -2 Introduction to Android Programming.pdf
24	Unknown	LENOVO	{None}	None	2025-08-16 19:34:28.492522	Lab 2025 Update Lab 1.pdf
\.


--
-- Name: pdf_documents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pdf_documents_id_seq', 24, true);


--
-- Name: pdf_documents pdf_documents_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pdf_documents
    ADD CONSTRAINT pdf_documents_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--


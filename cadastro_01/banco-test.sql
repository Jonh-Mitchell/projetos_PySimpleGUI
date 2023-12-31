PGDMP     ,    !                {            aula_30_08_2023    13.11    13.11     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16968    aula_30_08_2023    DATABASE     o   CREATE DATABASE aula_30_08_2023 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE aula_30_08_2023;
                postgres    false            �            1259    16974    city    TABLE     H   CREATE TABLE public.city (
    cidade character varying(10) NOT NULL
);
    DROP TABLE public.city;
       public         heap    postgres    false            �            1259    16969    clientes    TABLE     �   CREATE TABLE public.clientes (
    nome character varying(40) NOT NULL,
    tipo character varying(5) NOT NULL,
    adimplente character varying(5) NOT NULL,
    cidade character varying(10) NOT NULL
);
    DROP TABLE public.clientes;
       public         heap    postgres    false            �          0    16974    city 
   TABLE DATA           &   COPY public.city (cidade) FROM stdin;
    public          postgres    false    201   �       �          0    16969    clientes 
   TABLE DATA           B   COPY public.clientes (nome, tipo, adimplente, cidade) FROM stdin;
    public          postgres    false    200   �       (           2606    16978    city cidades_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.city
    ADD CONSTRAINT cidades_pkey PRIMARY KEY (cidade);
 ;   ALTER TABLE ONLY public.city DROP CONSTRAINT cidades_pkey;
       public            postgres    false    201            %           2606    16973    clientes clientes_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT clientes_pkey PRIMARY KEY (nome);
 @   ALTER TABLE ONLY public.clientes DROP CONSTRAINT clientes_pkey;
       public            postgres    false    200            &           1259    16984 
   fki_cidade    INDEX     A   CREATE INDEX fki_cidade ON public.clientes USING btree (cidade);
    DROP INDEX public.fki_cidade;
       public            postgres    false    200            )           2606    16979    clientes cidade    FK CONSTRAINT     z   ALTER TABLE ONLY public.clientes
    ADD CONSTRAINT cidade FOREIGN KEY (cidade) REFERENCES public.city(cidade) NOT VALID;
 9   ALTER TABLE ONLY public.clientes DROP CONSTRAINT cidade;
       public          postgres    false    2856    200    201            �      x��MLN�<���7�(59#1�+F��� dO      �   [   x�KI� 7N�������ɩ��7sy��%�d$�qxq{�r�&�&g$�pe�H�K�0��*����d
�����b�b��0�=... �s9     
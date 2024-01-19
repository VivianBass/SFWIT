from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    lastname1 = models.CharField(max_length=45)
    lastname2 = models.CharField(max_length=45, null=True)
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=128)
    profile_picture = models.CharField(max_length=255, null=True)
    birthdate = models.DateField()
    creation_date = models.DateField()
    update_date = models.DateField(null=True)


class Address_cat(models.Model):
    """
    Modelo que contiene todos los códigos postales con la información de dirección.

    Atributos:

    - id: Identificador de la dirección (primary_key)
    - d_codigo: Código de la dirección
    - d_asenta: Asentamiento de la dirección
    - d_tipo_asenta: Tipo de asentamiento
    - D_mnpio: Municipio
    - d_estado: Estado
    - d_ciudad: Ciudad
    - d_CP: Código postal
    - c_estado: Estado (código)
    - c_oficina: Oficina
    - c_CP: Código postal (código)
    - c_tipo_asenta: Tipo de asentamiento (código)
    - c_mnpio: Municipio (código)
    - id_asenta_cpcons: Identificador de asentamiento y código postal
    - d_zona: Zona
    - c_cve_ciudad: Clave de la ciudad (código)
    """

    id = models.CharField(max_length=200, primary_key=True)
    d_codigo = models.CharField(max_length=100)
    d_asenta = models.CharField(max_length=100)
    d_tipo_asenta = models.CharField(max_length=100)
    D_mnpio = models.CharField(max_length=100)
    d_estado = models.CharField(max_length=100)
    d_ciudad = models.CharField(max_length=100)
    d_CP = models.CharField(max_length=100)
    c_estado = models.CharField(max_length=100)
    c_oficina = models.CharField(max_length=100)
    c_CP = models.CharField(max_length=100)
    c_tipo_asenta = models.CharField(max_length=100)
    c_mnpio = models.CharField(max_length=100)
    id_asenta_cpcons = models.CharField(max_length=100)
    d_zona = models.CharField(max_length=100)
    c_cve_ciudad = models.CharField(max_length=100)

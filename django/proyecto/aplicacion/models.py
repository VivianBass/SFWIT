from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    lastname1 = models.CharField(max_length=45)
    lastname2 = models.CharField(max_length=45, null=True)
    username = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    profile_picture = models.CharField(max_length=255, null=True)
    birthdate = models.DateField()
    creation_date = models.DateTimeField()
    update_date = models.DateTimeField(null=True)
    role = models.ForeignKey('User_role', on_delete=models.RESTRICT, db_column='role_id')

class User_role(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=45)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=45) 

class Place(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    category = models.ForeignKey('Category', on_delete=models.RESTRICT, db_column='category_id')
    description = models.CharField(max_length=250)

class Picture(models.Model):
    id = models.AutoField(primary_key=True) 
    place = models.ForeignKey('Place', on_delete=models.RESTRICT, db_column='place_id')
    content = models.CharField(max_length=45)

class Review(models.Model):
    id = models.AutoField(primary_key=True)  
    user = models.ForeignKey('User', on_delete=models.RESTRICT, db_column='user_id')
    place = models.ForeignKey('Place', on_delete=models.RESTRICT, db_column='place_id')
    date = models.DateTimeField()
    comment = models.CharField(max_length=250) 
    score = models.FloatField()

class Rating(models.Model):
    id = models.AutoField(primary_key=True) 
    user = models.ForeignKey('User', on_delete=models.RESTRICT, db_column='user_id')
    date = models.DateTimeField()
    review = models.ForeignKey('Review', on_delete=models.RESTRICT, db_column='review_id')
    like = models.IntegerField()
    dislike = models.IntegerField()

class Address_place(models.Model):
    id = models.AutoField(primary_key=True) 
    place = models.ForeignKey('Place', on_delete=models.RESTRICT, db_column='place_id')
    country = models.CharField(max_length=45) 
    zip_code = models.IntegerField() 
    state = models.CharField(max_length=45) 
    region = models.CharField(max_length=45) 
    colony = models.CharField(max_length=45) 
    street = models.CharField(max_length=50) 
    ext_number = models.IntegerField() 
    int_number = models.IntegerField() 
    latitude = models.FloatField() 
    longitude = models.FloatField()

class Direccion_cat(models.Model):
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


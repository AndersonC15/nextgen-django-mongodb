from djongo import models

# Las demás tablas se mantienen porque sí usarán ORM si quieres
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100)

    class Meta:
        db_table = 'categoria'


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_marca = models.CharField(max_length=100)

    class Meta:
        db_table = 'marca'

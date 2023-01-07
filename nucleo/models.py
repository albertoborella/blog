from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre', unique=True)
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name='Categoría'
        verbose_name_plural='Categorías'
        ordering=['-created']

    def __str__(self):
        return self.name


class Etiqueta(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre', unique=True)
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name='Etiqueta'
        verbose_name_plural='Etiquetas'
        ordering=['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    bajada = models.TextField(verbose_name='Bajada')
    contenido = RichTextField(verbose_name='Contenido')
    imagen = models.ImageField(upload_to='post', verbose_name='Imagen', null=True, blank=True)
    publicado = models.BooleanField(default=False, verbose_name='Publicado')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Categoría')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Autor')
    etiquetas = models.ManyToManyField(Etiqueta)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name='Publicación'
        verbose_name_plural='Publicaciones'
        ordering=['titulo']

    def __str__(self):
        return self.titulo

class About(models.Model):
    descripcion = RichTextField(verbose_name='Descripción')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name='Acerca de'
        verbose_name_plural='Acerca de nosotros'
        ordering=['-created']

    def __str__(self):
        return self.descripcion


#Redes Sociales
class Link(models.Model):
    key = models.CharField(max_length=100, verbose_name='Key Link')
    nombre = models.CharField(max_length=100, verbose_name='Red Social')
    url = models.URLField(max_length=100, verbose_name='Enlace',blank=True,null=True)
    icono = models.CharField(max_length=100, verbose_name='Icono')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name='Red Social'
        verbose_name_plural='Redes Sociales'
        ordering=['nombre']

    def __str__(self):
        return self.nombre
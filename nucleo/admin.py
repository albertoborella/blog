from django.contrib import admin
from .models import Categoria,Etiqueta,Post,About,Link
admin.site.site_header = 'Administración del Blog'
admin.site.index_title = 'Panel de Control'
admin.site.site_title = 'Blog'

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('name','active','created')

class EtiquetaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('name','active','created')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('titulo','categoria','publicado','autor' ,'created')
    ordering = ('autor','-created')
    search_fields = ('titulo','contenido','autor__username','categoria__name')
    list_filter = ('autor','categoria','etiquetas')

    # def post_etiquetas(self, obj):
    #     return ' - '.join([e.name for e in obj.etiquetas.all().order_by('name') ])

    # post_etiquetas_shortdescription = 'Etiquetas'

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('descripcion','created')

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('nombre','key','url','icono')



admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Etiqueta,EtiquetaAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Link,LinkAdmin)
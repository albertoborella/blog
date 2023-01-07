from .models import About,Link,Categoria,Post


def ctx_about(request):
    ctx_about = {}
    ctx_about['ABOUT'] = About.objects.latest('created')
    return ctx_about


def ctx_categorias(request):
    ctx_categorias = {}
    ctx_categorias['categorias'] = Categoria.objects.filter(active=True)
    return ctx_categorias


def ctx_link_redes(request):
    ctx_redes = {}
    redes = Link.objects.all()
    for link in redes:
        ctx_redes[link.key] = {'url':link.url, 'icono':link.icono}
    print(ctx_redes)
    return ctx_redes


def ctx_fechas(request):
    ctx_fechas = {}
    ctx_fechas['dates'] = Post.objects.dates('created', 'month', order='DESC').distinct()
    return ctx_fechas


from django.contrib import admin

from .models import DOCUMENTO, FORMA_PAGO, VENTA, REGION, LOCALIDAD, COMUNA, ENTREGA, CATEGORIA, TIPO_PRODUCTO, PRODUCTO, DETALLE, SUCURSAL


admin.site.register(DOCUMENTO)
admin.site.register(FORMA_PAGO)
admin.site.register(VENTA)
admin.site.register(REGION)
admin.site.register(LOCALIDAD)
admin.site.register(COMUNA)
admin.site.register(ENTREGA)
admin.site.register(CATEGORIA)
admin.site.register(TIPO_PRODUCTO)
admin.site.register(PRODUCTO)
admin.site.register(DETALLE)
admin.site.register(SUCURSAL)

# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db.models import Q
from django.core.mail import EmailMessage
from models import Proyecto, Peticion, Wiki, Documento, Archivo, Comentario

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre','slug',)
    search_fields = ['nombre','slug',]
    list_per_page = 25
    list_max_show_all = 30

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                'filebrowser/js/FB_TinyMCE.js',
                'filebrowser/js/TinyMCEAdmin.js',)

class WikiAdmin(admin.ModelAdmin):
    #list_display = ('proyecto',)
    list_per_page = 25
    list_max_show_all = 30

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                'filebrowser/js/FB_TinyMCE.js',
                'filebrowser/js/TinyMCEAdmin.js',)

class PeticionAdmin(admin.ModelAdmin):
    list_display = ('proyecto','asunto','creado_fecha','inicio_fecha','terminado_fecha','creado_por','estado','asignado_a','prioridad',)
    list_filter = ['estado','prioridad',]
    search_fields = ['asunto']
    list_per_page = 25
    list_max_show_all = 30

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                'filebrowser/js/FB_TinyMCE.js',
                'filebrowser/js/TinyMCEAdmin.js',)

    def save_model(self, request, obj, form, change):
        obj.save()
        asunto = u'%s - Petición #%s (%s) %s' % (obj.proyecto.nombre,obj.pk, obj.estado, obj.asunto)
        de, a = obj.creado_por.email, obj.asignado_a.email
        cuerpo = u'<p>Ticket #%s ha sido reportado por %s</p><h3>Petición #%s: %s</h3><ul><li>Autor: %s</li><li>Estado: %s</li><li>Prioridad: %s</li><li>Asignado a: %s</li></ul><p>%s</p>' % (obj.pk,obj.creado_por.username,obj.pk,obj.asunto,obj.creado_por.username,obj.estado,obj.prioridad,obj.asignado_a.username,obj.descripcion)
        msg = EmailMessage(asunto, cuerpo, de, [a])
        msg.content_subtype = "html"
        msg.send()

    def queryset(self, request):
        qs = super(PeticionAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(Q(asignado_a=request.user) | Q(creado_por=request.user))

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('proyecto','categoria','titulo',)
    list_per_page = 25
    list_max_show_all = 30

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                'filebrowser/js/FB_TinyMCE.js',
                'filebrowser/js/TinyMCEAdmin.js',)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor','peticion','fecha',)
    list_per_page = 25
    list_max_show_all = 30

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                'filebrowser/js/FB_TinyMCE.js',
                'filebrowser/js/TinyMCEAdmin.js',)

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Peticion, PeticionAdmin)
admin.site.register(Wiki, WikiAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Comentario, ComentarioAdmin)

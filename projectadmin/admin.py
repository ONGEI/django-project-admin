# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Projecto, Peticion, Wiki, Documento, Archivo, Comentario

#class PostAdmin(admin.ModelAdmin):
#    list_display = ('profile','title','date_posted','only_users')
#    list_filter = ['profile','date_posted','only_users','authorize']
#    search_fields = ['title','content']
#    list_per_page = 25
#    list_max_show_all = 30
#    date_hierarchy = 'date_posted'

#    class Media:
#        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
#                'filebrowser/js/FB_TinyMCE.js',
#                'filebrowser/js/TinyMCEAdmin.js',)

#    def save_model(self, request, obj, form, change):
#        if obj.pk is None:
#            obj.date_posted = datetime.datetime.today()
#            obj.profile = Profile.objects.get(user = request.user)
#        obj.save()

#    def queryset(self, request):
#        qs = super(PostAdmin, self).queryset(request)
#        if request.user.is_superuser:
#            return qs
#        return qs.filter(profile=Profile.objects.get(user = request.user))

#    def add_view(self, request, form_url='', extra_context=None):
#        self.fields = ('title','content','only_users','authorize') if request.user.is_superuser else ('title','content','only_users')
#        return super(PostAdmin, self).add_view(request, form_url, extra_context)

#    def change_view(self, request, object_id, extra_context=None):
#        self.fields = ('title','content','only_users','authorize') if request.user.is_superuser else ('title','content','only_users')
#        return super(PostAdmin, self).change_view(request, object_id, extra_context=None)

class ProjectoAdmin(admin.ModelAdmin):
    list_display = ('nombre','slug',)
    list_filter = ['nombre','slug',]
    list_per_page = 25
    list_max_show_all = 30

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                'filebrowser/js/FB_TinyMCE.js',
                'filebrowser/js/TinyMCEAdmin.js',)

class WikiAdmin(admin.ModelAdmin):
    #list_display = ('projecto',)
    list_per_page = 25
    list_max_show_all = 30

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                'filebrowser/js/FB_TinyMCE.js',
                'filebrowser/js/TinyMCEAdmin.js',)

class PeticionAdmin(admin.ModelAdmin):
    list_display = ('projecto','asunto','creado_fecha','inicio_fecha','terminado_fecha','creado_por','estado','asignado_a','prioridad',)
    list_per_page = 25
    list_max_show_all = 30

    class Media:
        js = ('grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                'filebrowser/js/FB_TinyMCE.js',
                'filebrowser/js/TinyMCEAdmin.js',)

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('projecto','categoria','titulo',)
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

admin.site.register(Projecto, ProjectoAdmin)
admin.site.register(Peticion, PeticionAdmin)
admin.site.register(Wiki, WikiAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Comentario, ComentarioAdmin)

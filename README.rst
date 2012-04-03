====================
Django-Project-Admin
====================
Aplicación escrita en django que permite darle un seguimiento a un proyecto, nada que no sea conocido, asignación de tareas por ticket, wiki, archivos, etc., cualquier parecido con Redmine es porque nos hemos basado en este y django-todo. ¿Por qué no usamos Redmine?, si lo usamos, solo que para algunos proyectos este es "como matar una mosca con una basuca".

Basado en
---------
    * redmine : http://www.redmine.org/
    * django-todo : https://github.com/shacker/django-todo
    
DashBoard recomendado
---------------------
        # append an app list module for "Applications"
        self.children.append(modules.Group(
            _('Panel: Project Admin'),
            collapsible=True,
            column=1,
            css_classes=('collapse opened',),
            exclude=('django.contrib.*',),
            children = [
                modules.ModelList(
                    _('Proyectos'),
                    column=1,
                    collapsible=False,
                    models=('projectadmin.models.Proyecto',),
                ),
                modules.ModelList(
                    _('Recursos'),
                    column=1,
                    collapsible=True,
                    css_classes=('collapse opened',),
                    models=(
                        'projectadmin.models.Peticion',
                        'projectadmin.models.Wiki',
                        'projectadmin.models.Documento',
                        'projectadmin.models.Archivo',
                        'projectadmin.models.Comentario',
                        ),
                ),
                modules.LinkList(
                    _('Analisis'),
                    column=2,
                    children=[
                        {
                            'title': _(u'Calendario'),
                            'url': '/admin/project-admin/show/calendar/',
                            'external': False,
                        },
                    ]
                ),
            ]
        ))

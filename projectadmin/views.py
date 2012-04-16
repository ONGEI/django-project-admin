# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from models import Peticion
import datetime

def show_calendar(request,ano=None,mes=None):
    hoy = datetime.date.today() if ano is None and mes is None else datetime.date(year=int(ano),month=int(mes),day=1)
    peticiones = Peticion.objects.filter(Q(creado_fecha__month=hoy.month) | Q(inicio_fecha__month=hoy.month) | Q(terminado_fecha__month=hoy.month) | Q(completo_fecha__month=hoy.month)) if request.user.is_admin() else Peticion.objects.filter((Q(creado_fecha__month=hoy.month) | Q(inicio_fecha__month=hoy.month) | Q(terminado_fecha__month=hoy.month) | Q(completo_fecha__month=hoy.month)), (Q(asignado_a=request.user)|Q(creado_por=request.user)))
    return render(
        request,
        "calendario.html",
        {
            'hoy':hoy,'peticiones':peticiones,'sig':hoy.replace(month=hoy.month+1,day=1),'ant':hoy.replace(month=hoy.month-1,day=1),
        },
        )
show_calendar = staff_member_required(show_calendar)

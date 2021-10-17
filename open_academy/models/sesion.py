# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime

today_date = datetime.date.today()

class Sesion(models.Model):
    _name = 'open_academy.sesion'
    _description    = 'sesion'

    fecha = fields.Date("Fecha de inicio", default=today_date)
    duracion = fields.Integer(string='Duración')

    @api.onchange('duracion')
    def _onchange_duracion(self):
        if self.duracion<0:
            self.duracion=0
            return {
                'warning': {
                    'title': "Error",
                    'message': "valor ingresado incorrecto, ingrese valores positivos",
                }
            }

    cantidadAsientos = fields.Integer(string='Cantidad de asientos', default=1)

    porcentajeAsientos = fields.Integer(compute='_compute_name')
    @api.depends('cantidadAsientos')
    def _compute_name(self):
        for record in self:
            record.porcentajeAsientos = (self._onchange_count_asistentes_id()/record.cantidadAsientos)*100

    activo = fields.Boolean(String='¿Activo?',readonly=False,default=True)

    @api.onchange('cantidadAsientos')
    def _onchange_cantidadAsientos(self):
        if self.cantidadAsientos<=0:
            self.cantidadAsientos=1
            return {
                'warning': {
                    'title': "Error",
                    'message': "valor ingresado incorrecto, ingrese valores positivos",
                }
            }

    #bien
    #instructor_id = fields.Many2one('open_academy.socio', 'socioI_id', ondelete='cascade', index=True)

    asistentes_id = fields.Many2many('open_academy.socio','socio_id', index=True)
  
    def _onchange_count_asistentes_id(self):
        count=0
        for record in self:
            for a in record.asistentes_id:
                #print(a.name)
                count = count+1
            return count
            
    @api.onchange('asistentes_id')
    def _onchange_asistentes_id(self):
        count=0
        for record in self:
            for a in record.asistentes_id:
                #print(a.name)
                count = count+1
           
            if count > self.cantidadAsientos:
                return {
                    'warning': {
                        'title': "Error",
                        'message': "Asientos no disponibles",
                    }
                }
                self.asistentes_id = record.asistentes_id

    @api.constrains('asistentes_id')
    def _check_something(self):
        for record in self:
            for a in record.asistentes_id:
                if a.instructor is True:
                    raise ValidationError("Advertencia: Instructor no puede estar en la sesion: %s" % a.name)

    #bien
    sesions_id = fields.Many2one('open_academy.course','course_id', ondelete='cascade', index=True, required=True)
    
    #sesion_id = fields.Many2one('open_academy.socio','socios_id', ondelete='cascade')
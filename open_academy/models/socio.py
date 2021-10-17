# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Socio(models.Model):
    _name = 'open_academy.socio'
    _description    = 'socio'

    name = fields.Char(string='Nombre')
    instructor = fields.Boolean(String='¿Es un instructor?',readonly=False)

    socio_id = fields.Many2one('open_academy.sesion', 'asistentes_id', ondelete='cascade')

    #socioI_id = fields.One2many('open_academy.sesion', 'instructor_id', string='Sesiones')

    #herencia
    #socios_id = fields.Many2many('open_academy.sesion', 'sesionII_id', index=True) 
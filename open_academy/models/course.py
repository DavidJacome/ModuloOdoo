# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'open_academy.course'
    _description    = 'Cursos'

    name = fields.Char(string='Nombre')
    description = fields.Char(string='')

    #bien
    users_id = fields.Many2one('open_academy.users', 'responsable_id', ondelete='cascade', index=True, required=True)

    #bien
    course_id = fields.One2many('open_academy.sesion', 'sesions_id', string='Cursos')

    
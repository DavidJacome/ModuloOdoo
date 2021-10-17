# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class Users(models.Model):
    _name = 'open_academy.users'
    _description    = 'users'

    name = fields.Char(string='Nombre')

    responsable_id = fields.One2many('open_academy.course', 'users_id', string='responsable')
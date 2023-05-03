from odoo import models, fields


class Ambiente(models.Model):
    _name = 'apontamento.ambiente'
    _description = 'Ambiente em que a atividade será desenvolvida'

    name = fields.Char(string='Nome do Ambiente')

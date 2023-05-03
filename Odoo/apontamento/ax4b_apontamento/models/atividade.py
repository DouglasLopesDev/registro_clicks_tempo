from odoo import models, fields, api
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from functools import reduce


class Atividade(models.Model):
    _name = 'apontamento.atividade'
    _description = 'Cadastro de Atividade'

    name = fields.Char(string='Card')
    desenvolvedor_id = fields.Many2many(
        'res.users', string='Desenvolvedor')
    descricao = fields.Text(string='Descrição')
    esta_finalizado = fields.Boolean(string="Finalizado?", default=False)
    apontamento_ids = fields.One2many(
        comodel_name='apontamento.apontamento', inverse_name='atividade_id', string='Apontamento'
    )
    total_horas = fields.Char(string="Total de Horas",
                              compute='calcular_horas_totais', default='00:00:00'
                              )
    ambiente_id = fields.Many2one('apontamento.ambiente', string='Ambiente')

    # @api.model
    # def create(self, vals_list):
    #     return super().create(vals_list)

    def write(self, vals_list):
        if self.esta_finalizado:
            raise UserError(
                'Não pode alterar uma atividade que está finalizada')
        return super().write(vals_list)

    def calculo_total_horas(self, t):
        return "%02d:%02d:%02d" % \
            reduce(lambda ll, b: divmod(ll[0], b) + ll[1:],
                   [(t,), 60, 60])

    def to_td(self, h):
        ho, mi, se = h.split(':')
        return timedelta(hours=int(ho), minutes=int(mi), seconds=int(se))

    def calcular_horas_totais(self):
        horas = []
        for rec in self:
            for item in rec.apontamento_ids:
                horas.append(item.total)

            rec.total_horas = self.calculo_total_horas(
                t=sum(map(self.to_td, horas), timedelta()).total_seconds())

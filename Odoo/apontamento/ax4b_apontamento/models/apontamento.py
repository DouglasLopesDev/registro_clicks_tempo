from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from datetime import date, datetime, timedelta
from functools import reduce


class Apontamento(models.Model):

    # TODO: Refatorar código para mudar o nome da model de Apontamento para Tarefa

    _name = 'apontamento.apontamento'
    _description = 'Apontamento de hora equipe odoo'

    atividade = fields.Char(string='Descrição da Atividade')
    atividade_id = fields.Many2one(
        comodel_name='apontamento.atividade', string="Atividade")
    data_inicio = fields.Datetime(
        string='Início')
    data_fim = fields.Datetime(string='Finalização')
    total = fields.Char(compute='_calculo_total_horas',
                        store=True, string="Tempo Total")

    categoria_id = fields.Many2one('apontamento.categoria', string='Categoria')

    desenvolvedor_id = fields.Many2many(
        'res.users', string='Desenvolvedor')

    @api.depends('data_fim', 'data_inicio')
    def _calculo_total_horas(self):
        for record in self:
            if isinstance(record.data_fim, datetime) and isinstance(record.data_inicio, datetime):
                delta = (record.data_fim - record.data_inicio).total_seconds()
                record.total = "%02d:%02d:%02d" % \
                    reduce(lambda ll, b: divmod(ll[0], b) + ll[1:],
                           [(delta,), 60, 60])
            else:
                record.total = '00:00:00'

    def finalizar_atividade(self):
        for record in self:
            if not isinstance(record.data_fim, datetime):
                record.data_fim = datetime.now()
            record.data_fim = datetime.now()

    def iniciar_atividade(self):
        for record in self:
            if not isinstance(record.data_inicio, datetime):
                record.data_inicio = datetime.now()
            record.data_inicio = datetime.now()

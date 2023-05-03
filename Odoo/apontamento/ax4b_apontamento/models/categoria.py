from odoo import models, fields

TOPICOS = [
    ('predesenolvimento', 'Pré Desenvolvimento'),
    ('desenvolvimento', 'Desenvolvimento'),
    ('especificacao', 'Especificação'),
    ('homologacao', 'Homologação'),
    ('trocaatividade', 'Troca de Atividade'),
    ('publicacao', 'Publicação')
]

SUBTOPICOS = [
    ('codificacao', 'Codificação'),
    ('cloud', 'Cloud'),
    ('documentacao', 'Documentação'),
    ('codereview', 'Code Review'),
    ('passagemconsultor', 'Passagem com o Consultor')
]


class Categoria(models.Model):
    _name = 'apontamento.categoria'
    _description = 'Categoria em que a tarefa será desenvolvida'

    name = fields.Char(string='Nome da Categoria')
    topicos = fields.Selection(TOPICOS, string='Tópico')
    subtopicos = fields.Selection(SUBTOPICOS, string='Subtópico')

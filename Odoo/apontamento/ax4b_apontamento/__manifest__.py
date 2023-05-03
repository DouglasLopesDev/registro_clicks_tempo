{
    'name': 'Apontamento',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/apontamento_view.xml',
        'views/atividade_view.xml',
        'views/ambiente_view.xml',
        'views/categoria_view.xml',
        'reports/atividade_report.xml',
        'reports/atividade_card.xml',
    ],
    "application": True,
    "sequence": 1,
}

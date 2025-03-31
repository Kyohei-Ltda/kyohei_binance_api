# -*- coding: utf-8 -*-
{
    'name': "Binance API",
    'summary': "Integre su Odoo con Binance",
    'description': """
Aproveche las integraciones con Binance para sus cobros
================================================================================

Después de instalar el módulo obtendrá:
    * Tasas de cambio
    """,
    'author': "Kyohei Ltda.",
    'website': "https://www.kyohei.bo",
    'category': 'Accounting',
    'version': '18.0.0.1',
    'depends': ['account'],
'external_dependencies': {'python': ['num2words']},
    'license': 'Other proprietary',
    'data': [
        # 'security/ir.model.access.csv',
        'data/cron_data.xml',
        'settings/settings_view.xml',
    ]
}


# -*- coding: utf-8 -*-

from odoo import models, fields


class KyoheiBinanceApiSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    binance_secret = fields.Char(string='Binance secret', config_parameter="kyohei_binance_api.binance_secret")
    binance_apikey = fields.Char(string='Binance Apikey', config_parameter="kyohei_binance_api.binance_apikey")

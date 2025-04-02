# -*- coding: utf-8 -*-

from . import models
from . import settings

def _kyohei_binance_api_post_init(env):
    endpoint_parameter = env['ir.config_parameter'].search([['key', '=', 'kyohei_binance_api.binance_endpoint']])
    if not endpoint_parameter:
        env['ir.config_parameter'].create({'key': 'kyohei_binance_api.binance_endpoint', 'value': 'https://api.binance.com'})
        
def _kyohei_binance_api_uninstall(env):
    endpoint_parameter = env['ir.config_parameter'].search([['key', '=', 'kyohei_binance_api.binance_endpoint']])
    if endpoint_parameter:
        endpoint_parameter.sudo().unlink()

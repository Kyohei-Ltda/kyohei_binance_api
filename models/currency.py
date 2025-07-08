# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from binance.client import Client

CURRENCIES = ['UST', 'BTC', 'ETH']


class KyoheiBinanceApi(models.Model):
    _inherit = 'res.currency'

    def _create_binance_client(self):
        secret = self.env['ir.config_parameter'].sudo().get_param("kyohei_binance_api.binance_secret")
        apikey = self.env['ir.config_parameter'].sudo().get_param("kyohei_binance_api.binance_apikey")
        return Client(apikey, secret)

    def _update_crypto_rates(self, rate, rate_date):
        current_rate_ids = self.rate_ids.filtered(lambda x: x.name == rate_date)
        if current_rate_ids:
            for rate_id in current_rate_ids:
                if rate_id:
                    rate_id.write({'inverse_company_rate': rate})
        else:
            self.write({
                'rate_ids': [[0, 0, {
                    'name': rate_date,
                    'inverse_company_rate': rate
                }]]
            })

    @api.model
    def _get_binance_currency_rate(self, date=False):
        """
        Check if the active currency rates for the given date are available on the Bebop server and update them if necessary.
        If any currency rate is not available on the server, call the '_update_bebop_currencies' method to fetch and update them.

        :param date: Optional parameter to specify the date for which currency rates should be checked and updated. If not provided, the current date is used.
        """
        company_env = self.env['res.company']
        bolivian_companies = company_env.search([['country_code', '=', 'BO']])
        if bolivian_companies:
            rate_date = date if date else fields.Date.context_today(self)
            updating_currencies = self.search([['name', 'in', CURRENCIES]])
            client = self._create_binance_client()
            for currency in updating_currencies:
                symbol = f"BOB{currency.symbol}"
                tickers = client.get_ticker(symbol=symbol)
                pass
                # date_dict = {'date': rate_date.strftime('%d-%m-%Y')}

# -*- coding: utf-8 -*-
# from odoo import http


# class KyoheiBinanceApi(http.Controller):
#     @http.route('/kyohei_binance_api/kyohei_binance_api', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kyohei_binance_api/kyohei_binance_api/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kyohei_binance_api.listing', {
#             'root': '/kyohei_binance_api/kyohei_binance_api',
#             'objects': http.request.env['kyohei_binance_api.kyohei_binance_api'].search([]),
#         })

#     @http.route('/kyohei_binance_api/kyohei_binance_api/objects/<model("kyohei_binance_api.kyohei_binance_api"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kyohei_binance_api.object', {
#             'object': obj
#         })


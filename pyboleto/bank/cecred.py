# -*- coding: utf-8 -*-
from pyboleto.data import BoletoData, CustomProperty


class BoletoCecred(BoletoData):
    '''Implementa Boleto Cecred

        Gera Dados necessários para criação de boleto para o banco Cecred
    '''

    agencia_cedente = CustomProperty('agencia_cedente', 4)
    conta_cedente = CustomProperty('conta_cedente', 6)
    codigo_beneficiario = CustomProperty('codigo_beneficiario', 6)
    nosso_numero = CustomProperty('nosso_numero', 7)

    carteira = CustomProperty('carteira', 1)

    def __init__(self):
        super(BoletoCecred, self).__init__()

        self.codigo_banco = "085"
        self.logo_image = "logo_cecred.jpg"
        self.especie_documento = 'DM'
        self.label_cedente = u'Agência/Código Beneficiário'
        self.local_pagamento = u'Pagável Preferencialmente nas Cooperativas '\
            u'do sistema Cecred. Após venc. somente na cooperativa'

    @property
    def codigo_dv_banco(self):
        return self.codigo_banco + '-1'

    @property
    def campo_livre(self):
        content = "%2s%5s%6s%8s%4s" % (self.carteira.zfill(2),
                                       self.agencia_cedente.zfill(5),
                                       self.codigo_beneficiario.zfill(6),
                                       self.nosso_numero.zfill(8),
                                       '0851')
        return content

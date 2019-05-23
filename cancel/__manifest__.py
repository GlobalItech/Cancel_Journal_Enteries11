{
    'name':   'User Rights for Cancel Journal Enteries',
    'author': 'Itech Resources',
    'company': 'ItechResources',
    'depends': [
                'base',
                'account_accountant_cbc',
                'sale',
                'purchase',
                'account_cancel',
                ],
    
    'data': [
        'views/cancel.xml',
        'security/cancel_rights.xml'
        ,
       
    ],
    
    'application': True,
    'price':'15.0',
    'currency': 'EUR',
}

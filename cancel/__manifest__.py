{
    'name':   'Cancel User Rights',
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
}

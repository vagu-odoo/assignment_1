{
    'name':'stock_transport',
    'depends':[
        'fleet',
        'stock_picking_batch'
    ],
    'installable':True,
    'application':True,
    'auto_install':False,
    'data':[
        'security/ir.model.access.csv',
        'views/fleet_category.xml',
        'views/batch_transfer.xml',
        'views/stock_picking_view.xml',
    ]
}
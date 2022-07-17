{
    'name': 'library_checkout',
    'version': 'Version 1',
    'summary': 'library_checkout ',
    'description': 'library_checkout',
    'category': 'Category',
    'author': 'Eladio G',
    'website': 'Website',
    "license": "AGPL-3",
    'depends': ['library_member'],
    'data': [
        "security/ir.model.access.csv",
        "views/checkout_view.xml",
        "views/library_menu.xml",
    ],
    'installable': True,
    'auto_install': False
}

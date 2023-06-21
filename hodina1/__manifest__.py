{
    'name': 'modul1',
    'version': '2.0',
    'depends': ['website'],
    'installable': True,
    'data':['views/snippets.xml'],
    'assets': {
        'web.assets_tests': [
            'hodina1/**/*',
        ],
    },
    'license': 'LGPL-3',
}
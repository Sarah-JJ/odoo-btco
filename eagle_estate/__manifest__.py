# -*- coding: utf-8 -*-

{
    'name': "Eagle Estate",

    'description': """
        Manage Eagle estates
    """,

    'author': "Sarah Juhain",

    "category": "Services/Estate",
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        "views/eagle_estate_actions.xml",
        "views/eagle_estate_menus.xml",
        "security/ir.model.access.csv",
        "views/eagle_estate_property_views.xml",
        "views/eagle_estate_property_room_views.xml",
    ],
    "application": True,
}

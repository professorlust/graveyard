"""
Module for helping with and handling common articles.
"""

# Normative directory of Creative Pages allowed on the page
# Key is the common "short" identification of creative page,
# as present in database (as string) and data model
COMMON_ARTICLES_CREATIVE_PAGES = {
    'clanky': {
        'name': 'Články&Eseje',
        'sections': [
            'Doplňky k pravidlům',
            'Historie postavy',
            'Hlod :-)',
            'Ostatní',
            'Poezie',
            'Popis dobrodružství',
            'Povídky',
            'Publicistika',
            'Recenze',
            'Úvahy',
        ]
    }
}


SLUG_NAME_TRANSLATION_FROM_CZ = {
    'clanky': 'articles-and-essays'
}

SLUG_NAME_TRANSLATION_TO_CZ = {v:k for k,v in SLUG_NAME_TRANSLATION_FROM_CZ.items()}

from datetime import date

import boundaries

boundaries.register('Philadelphia City Council Districts',
    encoding='iso-8859-1',
    srid=3702,
    last_updated=date(2011, 11, 28),
    name='Philadelphia City Council Districts',
    singular='Philadelphia City Council District',
    domain='Philadelphia, PA, USA',
    authority='Philadelphia City Planning Commission',
    source_url='https://www.opendataphilly.org/dataset/city-council-districts',
    start_date=date(2016, 1, 1),
    name_func=boundaries.clean_attr('DISTRICT'),
    id_func=boundaries.attr('OBJECTID'),
)
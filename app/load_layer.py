import os
from django.contrib.gis.utils import LayerMapping
from .models import Plots


plots_mapping = {
    'farmer': 'MED_DESCRI',
    'culture': 'RTT_DESCRI',
    'season': 'F_CODE_DES',
    'geom': 'MULTILINESTRING',

}

plots_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/countries.shp'))


def run(verbose=True):

    pl = LayerMapping(Plots, plots_shp, plots_mapping, transform=False, encoding='iso-8859-1')
    pl.save(strict=True, verbose=verbose)

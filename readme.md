# QGIS Gazetteer Plugin

Adds a gazetteer search panel to QGIS 1.8 / 2.0 which by default searches GeoNames, Yahoo (place search) and OSM Nominatim plus an [Astun Technology](http://astuntechnology.com) iShare address search.

## Available Gazetteers

All searches are performed via a web service call. The available searches can be configured in `gazetteers/config.ini`, each gazetteer requires a corresponding set of config / logic in it's own python file in `gazetters`.

The [qgis-gazetteer-search](https://github.com/mixedbredie/qgis-gazetteer-search) repository by [mixedbredie](https://github.com/mixedbredie) is a good choice if you'd like to roll your own search webservice such as one based on the LLPG (Local Land and Property Gazetteer) or LSG (Local Street Gazetteer) used in Great Britain.

## Installation

The plugin files need to live in a directory called `gazetteersearch` inside the QGIS Python plugins directory.

*Windows note:* The QGIS plugin directory should be under `C:\Documents and Settings\<Username>\.qgis2\python\plugins\` (Windows XP) or `C:\Users\<Username>\.qgis2\python\plugins\` (Windows +7).

*QGIS 1.8 note:* QGIS 1.8 stores it config under a `.qgis` directory.

### Using git

If you are using `git` then simply clone the repository into your QGIS python plugins directory:

    cd ~/.qgis2/python/plugins/
    git clone https://github.com/AstunTechnology/QGIS-Gazetteer-Plugin.git gazetteersearch

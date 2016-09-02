# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 Boundless Spatial
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf import settings
from exchange.version import get_version


def resource_variables(request):
    """Global exchange values to pass to templates"""
    defaults = dict(
        VERSION=get_version(),
        REGISTRY=getattr(settings, 'REGISTRY', False),
        REGISTRYURL=getattr(settings,'REGISTRYURL', None),
        CATALOGLIST=getattr(settings, 'CATALOGLIST', None),
        MAP_CRS=settings.DEFAULT_MAP_CRS,
        BOUNDLESS_URL=settings.BOUNDLESS_URL,
        BOUNDLESS_LINKTEXT=settings.BOUNDLESS_LINKTEXT,
    )

    return defaults


def version(request):
    """ Returns the exchange version """

    return dict(VERSION=get_version())


def registry(request):
    """ Registry variable to pass to templates"""

    return {'REGISTRY': settings.REGISTRY}


def map_crs(request):
    """ Map CRS variable to pass to templates"""

    return {'MAP_CRS': settings.DEFAULT_MAP_CRS}


def template_globals(request):
    """Global values to pass to templates"""

    defaults = dict(
        USE_OSGEO_IMPORTER=('osgeo_importer' in settings.INSTALLED_APPS)
    )
    return defaults

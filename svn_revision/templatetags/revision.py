# $Id: django-revision.py $
# Authors: Sean Auriti <sa@alexanderinteractive.com>, David Napolitan <dn@alexanderinteractive.com>

"""
Creates a template tag called {% revision %} that returns the current svn version.
Requires svnversion.
"""

import sys, os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), "../../"))
from django import template
from svn_revision.templatetags import REVISION

register = template.Library()


@register.simple_tag
def revision():
    """displays the revision number
    
    {% revision %}"""
    return REVISION

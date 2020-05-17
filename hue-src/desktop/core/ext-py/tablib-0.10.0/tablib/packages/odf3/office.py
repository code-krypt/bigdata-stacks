# -*- coding: utf-8 -*-
# Copyright (C) 2006-2007 Søren Roug, European Environment Agency
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Contributor(s):
#

from .namespaces import OFFICENS
from .element import Element
from .draw import StyleRefElement

# Autogenerated
def Annotation(**args):
    return StyleRefElement(qname = (OFFICENS,'annotation'), **args)

def AutomaticStyles(**args):
    return Element(qname = (OFFICENS, 'automatic-styles'), **args)

def BinaryData(**args):
    return Element(qname = (OFFICENS,'binary-data'), **args)

def Body(**args):
    return Element(qname = (OFFICENS, 'body'), **args)

def ChangeInfo(**args):
    return Element(qname = (OFFICENS,'change-info'), **args)

def Chart(**args):
    return Element(qname = (OFFICENS,'chart'), **args)

def DdeSource(**args):
    return Element(qname = (OFFICENS,'dde-source'), **args)

def Document(version="1.1", **args):
    return Element(qname = (OFFICENS,'document'), version=version, **args)

def DocumentContent(version="1.1", **args):
    return Element(qname = (OFFICENS, 'document-content'), version=version, **args)

def DocumentMeta(version="1.1", **args):
    return Element(qname = (OFFICENS, 'document-meta'), version=version, **args)

def DocumentSettings(version="1.1", **args):
    return Element(qname = (OFFICENS, 'document-settings'), version=version, **args)

def DocumentStyles(version="1.1", **args):
    return Element(qname = (OFFICENS, 'document-styles'), version=version, **args)

def Drawing(**args):
    return Element(qname = (OFFICENS,'drawing'), **args)

def EventListeners(**args):
    return Element(qname = (OFFICENS,'event-listeners'), **args)

def FontFaceDecls(**args):
    return Element(qname = (OFFICENS, 'font-face-decls'), **args)

def Forms(**args):
    return Element(qname = (OFFICENS,'forms'), **args)

def Image(**args):
    return Element(qname = (OFFICENS,'image'), **args)

def MasterStyles(**args):
    return Element(qname = (OFFICENS, 'master-styles'), **args)

def Meta(**args):
    return Element(qname = (OFFICENS, 'meta'), **args)

def Presentation(**args):
    return Element(qname = (OFFICENS,'presentation'), **args)

def Script(**args):
    return Element(qname = (OFFICENS, 'script'), **args)

def Scripts(**args):
    return Element(qname = (OFFICENS, 'scripts'), **args)

def Settings(**args):
    return Element(qname = (OFFICENS, 'settings'), **args)

def Spreadsheet(**args):
    return Element(qname = (OFFICENS, 'spreadsheet'), **args)

def Styles(**args):
    return Element(qname = (OFFICENS, 'styles'), **args)

def Text(**args):
    return Element(qname = (OFFICENS, 'text'), **args)

# Autogenerated end

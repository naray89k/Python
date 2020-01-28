#!/usr/bin/env python
# coding: utf-8
# mypackage/A/spam.py

from . import grok

# mypackage/A/spam.py

from ..B import bar

# mypackage/A/spam.py

from mypackage.A import grok # OK
from . import grok # OK
import grok # Error (not found)

from . import grok # OK
import .grok # ERROR


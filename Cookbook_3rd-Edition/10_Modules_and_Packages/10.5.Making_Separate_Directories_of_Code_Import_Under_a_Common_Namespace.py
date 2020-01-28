#!/usr/bin/env python
# coding: utf-8
import sys
sys.path.extend(['foo-package', 'bar-package'])
import spam.blah
import spam.grok

import spam
spam.__path__

import spam.custom
import spam.grok
import spam.blah

spam


#!/usr/bin/env python
# coding: utf-8
import shutil
shutil.unpack_archive('Python-3.3.0.tgz')
shutil.make_archive('py33','zip','Python-3.3.0')

shutil.get_archive_formats()


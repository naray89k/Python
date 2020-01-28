#!/usr/bin/env python
# coding: utf-8
raise SystemExit('It failed!')

import sys
sys.stderr.write('It failed!\n')
raise SystemExit(1)


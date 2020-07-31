#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 The WorkflowHub Team.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

__version__ = "0.1"
__author__ = 'WorkflowHub Team - https://workflowhub.org'
__credits__ = 'University of Southern California, University of Hawaii at Manoa'

import logging

from .generator import WorkflowGenerator
from .trace import Trace, TraceAnalyzer
from .types import OutputFormat

logging.getLogger('workflowhub').addHandler(logging.NullHandler())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 The WorkflowHub Team.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import networkx as nx
from typing import Optional


class Workflow(nx.DiGraph):
    def __init__(self, name: str, makespan: Optional[int]) -> None:
        super().__init__(name=name, makespan=makespan)

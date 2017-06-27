# -*- coding: utf-8 -*-
# Copyright (c) 2016 Spotify AB

from __future__ import absolute_import, division, print_function

import attr
from .base import BaseNode


@attr.s
class TypeNode(BaseNode):
    name = attr.ib()


# -*- coding: utf-8 -*-
#
# File is part of the Prometheus Project
#
# Copyright (C) 2012-2015 Roger Pereira Boff <roger@gmail.com>
# All rights reserved
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., or visit: http://www.gnu.org/.
#
# Author: Roger Pereira Boff <rogerboff@gmail.com>
#
from django.views.generic.base import TemplateView


class DjSourceView(TemplateView):
    template_name = 'djsourceview.html'

    def get_context_data(self, **kwargs):
        kwargs['host'] = self.request.get_host()
        return super(DjSourceView, self).get_context_data(**kwargs)

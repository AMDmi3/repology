# Copyright (C) 2019 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# This file is part of repology
#
# repology is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# repology is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with repology.  If not, see <http://www.gnu.org/licenses/>.

from typing import List


def cpe_parse(cpe_str: str) -> List[str]:
    escaped = False
    current = ''
    res = []

    for char in cpe_str:
        if escaped:
            current += '\\' + char
            escaped = False
        elif char == '\\':
            escaped = True
        elif char == ':':
            res.append(current)
            current = ''
        else:
            current += char

    res.append(current)
    return res

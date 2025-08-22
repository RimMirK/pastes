#  pastes - Minimal Python client for pastes.dev
#  Copyright (C) 2025-present RimMirK
#
#  This file is part of pastes.
#
#  pastes is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, version 3 of the License.
#
#  pastes is an independent, unofficial client library.
#  It provides a very simple interface for uploading code to pastes.dev:
#  just two functions are available — paste() and apaste().
#
#  You should have received a copy of the GNU General Public License
#  along with pastes.  If not, see the LICENSE file.
#
#  Repository: https://github.com/RimMirK/pastes
#  Telegram: @RimMirK

from .main import paste, apaste, LANGUAGES

__version__ = version = '1.3.1'

__all__ = [
    'paste',
    'apaste',
    'version',
    'LANGUAGES',

]


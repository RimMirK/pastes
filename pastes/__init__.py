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
#  It provides a very simple interface for uploading and getting code from pastes.dev
#
#  You should have received a copy of the GNU General Public License
#  along with pastes.  If not, see the LICENSE file.
#
#  Repository: https://github.com/RimMirK/pastes
#  Telegram: @RimMirK


__version__ = version = '1.5.1'

from .main import _set_api_url, _set_user_agent, paste, get_paste, apaste, aget_paste, LANGUAGES


__all__ = [
    '_set_api_url',
    '_set_user_agent',
    'paste',
    'get_paste',
    'aget_paste',
    'apaste',
    'version',
    'LANGUAGES'
]




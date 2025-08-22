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


from requests import get, post
from gzip import compress


_api_url = 'https://api.pastes.dev/post'
_pasted_link = 'https://pastes.dev/{}'


LANGUAGES = [
    # text
    "plain"
    "log"
    
    # config
    "yaml"
    "json"
    "xml"
    "ini"
    
    # code
    "java"
    "javascript"
    "typescript"
    "python"
    "kotlin"
    "scala"
    "cpp"
    "csharp"
    "shell"
    "ruby"
    "rust"
    "sql"
    "go"
    
    # web
    "html"
    "css"
    "scss"
    "php"
    "graphql"
    
    # misc
    "dockerfile"
    "markdown"
    "proto"
]


def paste(code, language = 'auto'):
    headers = {
        'Content-Type': f'text/{language}',
        'Content-Encoding': 'gzip',
    }

    gzip_data = compress(code.encode('utf-8'))

    response = post(_api_url, data=gzip_data, headers=headers)
    
    return _pasted_link.format(response.json()['key'])

from httpx import post as apost

async def apaste(code, language = 'auto'):
    headers = {
        'Content-Type': f'text/{language}',
        'Content-Encoding': 'gzip',
    }
    
    gzip_data = compress(code.encode('utf-8'))
    
    response = apost(_api_url, data=gzip_data, headers=headers)
    
    return _pasted_link.format(response.json()['key'])


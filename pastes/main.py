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


from requests import get, post
from gzip import compress
from . import version 

_api_url = 'https://api.pastes.dev/'
_pasted_link = 'https://pastes.dev/{}'
_user_agent = f'pastes/{version} (https://github.com/RimMirK/pastes)'
_default_headers = {"User-Agent": _user_agent}

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

# general
def _set_api_url(new_url):
    global _api_url
    _api_url = new_url if new_url.endswith("/") else new_url+"/"

def _set_user_agent(new_user_agent):
    global _user_agent, _default_headers
    _user_agent = new_user_agent
    _default_headers.update({"User-Agent": new_user_agent})
    


# sync
def paste(code, language = 'auto'):
    headers = _default_headers
    headers.update({
        'Content-Type': f'text/{language}',
        'Content-Encoding': 'gzip',
    })

    gzip_data = compress(code.encode('utf-8'))

    response = post(_api_url+"post", data=gzip_data, headers=headers)
    
    return _pasted_link.format(response.json()['key'])

def get_paste(url):
    return get(_api_url+(url.rstrip("/").split("/")[-1]), headers=_default_headers).text

# async
import httpx

async def apaste(code, language = "auto"):
    headers = _default_headers
    headers.update({
        "Content-Type": f"text/{language}",
        "Content-Encoding": "gzip",
    })

    gzip_data = compress(code.encode("utf-8"))

    async with httpx.AsyncClient() as client:
        response = await client.post(_api_url+"post", data=gzip_data, headers=headers)

    response.raise_for_status()
    return _pasted_link.format(response.json()["key"])

async def aget_paste(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(_api_url+(url.rstrip("/").split("/")[-1]), headers=_default_headers)

    response.raise_for_status()
    return response.text









# by @RimMirK (t.me/RimMirK)

from requests import get, post
from gzip import compress

__version__ = version = '1.0.0'

__all__ = [
    'paste'
    'version'
    'LANGUAGES',
]

_api_url = 'https://bytebin.lucko.me/post'
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

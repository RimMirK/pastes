from requests import get, post
from gzip import compress


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

from httpx import post as apost

async def apaste(code, language = 'auto'):
    headers = {
        'Content-Type': f'text/{language}',
        'Content-Encoding': 'gzip',
    }
    
    gzip_data = compress(code.encode('utf-8'))
    
    response = apost(_api_url, data=gzip_data, headers=headers)
    
    return _pasted_link.format(response.json()['key'])
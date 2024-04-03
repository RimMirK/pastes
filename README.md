# PasteCodeAPI

API client for [pastes.dev](https://pastes.dev/)

## Install
```sh
pip install pastes
```

## Usage
```py
from pastes import paste

code = """
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
"""

url = paste(code)

print(url) # https://pastes.dev/UUHlliP7SF
```

## Developer
[@RimMirK](https://t.me/RimMirK)
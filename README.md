# PasteCodeAPI

API client for [pastes.dev](https://pastes.dev/)

## Install
```sh
pip install pastes
```

## Usage
### Sync
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

### Async
```py
from pastes import apaste
import asyncio

code = """
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
"""

async def main():
    url = await apaste(code)

    print(url) # https://pastes.dev/UUHlliP7SF

asyncio.run(main())
```

## Developer
[@RimMirK](https://t.me/RimMirK)
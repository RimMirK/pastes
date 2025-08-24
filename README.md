![pasters](.github/logo+name-lt.png#gh-light-mode-only)
![pasters](.github/logo+name-dt.png#gh-dark-mode-only)

[![PyPI](https://img.shields.io/pypi/v/pastes?color=blue&label=PyPI)](https://pypi.org/project/pastes/)
[![Python](https://img.shields.io/pypi/pyversions/pastes.svg?logo=python&logoColor=yellow)](https://pypi.org/project/pastes/)
[![License](https://img.shields.io/github/license/RimMirK/pastes?color=green)](LICENSE)
[![StandWithUkraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)

Minimalistic Python client for [pastes.dev](https://pastes.dev/)
Share your code in seconds with a simple function call.  

---

## ✨ Features
- 🌀 Both **sync** and **async** APIs  
- ⚡ One-liner usage  
- 📤 Returns instant paste URL  
- 🐍 Pure Python, only requests and httpx are required

---

## 📦 Installation
```sh
pip install pastes
```

---

## ⚡ Usage

### 🔹 Sync

```py
from pastes import paste, get_paste, _set_api_url, _set_user_agent

# set custom API endpoint (optional)
_set_api_url("https://my-api.example.com")

# set custom user agent (optional)
_set_user_agent("My project/1.0.0")

code = """
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
"""

# create paste
url = paste(code)
print(url)  # https://pastes.dev/UUHlliP7SF

# fetch paste
print(get_paste(url))  # def fib(n): ...
```

### 🔹 Async

```py
from pastes import apaste, aget_paste, _set_api_url, _set_user_agent
import asyncio

# set custom API endpoint (optional)
_set_api_url("https://my-api.example.com")

# set custom user agent (optional)
_set_user_agent("My project/1.0.0")

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
    # create paste
    url = await apaste(code)
    print(url)  # https://pastes.dev/UUHlliP7SF

    # fetch paste
    text = await aget_paste(url)
    print(text) # def fib(n): ...

asyncio.run(main())
```

## 👨‍💻 Author

Made with ❤️ by [@RimMirK](https://t.me/RimMirK)



# Pastes
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
- 🐍 Pure Python, only requests required

---

## 📦 Installation
```sh
pip install pastes
```

---

## ⚡ Usage

### 🔹 Sync

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
print(url)  # https://pastes.dev/UUHlliP7SF
```

---

### 🔹 Async

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
    print(url)  # https://pastes.dev/UUHlliP7SF

asyncio.run(main())
```

---

## 👨‍💻 Author

Made with ❤️ by @RimMirK


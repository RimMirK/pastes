# Pasters
[![PyPI](https://img.shields.io/pypi/v/pasters?color=blue&label=PyPI)](https://pypi.org/project/pasters/)
[![Python](https://img.shields.io/pypi/pyversions/pasters.svg?logo=python&logoColor=yellow)](https://pypi.org/project/pasters/)
[![License](https://img.shields.io/github/license/RimMirK/pasters?color=green)](LICENSE)
[![StandWithUkraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)

Minimalistic Python client for [paste.rs](https://paste.rs/)  
Share text or code in seconds with one simple call.  

---

## ✨ Features
- 🌀 Both **sync** and **async** APIs  
- ⚡ One-liner usage  
- 📤 Instant paste URL  
- 🐍 Pure Python (depends only on `requests` and `httpx`)  

---

## 📦 Installation
```sh
pip install pasters
````

---

## ⚡ Usage

### 🔹 Sync

```python
from pasters import paste, get_paste, delete_paste

# create paste
url = paste("print('hello world')", ext="py")
print(url)  # https://paste.rs/abcd.py

# fetch paste
print(get_paste(url))

# delete paste
delete_paste(url)
```

### 🔹 Async

```python
from pasters import apaste, aget_paste, adelete_paste
import asyncio

async def main():
    # create paste
    url = await apaste("# some markdown text", ext="md")
    print(url)  # https://paste.rs/efgh.md

    # fetch paste
    text = await aget_paste(url)
    print(text)

    # delete paste
    await adelete_paste(url)

asyncio.run(main())
```

---

## API

* `paste(text, ext='', allow_206=False) -> str`
* `apaste(text, ext='', allow_206=False) -> str`
* `get_paste(url) -> str`
* `aget_paste(url) -> str`
* `delete_paste(url) -> None`
* `adelete_paste(url) -> None`

---

## 👨‍💻 Author

Made with ❤️ by [@RimMirK](https://t.me/RimMirK)

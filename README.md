# py_win_x86_64_gcc
Download tools from w64devkit with Python.

> [!IMPORTANT]
> This project simply packages `7zr.exe` and `w64devkit.exe` without any modifications.
> - `7zr.exe` is sourced from https://www.7-zip.org/download.html
> - `w64devkit.exe` is sourced from https://github.com/skeeto/w64devkit/releases
>
> This project is only compatible with **64-bit Windows systems based on the x86_64 architecture**.

## Installation

```cmd
pip install py_win_x86_64_gcc
```

## Usage

> [!NOTE]
> An extraction process may be triggered on first use, which will take approximately ten seconds to complete.

```python
from py_win_x86_64_gcc import get_all_tools, get_tool

# Get all the executable filename in w64devkit
print(get_all_tools())

# Get filepath for certain tool (like g++, gcc etc.)
print(get_tool("g++"))
print(get_tool("gcc"))

# Compile something with g++ if you like
import subprocess
ret1 = subprocess.run(
    [get_tool("g++"), "test_gcc.cpp", "-o", "test_gcc.exe"])
ret2 = subprocess.run(["test_gcc.exe"])
```

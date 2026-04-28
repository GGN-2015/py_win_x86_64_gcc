import os
import shutil
import subprocess
from typing import Optional

DIRNOW = os.path.dirname(os.path.abspath(__file__))
DATA_PACK_DIR = os.path.join(DIRNOW, "data_pack")

ZIP_TOOL = os.path.join(DATA_PACK_DIR, "7zr.exe")
DEVKIT_ZIP = os.path.join(DATA_PACK_DIR, "w64devkit-x64-2.7.0.7z.exe")
AIM_FOLDER = os.path.join(DATA_PACK_DIR, "w64devkit")

GCC_BIN_FOLDER = os.path.join(AIM_FOLDER, "bin")

def unzip(force:bool=False, quiet:bool=False) -> bool:
    if not os.path.isfile(ZIP_TOOL):
        raise FileNotFoundError(f"{ZIP_TOOL}")
    if not os.path.isfile(DEVKIT_ZIP):
        raise FileNotFoundError(f"{DEVKIT_ZIP}")
    if force:
        if os.path.isdir(AIM_FOLDER):
            shutil.rmtree(AIM_FOLDER)
    if os.path.isdir(AIM_FOLDER):
        return True
    if not quiet:
        print("py_win_x86_64_gcc: unzip ...")
    ret = subprocess.run(
            args=[ZIP_TOOL, "x", DEVKIT_ZIP],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL, check=False,
            cwd=DATA_PACK_DIR,
            shell=True)
    return os.path.isdir(AIM_FOLDER)

def get_7zr() -> str:
    return ZIP_TOOL

def get_gcc_bin_folder(force_unzip:bool=False) -> Optional[str]:
    if unzip(force_unzip):
        return GCC_BIN_FOLDER
    return None

def get_all_tools(force_unzip:bool=False) -> list[str]:
    if unzip(force_unzip):
        return sorted(list(os.listdir(GCC_BIN_FOLDER)) + ["7zr.exe"])
    else:
        return ["7zr.exe"]

def get_tool(tool_name:str, force_unzip:bool=False) -> Optional[str]:
    unzip(force_unzip)
    if tool_name.endswith(".exe") or tool_name.endswith(".bat"):
        tool_name = tool_name[:-4]
    
    if tool_name.lower() == "7zr":
        return ZIP_TOOL

    tool_list = get_all_tools()
    found:Optional[str] = None
    for suf in [".exe", ".bat"]:
        if (tool_name + suf) in tool_list:
            found = tool_name + suf
            break
    
    if found is None:
        return None
    else:
        return os.path.join(GCC_BIN_FOLDER, found)

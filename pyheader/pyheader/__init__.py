import platform
WIN = False
plat = platform.system()
if plat == "Windows":
    WIN = True
__all__=["WIN"]
# rotmg_teleport

you have to manually set regions for now. screen grab has left, top, right, bottom of entire window... offset by window resolution to automatically... or just manually set values for where your hp bar is.

manually set threshold within code for automatic teleportation when ur health gets below some value. actually by default it is set at 0.25 but it's a parameter in the teleport_nexus function

my game didnt load so i didnt test it yet... use with caution

```
pip install numpy
pip install pywin32
pip install opencv-python
pip install pywinauto
```

and these are the values you change until the screen fits your health bar

```
left, top, right, bottom = 620, 260, 790, 270
```

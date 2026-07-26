# Different styles of importing modules

# 1) import module_name
import math
print("PI :", math.pi)

# 2) from module_name import entity
from math import pi
print("PI :", pi)

# 3) import module_name as alias
import math as m
print("PI :", m.pi)

# 4) from module_name import entity as alias
from math import pi as PI
print("PI :", PI)
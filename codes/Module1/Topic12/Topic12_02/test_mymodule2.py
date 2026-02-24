# 将目标路径添加到 sys.path 中
import sys
sys.path.append("codes/Module1/Topic12/Topic12_02/other_path")

import codes.Module1.Topic12.Topic12_02.mymodule3 as mymodule3

print(mymodule3.add(5, 3))
print(mymodule3.subtract(5, 3))
print(mymodule3.PI)
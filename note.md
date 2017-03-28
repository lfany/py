### Python 环境变量
- PYTHONPATH	PYTHONPATH是Python搜索路径，默认我们import的模块都会从PYTHONPATH里面寻找。
- PYTHONSTARTUP	Python启动后，先寻找PYTHONSTARTUP环境变量，然后执行此文件中变量指定的执行代码。
- PYTHONCASEOK	加入PYTHONCASEOK的环境变量, 就会使python导入模块的时候不区分大小写.
- PYTHONHOME	另一种模块搜索路径。它通常内嵌于的PYTHONSTARTUP或PYTHONPATH目录中，使得两个模块库更容易切换。


### 2.X python 支持

'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
print "你好，世界";
'''

注意：Python3.X 源码文件默认使用utf-8编码，所以可以正常解析中文，无需指定 UTF-8 编码。
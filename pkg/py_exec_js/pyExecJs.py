# pyexecjs、js2py 等库不维护了

import subprocess

# js文件最后必须有输出，可以使用 console.log
pro = subprocess.run("node pkg/py_exec_js/js.js", stdout=subprocess.PIPE)
print(pro)
# 获得标准输出
_token = pro.stdout
print(_token)
# 转一下格式
token = _token.decode().strip()
print(token)
# TODO 小工具

一个命令行待办工具，纯 Python 3 标准库，无第三方依赖。

## 运行
- 添加：`python todo.py add <内容>`
- 列出：`python todo.py list`

## 约定
- 只用标准库，不要引入任何第三方包
- 新功能要保持现有命令行风格（`python todo.py <命令> <参数>`）
- 改完必须能用上面的命令跑通

## 测试
- 如果还没有测试文件，用标准库 `unittest` 新建 `test_todo.py`
- 改完跑：`python -m unittest`

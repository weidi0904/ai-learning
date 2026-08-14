# todo.py
import sys

TODOS = []

def add(item):
    TODOS.append(item)
    print(f"已添加：{item}")

def list_todos():
    if not TODOS:
        print("（暂无待办）")
        return
    for i, item in enumerate(TODOS, 1):
        print(f"{i}. {item}")

def main():
    if len(sys.argv) < 2:
        print("用法：python todo.py [add <内容> | list]")
        return
    cmd = sys.argv[1]
    if cmd == "add":
        add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_todos()
    else:
        print(f"未知命令：{cmd}")

if __name__ == "__main__":
    main()
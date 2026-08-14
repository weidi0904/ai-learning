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

def done(index_text):
    if not index_text.isdigit():
        print("请输入数字序号。")
        return

    index = int(index_text)
    if index < 1 or index > len(TODOS):
        print("序号超出范围。")
        return

    item = TODOS.pop(index - 1)
    print(f"已完成：{item}")

def main():
    if len(sys.argv) < 2:
        print("用法：python todo.py [add <内容> | list | done <序号>]")
        return
    cmd = sys.argv[1]
    if cmd == "add":
        add(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_todos()
    elif cmd == "done":
        if len(sys.argv) < 3:
            print("请输入待办序号。")
            return
        done(sys.argv[2])
    else:
        print(f"未知命令：{cmd}")

if __name__ == "__main__":
    main()

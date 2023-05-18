MAX = 3
stack = [0]*MAX
sp = 0

def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp = sp + 1
        print("本", d, "冊を追加しました")
    else:
        print("これ以上データを入れられません")
def pop():
    global sp
    if sp > 1:
        sp = sp - 1
        return stack[sp]
    else:
        print("取り出すデータが存在しません")
        return None

def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp = sp + 1
        print("本", d, "冊を追加しました")
    else:
        print("これ以上データを入れられません")

for i in range(5):
    push(i)
for i in range(5):
    d = pop()
    print("取り出したデータ", d)
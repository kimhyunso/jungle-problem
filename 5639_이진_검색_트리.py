import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(6 ** 10)

preorder = []
for line in sys.stdin:
    line = line.strip()
    if line:
        preorder.append(int(line))
    else:
        break

def postorder(start, end):
    if start > end:
        return
    
    root = preorder[start]
    
    split = start + 1
    while split <= end and preorder[split] < root:
        split += 1
    
    # 왼쪽 서브트리
    postorder(start + 1, split - 1)
    # 오른쪽 서브트리
    postorder(split, end)
    # 루트 출력
    print(root)

postorder(0, len(preorder) - 1)
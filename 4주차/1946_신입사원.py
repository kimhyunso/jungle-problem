import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    person_cnt = int(input())
    person_infomation = []

    for _ in range(person_cnt):
        doc_rank, interview_rank = map(int, input().split())
        person_infomation.append((doc_rank, interview_rank))

    person_infomation.sort(key=lambda x : (x[0], x[1]))

    rank = int(1e9)
    count = 0

    for doc, interview in person_infomation:
        if interview < rank:
            rank = interview
            count += 1
    print(count)


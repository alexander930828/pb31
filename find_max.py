# 최댓값 구하기
# 입력: 숫자가 n개 들어 있는 리스트
# 출력: 숫자 n개 중 최댓값

def find_max(a):
    max_n = a[0]
    n = len(a)
    for i in range(1, n):
        if max_n <= a[i]:
            max_n = a[i]
    return max_n

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v))


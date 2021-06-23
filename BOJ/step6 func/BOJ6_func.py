#15596  정수 N개의 합
# Python 2, Python 3, PyPy, PyPy3: def solve(a: list) -> int
#a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
#리턴값: a에 포함되어 있는 정수 n개의 합 (정수)
def solve(a):
    return sum(a)
# solve= sum

#4673   셀프넘버
def self_number(num):
    self_num = num
    while num != 0:
        self_num += num % 10
        num //= 10
    return self_num


result = []

for i in list(range(1, 10001)):
    result.append(self_number(i))
    if i not in result:
        print(i)


#1065 한수
#어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
# boj, 1065 : 한수, python3
N = int(input())

def hansu(num):
    cnt = 0
    for i in range(1,num+1):
        if i <= 99:
            cnt += 1
        else:
            nums = list(map(int, str(i)))
            if nums[0] - nums[1] == nums[1] - nums[2]:
                cnt += 1
    print(cnt)

hansu(N)
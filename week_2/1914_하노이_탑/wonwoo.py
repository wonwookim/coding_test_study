import sys
input = sys.stdin.readline
num = int(input())
def hannoi(num, start, temp, end):
    if num > 20:
        return None
    if num == 1:
        print(f'{start} {end}')
        return None
    hannoi(num-1, start, end, temp)
    print(f'{start} {end}')
    hannoi(num-1, temp, start, end)
        
print(2**num - 1)
hannoi(num, 1,2,3)
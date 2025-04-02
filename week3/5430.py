import sys

class AC:
    def __init__(self):
        self.list = []

    def rotate(self,value):
        self.list = self.list.reverse(value)

    def delete(self):
        if not self.list:
            print('error')
        return self.list.pop(0)


lines = [line.strip() for line in sys.stdin.readlines()] 
num = int(lines[0])

ac = AC()
for i in range(n):
    num_list = list(lines[3*i])
    for x in lines[3*i+ 1]:
        if x == 'R':
            ac.rotate(ac)
        elif x == 'D':
            ac.delete()
    







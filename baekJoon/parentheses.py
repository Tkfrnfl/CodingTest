from itertools import combinations
import operator
import copy

if __name__ == "__main__":
    n = int(input())
    arr = list(input())

    mx = 2**31 *-1

    operators={
        "+":operator.add,
        "-":operator.sub,
        "*":operator.mul,
    }

    def cal(fomula):
        fomula_copy = copy.deepcopy(fomula)
        while len(fomula_copy) > 1:
            num = operators[fomula_copy[1]](int(fomula_copy[0]), int(fomula_copy[2]))

            fomula_copy = [num] + fomula_copy[3:]
        return fomula_copy[0]    

    for i in range((n//2)+1):

        comb= list(combinations(range(n//2),i))

        for case in comb:
            arr_copy= copy.deepcopy(arr)
            for j in case:
                arr_cal= arr[j*2:j*2+3]
                arr_rest1= arr[:j*2]
                arr_rest2= arr[j*2+3:]

                cal_num= operators[arr[j*2+1]](int(arr_cal[0]),int(arr_cal[2]))

                arr_copy= arr_rest1+[cal_num]+arr_rest2

            mx=max(mx,cal(arr_copy))

    print(mx)
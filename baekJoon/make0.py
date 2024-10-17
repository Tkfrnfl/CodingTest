# from itertools import product
# import copy

# if __name__ == "__main__":
#     n= int(input())
#     arr=[int(input())for _ in range(n)]

#     result=[]

#     op=[0,1,2] # 0= +   1= -  2=None 

#     for ar in arr:
#         ar_prod= list(product(op, repeat=ar-1))
        
#         num_arr = [k for k in range(1,ar+1)]

#         prod_list=[]
#         for prod in ar_prod:
            
#             num_copy =copy.deepcopy(num_arr)
#             prod_copy = copy.deepcopy(list(prod))
#             # 공백 먼저 처리
#             cnt=0
#             for idx,val in enumerate(prod):
#                 if val ==2:
#                     num_copy[idx-cnt]=num_copy[idx-cnt]*10+num_copy[idx+1-cnt]
#                     num_copy.pop(idx+1-cnt)
#                     prod_copy.pop(idx-cnt)
#                     cnt+=1

#             num=num_copy[0]
#             for idx,val in enumerate(prod_copy):
#                 if val ==0:
#                     num+=num_copy[idx+1]
#                 if val ==1:
#                     num-=num_copy[idx+1]

#             if num==0:
#                 prod_list.append(prod)

#         result.append(prod_list)

#     answer=[]
#     for re in result:

#         for i in re:
#             result_str=''
#             for idx,val in enumerate(i):
#                 if val == 0:
#                     result_str+=str(idx+1)
#                     result_str+='+'
#                 if val == 1:    
#                     result_str+=str(idx+1)
#                     result_str+='-'
#                 if val == 2:    
#                     result_str+=str(idx+1)
#                     result_str+=' '
#             result_str+=str(len(i)+1)
#             answer.append(result_str)
#         answer.append('\n')  
               


#     sorted_answers = sorted(answer, key=lambda x: [ord(char) for char in x])

#     print(sorted_answers)
#     # 결과 출력
#     for ans in sorted_answers: 
#             print(ans)
from itertools import product

def find_zero_expressions(n):
    ops = [0, 1, 2]  # 0 = '+', 1 = '-', 2 = ' ' (공백)
    num_arr = [i for i in range(1, n + 1)]  # 1부터 N까지 숫자 리스트

    result = []

    # 연산자 조합 생성
    for op_combination in product(ops, repeat=n - 1):
        # 표현식 문자열 만들기
        expression = ''
        for i in range(n - 1):
            expression += str(num_arr[i]) + ('+' if op_combination[i] == 0 else '-' if op_combination[i] == 1 else ' ')
        expression += str(num_arr[-1])  # 마지막 숫자 추가

        # 수식을 평가하여 결과가 0인지 확인
        if evaluate_expression(expression) == 0:
            result.append(expression)

    return result

def evaluate_expression(expression):
    # 공백을 제거하고 숫자를 이어 붙이기 위해 eval() 사용
    expression = expression.replace(' ', '')
    return eval(expression)

if __name__ == "__main__":
    test_cases = int(input())
    cases = [int(input()) for i in range(test_cases)]

    all_results = []

    for n in cases:
        results = find_zero_expressions(n)
        all_results.append(sorted(results))  # ASCII 순서로 정렬

    # 결과 출력
    for idx, results in enumerate(all_results):
        for result in results:
            print(result)
        if idx < len(all_results) - 1:
            print()  # 각 테스트 케이스의 결과를 띄어쓰기
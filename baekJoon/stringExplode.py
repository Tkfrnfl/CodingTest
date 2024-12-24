#-*- coding:utf-8 -*-


if __name__ == "__main__":
    string=str(input())
    bomb=str(input())


    stack = []
    bomb_length = len(bomb)

    for char in string:
        stack.append(char)

        # 스택의 마지막 부분이 폭탄 문자열과 같으면 폭발 처리
        if len(stack) >= bomb_length and ''.join(stack[-bomb_length:]) == bomb:
            del stack[-bomb_length:] 

    result = ''.join(stack)
    if result:
        print(result)
    else:
        print("FRULA")
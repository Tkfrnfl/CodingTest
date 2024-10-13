
if __name__ == "__main__":



    def solution(commands):
        answer = []
        arr = [['']*50 for _ in range(50)]
        mg={}
        
        for cmd in commands:
            split = cmd.split()

            if split[0]== 'UPDATE':
                if len(split) ==4:
                    arr[int(split[1]) - 1][int(split[2]) - 1] = split[3]
                else:
                    for i in range(50):
                        for j in range(50):
                            if arr[i][j]== split[1]:
                                arr[i][j]= split[2]
            # if split[0]== 'MERGE':
            #     i1=int(split[1])
            #     i2=int(split[2])
            #     i3=int(split[3])
            #     i4=int(split[4])
                
            #     arr[i3][i4] = arr[i1][i2]
                
            #     if (i1,i2) in mg:
            #         mg[(i1,i2)].append((i3,i4))
            #     else:
            #         mg[(i1,i2)]= (i3,i4)
                    
            #     if (i3,i4) in mg:
            #         mg[(i3,i4)].append((i1,i2))
            #     else:
            #         mg[(i3,i4)]= (i1,i2)
                
            #     tmp = mg[(i1,i2)]
            #     tmp = list(tmp)
            #     tmp.append((i1,i2))
            #     tmp = tuple(tmp)
            #     for i in tmp:
            #         print(i)
            #         print(mg)
            #         if i in mg:
            #             for j in tmp:
            #                 if j!=i:
            #                     mg[i].append(j)
            #         else:
            #             mg.setdefault(i,[])
            #             for j in tmp:
            #                 if j!=i:
            #                     mg[i].append(j)
                        
            # if split[0]== 'UNMERGE':
            #     i1=int(split[1])
            #     i2=int(split[2])
                
            #     tmp = mg[(i1,i2)]
            #     for i in tmp:
            #         if i!=(i1,i2):
            #             arr[i[0]][i[1]] = ''
            #         mg.setdefault(i,[])
            # if split[0]== 'PRINT':
            #     answer.append(arr[int(split[1])][int(split[2])])
            elif split[0] == 'MERGE':
                r1, c1, r2, c2 = map(int, split[1:])
                r1 -= 1  # 인덱스 조정
                c1 -= 1
                r2 -= 1
                c2 -= 1

                # 병합 셀 값 결정
                value_to_merge = arr[r1][c1] if arr[r1][c1] else arr[r2][c2]
                arr[r1][c1] = value_to_merge
                arr[r2][c2] = value_to_merge

                # 병합 정보 저장
                if (r1, c1) not in mg:
                    mg[(r1, c1)] = []
                if (r2, c2) not in mg:
                    mg[(r2, c2)] = []

                mg[(r1, c1)].append((r2, c2))
                mg[(r2, c2)].append((r1, c1))

            elif split[0] == 'UNMERGE':
                r, c = map(int, split[1:])
                r -= 1  # 인덱스 조정
                c -= 1

                # 병합 해제
                if (r, c) in mg:
                    for (i, j) in mg[(r, c)]:
                        arr[i][j] = ''  # 병합 해제된 셀 비우기

                    # 원래 셀의 값을 가져와서 복원
                    arr[r][c] = arr[r][c] if arr[r][c] else ''

                mg.pop((r, c), None)  # 병합 정보 삭제

            elif split[0] == 'PRINT':
                r, c = map(int, split[1:])
                r -= 1  # 인덱스 조정
                c -= 1
                if arr[r][c]:
                    answer.append(arr[r][c])
                else:
                    answer.append("EMPTY")
        print(answer)        
        return answer
    

    solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])
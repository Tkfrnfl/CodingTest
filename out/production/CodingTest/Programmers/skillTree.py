def solution(skill, skill_trees):
    
    answer = 0
    

    for i in range(len(skill_trees)):
        tmp_treelist=list(skill_trees[i])
        tmp_skilllist=list(skill)

        tmp_skill=tmp_skilllist.pop(0)

        for j in range(len(tmp_treelist)):
            if tmp_treelist[j] in list(skill):
                if tmp_treelist[j]==tmp_skill:
                    if len(tmp_skilllist)>0:
                        tmp_skill=tmp_skilllist.pop(0)
                    
                else:
                    break
            if j+1==len(tmp_treelist):
                answer+=1
        
    print(answer)
    return answer
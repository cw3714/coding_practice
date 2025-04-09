def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5] 
    
    a_answer = 0
    b_answer = 0
    c_answer = 0
    
    res = []
    
    for i in range(0,len(answers)):
        if a[i % len(a)] == answers[i]:
            a_answer += 1
        if b[i % len(b)] == answers[i]:
            b_answer += 1
        if c[i % len(c)] == answers[i]:
            c_answer += 1
    
    max_score = (max(a_answer,b_answer,c_answer))
    
    answers = [a_answer, b_answer, c_answer]
    for i, answer in enumerate(answers, start=1):
        if answer == max_score:
            res.append(i)
    
        
    
    
    return res
    
    
    
    

    
    
    
    
            
        
    
    
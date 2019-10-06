def solution(record):
    uid_map = {

    }
    enter_map = {
        
    }
    
    answer = []
    
    word_map = {
        "Enter" : "들어왔",
        "Leave" : "나갔",        
    }
    

    for i in range(len(record)-1,0,-1):
        tmp = record[i].split()
        if tmp[0] == "Leave":
            continue       

        action, uid, nick = record[i].split()
        
        keys = uid_map.keys()
        
        if uid not in keys:
            uid_map[uid] = nick
        
        
    

    for s in record:
        tmp = s.split()
        action = tmp[0]
        uid = tmp[1]
        
        if action == "Enter":
            enter_map[uid] = True

        if (action in word_map.keys()) and (enter_map[uid] == True):
            ret = uid_map[uid] + "님이 " + word_map[action] + "습니다."
            
            answer.append(ret)
        

    print(answer)
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 PRodo","Change uid4567 Ryan"]	)
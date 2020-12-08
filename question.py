print("question подключен!")
import youtube_dl

def start(Question, user_id, id):
    x = 0
    for id_user in Question[0]:
        print(id_user)
        if id_user == user_id:
            if id == Question[1][x]:
                print(user_id)
                Question[3].pop(x)
                Question[3].insert(x,'n')
                print(Question)
                id_question = Question[2][x]
                return id_question
        x = x + 1
    return False


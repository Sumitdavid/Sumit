money=(1,2,3,4,5,6,7,8,9)
qstns=("a","b","c","d","e","f","g","h","i")
answers=("a","b","c","d","e","f","g","h","i")
for i in range(0, len(qstns)):
    print("Question is",qstns[i])
    ans = input("Select your option")
    if (answers[i]==ans):
        print("Your answer is correct & you won",money[i])
        # if (qstns[i]==i) & (answers[i]==i):
            # if (answers[i]==i):
            #      print("You are the crorepati")
        if (qstns[i]=="i") & (answers[i]=="i"):
            print("You are the crorepati")
    else:break
    




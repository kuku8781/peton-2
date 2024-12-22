
neme_user = input("как тебя звать ")
print(f"""Мне приятно знать твое имя, {neme_user}! Самое время отправляться в путешествие!
{neme_user}, ты начинаешь игру с 0 очков. В ходе игры ты будешь получаться очки, за которые ты сможешь приобрести интересные вещи и артефакты, которые помогут тебе достичь победы.
За каждый правильный ответ ты будешь получать очки:
за правильный ответ на 1-ое задание: 10 очков
за правильный ответ на 2-ое задание: 20 очков
за правильный ответ на 3-ое задание: 30 очков""")
one_artefact = False
two_artefact = False
three_artefact = False
score = 0
print(f"""и вот первая заагадка выбери правельный ответ:весит груша не льзя суушать: 
1. я не знаю 
2.обычная груша 
3.лампочка """)
answer_one = int(input("выбери 1 2 или 3"))
if answer_one==3:
    one_artefact = True
    score += 10
    print(f"это правельный ответ: +10 очков теперьб у тебя {score} очков  ")
else:
    print("это не правельный ответ ")
print(f"""и вот первая заагадка выбери правельный ответ:весит груша не льзя суушать: 
1. я не знаю 
2.обычная груша 
3.лампочка """)
answer_two = int(input("выбери 1 2 или 3"))
if answer_two==2:
    two_artefact = True
    score += 20
    print(f"это правельный ответ: +20 очков теперьб у тебя {score} очков  ") 
else:
    print("это не правельный ответ ")
print(f"""и вот первая заагадка выбери правельный ответ:весит груша не льзя суушать: 
1. я не знаю 
2.обычная груша 
3.лампочка """)
answer_three = int(input("выбери 1 2 или 3"))
if answer_three==1:
    three_artefact = True
    score += 30
    print(f"это правельный ответ: +30 очков теперьб у тебя {score} очков  ")
else:
    print("это не правельный ответ ")




print(f"ты посторался и получил {score} очков ")
print(f"""ты зороботол свои {score} очков. и решив пойти в могозин не ев три дня купить себе чегонебудь одного 
1 - 10яиц - 10 очков
2 - молоко - 30 очков
3 - хлеб - 5 очьков
4 - красной икры - 1034042 очков
5 - пропустить""")
answer = int(input("выбери 1,2,3,4,5"))
if answer==1 and score >= 10:
    score -= 10
    print("ты купил 10яиц")
elif answer==2 and score >= 30:
    score -= 30
    print("ты купил молоко ")  
elif answer==3 and score >= 5:
    score -= 5
    print("ты купил хлеб ")  
elif answer==4 and score >= 1034042:
    print("ты купил красную икру  ")
elif answer==5:
    print("ты пропустил магазин")
else:
    print("тебе не хвотило денег из за того что ты не устроился на работу")
print(f"у тебя осталось {score} очков ")

if one_artefact == True and two_artefact == True and three_artefact == True :
    print("ты мега супер кросавчик ты выграл ")
elif one_artefact == True and two_artefact == True and three_artefact ==False  :
    print("у тебя не верно третие ")
elif one_artefact == True and two_artefact == False and three_artefact == True :
    print("у тебя не верно второе  ")
elif one_artefact == False and two_artefact == True and three_artefact == True :
    print("у тебя не верно первое ")
elif one_artefact == True and two_artefact == False and three_artefact ==False  :
    print("у тебя не верно второе и третие ")
elif one_artefact == False and two_artefact == False and three_artefact == True :
    print("у тебя не верно первое и второе  ")
elif one_artefact == False and two_artefact == True and three_artefact == False :
    print("у тебя не верно первое и третие ")
else:
    print("у тебя всё не верно ")


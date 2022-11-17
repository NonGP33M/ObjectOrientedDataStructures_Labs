'''

Chapter : 9 - item : 5 - Premier League Score

สร้างฟังก์ชันที่นำชุดข้อมูล(list)ของ football clubs ที่มีคุณสมบัติดังนี้ name, wins, loss, draws, scored, conceded และทำการ return list ของ team name โดยเรียงลำดับทีมที่มีคะแนน(total point)มากที่สุด โดยถ้าหากมีทีมที่คะแนนเท่ากัน ให้นำผลต่างของจำนวนประตูที่ทำได้(scored)กับจำนวนประตูที่เสีย(conceded) มาคิด

***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***

[ชนะได้ 3 คะแนน, เสมอได้ 1 คะแนน, แพ้ได้ 0 คะแนน]

ตัวอย่าง

team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }

Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
Goal Difference = scored - conceded = 88 - 20 = 68

'''

def sortFootballClubs(lists):
    sortedLists = []
    for i in lists:
        templist = []
        templist.append(i[0])
        templist.append({"points":(3*int(i[1])+int(i[3]))}) # 3 * wins + 0 * loss + 1 * draws = 3 * wins + draws
        templist.append({"gd":int(i[4])-int(i[5])})
        sortedLists.append(templist)

    for i in range(len(sortedLists)):
        swapped = False
        for j in range(0,len(sortedLists)-i-1):
            if (sortedLists[j][1].get("points") < sortedLists[j+1][1].get("points"))\
                or (sortedLists[j][1].get("points") == sortedLists[j+1][1].get("points") and sortedLists[j][2].get("gd") < sortedLists[j+1][2].get("gd")):
                sortedLists[j],sortedLists[j+1] = sortedLists[j+1],sortedLists[j]
                swapped = True
        if swapped == False:
            break

    return sortedLists

lists = input("Enter Input : ").split("/")
teamList = []
for i in lists:
    tempList = i.split(",")
    teamList.append(tempList)
answerList = sortFootballClubs(teamList)
print("== results ==")
for i in answerList:
    print(i)
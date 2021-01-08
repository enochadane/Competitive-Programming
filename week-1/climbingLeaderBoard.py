# Not- Optimized

def climbingLeaderboard(ranked, player):
    rank = 1
    playerScore = []
    leaderBoard = ranked
    for i in range(len(player)):
        rank = 1
        bound = len(leaderBoard)
        for j in range(bound):
            if player[i] >= leaderBoard[j]:
                leaderBoard.insert(j, player[i])
                break
            elif player[i] < leaderBoard[bound-1]:
                leaderBoard.append(player[i])
                break
            else:
                continue
        print(leaderBoard)
        for k in range(1, len(ranked), 1):
            if leaderBoard[0] == player[i] and k == 1:
                playerScore.append(rank)
            if leaderBoard[k] != leaderBoard[k-1]:
                rank += 1
                if leaderBoard[k] == player[i]:
                    playerScore.append(rank)
        # print(playerScore)


climbingLeaderboard([1, 1, 2], [1, 1])

# source: Internet

def climbingLeaderboard(ranked, player):
    ranked = sorted(list(set(ranked)), reverse=True)
    player = sorted(player, reverse=True)
    
    l=len(ranked)
    j=0
    
    ans=[]
    for i in range(len(player)):
        while j<l and player[i]<ranked[j]:
            j+=1
        
        ans.append(j+1)
        
    return ans[::-1]

climbingLeaderboard([100, 90, 90, 80], [70, 80, 105])
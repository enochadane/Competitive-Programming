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

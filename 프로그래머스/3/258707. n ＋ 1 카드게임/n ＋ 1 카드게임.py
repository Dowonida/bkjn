from heapq import heappop, heappush
def solution(coin, cards):
    n = len(cards)
    N = n+1
    # draw에 짝 없는 카드 추가
    # pair에는 [(비용,번호)]로 힙 저장
    # 1. 카드를 최대한 뽑기
    # 2. pair에서 카드 가져오기
    # 위 작업을 코인이 떨어질 때까지 반복
    # 조건을 따로 걸기 귀찮으니까 엄청 비싼 조커 카드를 추가해두자.
    pair = [(100000,0)]
    draw = set()
    hand = set()
    answer = 1
    for i in range(n//3):
        card = cards[i]
        if N-card in hand:
            answer += 1
        else:
            hand.add(card)
    print(answer)
    cur_idx = n//3
    while coin:
        
        for i in range(cur_idx,min(n,n//3+2*answer)):
            card = cards[i]
            
            if N-card in hand:
                heappush(pair, (1,card))
            elif N-card in draw:
                heappush(pair, (2,card))
            else:
                draw.add(card)
            
        val, num = heappop(pair)

        if val>coin:
            break
        cur_idx = n//3+2*answer
        coin -= val
        answer += 1

    return min(n//3+1,answer)



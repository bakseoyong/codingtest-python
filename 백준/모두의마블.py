if __name__ == '__main__':
    n = int(input())

    cards = list(map(int, input().split()))

    cards.sort(reverse=True)

    answer = 0
    card_0 = cards[0]

    for i in range(1, len(cards)):
        answer += card_0 + cards[i]

    print(answer)

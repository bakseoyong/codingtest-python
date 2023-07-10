if __name__ == '__main__':
    X, Y, W, S = map(int, input().split())

    if 2 * W < S:
        print((X + Y) * W)
    else:
        if W > S:
            print(min(X, Y) * S + (max(X, Y) - min(X, Y)) // 2 * S * 2 + (max(X, Y) - min(X, Y)) % 2 * W)
        else:
            print(min(X, Y) * S + (max(X, Y) - min(X, Y)) * W )
def solution(words):
    #트라이 구현 연습
    answer = 0

    tree = {}

    #트라이 트리 구조 만들기
    for word in words:
        cur_tree = tree

        for w in word:
            cur_tree.setdefault(w, [0, {}])
            cur_tree[w][0] += 1
            cur_tree = cur_tree[w][1]

    #탐색
    for word in words:
        cur_tree = tree

        for index in range(len(word)):
            if cur_tree[word[index]][0] == 1:
                break

            cur_tree = cur_tree[word[index]][1]

        answer += (index + 1)


    return answer






if __name__ == '__main__':
    words = ["go", "gone", "guild"]

    solution(words)
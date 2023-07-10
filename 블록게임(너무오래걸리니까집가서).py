def solution(board):
    answer = 0

    width = len(board[0])
    height = len(board)
    #print('width and height', width, height)
    #우선 삭제할 수 있는 블록인지 판단하기


    #블록 모양 배열을 만들고 식별해야 하는데
    #[ [이동], 삭제가능여부, 최초 판별 기준 몇번째 칸 위가 비워져 있어야 하는지 ]
    blocks = [
        [[(1, 0), (1, 0), (0, 1)], 0, [0], 0],
        [[(1, 0), (-1, 0), (0, 1), (0, 1)], 0, [0], 1],
        [[(0, 1), (1, 0), (1, 0)], 1, [(0, 1), (0, 2)], 2],
        [[(0, 1), (0, 1), (-1, 0)], 1, [(0, -1), (1, -1)], 3],

        [[(0, 1), (0, -1), (1, 0), (1, 0)], 0, [0], 4],
        [[(0, 1), (0, 1), (1, 0)], 1, [(0, 1), (1, 1)], 5],
        [[(0, 1), (-1, 0), (-1, 0)], 1, [(0, -2), (0, -1)], 6],
        [[(1, 0), (0, 1), (0, 1)], 0, [0], 7],

        [[(0, 1), (-1, 0), (1, 0), (1, 0)], 1, [(0, -1), (0, 1)], 8],
        [[(0, 1), (1, 0), (-1, 0), (0, 1)], 0, [0], 9], #(x, y) 순서쌍이 잖아.
        [[(1, 0), (1, 0), (-1, 0), (0, 1)], 0, [0], 10],
        [[(0, 1), (-1, 0), (1, 0), (0, 1)], 0, [0], 11]
     ]

    #dfs 처럼 해야지
    def isThisBlock(moves, num):
        move_y = i
        move_x = j
        for move in moves:
            # 이동 가능 판단
            # not 에 괄호 안써주면 and 앞까지만 적용됨.
            if not (0 <= move_y + move[1] < width and 0 <= move_x + move[0] < height):
                return False

            #여기서 뜨는 이유가 뭐지 위에서 False라고 식별을 하는데...
            if board[move_y + move[1]][move_x + move[0]] != num:
                return False

            move_y += move[1]
            move_x += move[0]

        return True

    def tempOrDelete():
        nonlocal possible_blocks, answer

        for empty_space in empty_spaces:
            y = i + empty_space[0]
            x = j + empty_space[1]

            # 범위 안에 해당하는지 안봐도 블럭 탐색할때 이미 했으니까 상관없겠다.
            # if not (0 <= y < height and 0 <= x < width):
            #     possible_blocks.add((num, i, j))
            #     break
            for p in range(0, y):
                if board[p][x] != num:
                    possible_blocks.add((num, i, j, index))
                    return False
        #삭제하고 answer 늘리기
        #배열 따라 가며 삭제하고

        answer += 1

    impossible_blocks = set()
    possible_blocks = set()

    for i in range(0, len(board[0])): #세로
        for j in range(0, len(board)): #가로
            #0이 아닌 수를 탐색하기
            if board[i][j] != 0:
                num = board[i][j]
                #print(num)
                #탐색시작
                for moves, isPossible, empty_spaces, index in blocks:
                    #이 블록이 맞다면
                    if isThisBlock(moves, num):
                        4는 불가능 하니까 패스하고 그다음 3인데 3은 가능하긴 하다. 가능 하면 이제 위에 막는게 없는지 찾아야 한다.
                        3의 탐색이 시작된 부분 기준으로 해서 x + 몇칸 까지는 위가 비워져 있어야 하는지 보면 되겠다.

                        배열로 저장해놨으니까 그만큼 순회를 볼면서 그 위가 비워져있는지 확인.
                        비워져있으면 지울 수 있는 칸으로 보고
                        result값 1 올리고 블럭은 삭제

                        #삭제 불가능한 블럭은 불가능 Set에 저장
                        if isPossible == 0:
                            impossible_blocks.add((num, i, j, index))
                            break
                        #삭제 '가능성이 있는' 블럭은 가능 Set에 저장
                        else:
                            #바로 삭제가 가능한지 확인해보자 ( 위에 막고 있는 블럭이 없는지 확인해 보자)
                            tempOrDelete(empty_spaces)




    return answer

if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
     [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
     [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]

    solution(board)
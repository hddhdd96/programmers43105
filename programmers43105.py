def solution(triangle):
    # 왼쪽 아래로 and 오른쪽 아래로 대각선
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i - 1][0]
        triangle[i][i] += triangle[i - 1][i - 1]

    # 가운데 작은 삼각형
    for i in range(2, len(triangle)):
        for j in range(1, i):
            if triangle[i - 1][j - 1] >= triangle[i - 1][j]:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += triangle[i - 1][j]

    answer = max(triangle[len(triangle) - 1])

    return answer


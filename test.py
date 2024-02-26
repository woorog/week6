from collections import deque

# 입력
n, hp, drink = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
q = deque([(6, 3, hp)])  # 시작 위치 (y, x) 및 체력
visited = [[False for _ in range(n)] for _ in range(n)]
visited[6][3] = True
max_mint_choco = 0

# 이동 가능한 방향 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    y, x, cur_hp = q.popleft()

    if cur_hp < 0:  # 현재 체력이 0 이하면 더 이상 탐색 중지
        continue

    # 현재 위치에서 민트초코우유를 마시는 경우
    if board[y][x] == 2:
        cur_hp += drink  # 체력 회복
        max_mint_choco += 1  # 마신 민트초코우유 수 증가
        board[y][x] = 0  # 민트초코우유를 마셨으므로 지도에서 제거

    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            visited[ny][nx] = True
            q.append((ny, nx, cur_hp - 1))  # 이동 후 체력 1 감소

# 최대로 마실 수 있는 민트초코우유의 수 출력
print(max_mint_choco)
def main():
    N,K = map(int,input().split())

    MAX = (N-1) * (N-2) //2
    if K>MAX:
        print(-1)
        return

    extra_edges = MAX - K
    graph = []
    # スター(距離2の辺の数を最大にする)
    for i in range(2,N+1):
        graph.append([1,i])
    # 距離2の頂点同士を繋ぐ
    cnt = 0
    for i in range(2,N):
        for j in range(i+1,N+1):
            if cnt >= extra_edges:
                continue
            graph.append([i,j])
            cnt += 1
    print(len(graph))
    for x,y in graph:
        print(x,y)

if __name__ == "__main__":
    main()

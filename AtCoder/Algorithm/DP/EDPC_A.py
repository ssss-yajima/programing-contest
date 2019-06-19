'''
https://atcoder.jp/contests/dp/tasks/dp_a
'''
N = int(input())
H = list(map(int,input().split()))

def main():
    if N==2:
        print(abs(H[1] - H[0]))
        return

    costs = [0 for _ in range(N)]
    costs[1] = abs(H[1]-H[0])
    costs[2] = min(costs[0] + abs(H[1]-H[0]), abs(H[2]-H[0])) # 0>1>2と0>2のmin

    for i in range(2,N):
        step_1 = abs(H[i] - H[i-1]) # 1段上る
        step_2 = abs(H[i] - H[i-2]) # 2段上る
        # 漸化式 fn = min(fn-1, fn-2)
        costs[i] = min(costs[i-1] + step_1, costs[i-2] + step_2) 
    print(costs[-1])
    

if __name__ == "__main__":
    main()

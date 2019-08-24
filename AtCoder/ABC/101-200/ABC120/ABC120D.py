n,m = map(int, input().split())
edge = [list(map(lambda x:x-1,map(int, input().split()))) for _ in range(m)]

class UnionFind:
    def __init__(self,size):
        self.table = [x for x in range(size)]
        
    def unite(self, u, v):
        if self.table[u] != self.table[v]:
            target_group = self.table[v]
            for i in range(len(self.table)):
                if self.table[i] == target_group:
                    self.table[i] = u
            # print(u,v,self.table)

    def find(self, u):
        return self.table[u]

    def size(self, u):
        return self.table.count(u)

uf = UnionFind(n)
cost = n*(n-1)//2
costs = [cost]
for e in edge[:-1]:
    cost = cost - (uf.size(uf.find(e[0])) * uf.size(uf.find(e[1])))
    costs += [max(0, cost)]
    uf.unite(e[0], e[1])

for c in costs[::-1]:
    print(c)
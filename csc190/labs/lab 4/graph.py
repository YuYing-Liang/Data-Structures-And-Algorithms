class graph:

    def __init__(self):
        self.store = []
        # store is in form [[[to index #, weight]], [], [] ...]

    def addVertex(self, n):
        for i in range(len(self.store), len(self.store) + n, 1):
            self.store += [[i, []]]

        return len(self.store)

    def addEdge(self, from_idx, to_idx, directed, weight):
        if weight <= 0 or not(0 <= from_idx < len(self.store) and 0 <= to_idx < len(self.store)):
            return False

        self.store[from_idx][1] += [[to_idx, weight]]
        if directed:
            self.store[to_idx][1] += [[from_idx, weight]]
        return True

    def traverse(self, start, typeBreadth):
        # True = Breadth, False = Depth

        C = []
        D = []
        P = []
        # Breadth = queue, Depth = stack

        for i in range(len(self.store)):
            D += [False]
            P += [False]

        if start is None:
            return_list = []

            for i in range(len(self.store)):
                r_list = []
                if not D[i]:
                    C += [self.store[i]]
                    D[i] = True

                while len(C) > 0:
                    w = 0
                    if typeBreadth:
                        w = C[0]
                        C = C[1:len(C)]
                    else:
                        w = C[len(C) - 1]
                        C = C[0:len(C) - 1]

                    if not P[w[0]]:
                        r_list += [w[0]]
                        P[w[0]] = True

                    for x in range(len(w[1])):
                        if not D[w[1][x][0]]:
                            C += [self.store[w[1][x][0]]]
                            D[w[1][x][0]] = True

                if r_list != []:
                    return_list += [r_list]

            return return_list

        elif 0 <= start < len(self.store):
            r_list = []

            if not D[start]:
                C += [self.store[start]]
                D[start] = True

            while len(C) > 0:
                w = 0
                if typeBreadth:
                    w = C[0]
                    C = C[1:len(C)]
                else:
                    w = C[len(C) - 1]
                    C = C[0:len(C) - 1]

                if not P[w[0]]:
                    r_list += [w[0]]
                    P[w[0]] = True

                for x in range(len(w[1])):
                    if not D[w[1][x][0]]:
                        C += [self.store[w[1][x][0]]]
                        D[w[1][x][0]] = True
            return r_list
        return []

    def connectivity(self, vx, vy):
        is_path_vx_to_vy = False
        is_path_vy_to_vx = False

        # Depth-Order Traversal indicated whether vx and vy are connected
        path = list(self.traverse(vx, False))
        for i in path:
            if i == vy:
                is_path_vx_to_vy = True

        path = list(self.traverse(vy, False))
        for i in path:
            if i == vx:
                is_path_vy_to_vx = True

        return [is_path_vx_to_vy, is_path_vy_to_vx]

    def path(self, vx, vy):
        # paths = self.connectivity(vx, vy)
        path_vx_vy = []
        path_vy_vx = []

        path_vx_vy = self.path_helper(self.store, vx, vy, path_vx_vy)
        path_vy_vx = self.path_helper(self.store, vy, vx, path_vy_vx)
        return [path_vx_vy, path_vy_vx]

    def path_helper(self, graph, vx, vy, path=[]):
        if not(0 < vx < len(self.store)) and not(0 < vy < len(self.store)):
            return []

        path = path + [vx]
        if vx == vy:
            return path

        for i in range(len(graph[vx][1])):
            if len(graph[vx][1]) > 0:
                if graph[vx][1][i][0] not in path:
                    new_path = self.path_helper(graph, graph[vx][1][i][0], vy, path)
                    if new_path:
                        return new_path
        return []


grid = [
['X','X','X','X','X','X','X'],
['X',2,0,0,0,0,'X'],
['X',0,3,0,3,0,'X'],
['X',0,0,0,0,0,'X'],
['X',0,3,0,3,0,'X'],
['X',0,3,1,3,0,'X'],
['X','X','X','X','X','X','X']
]


INF=1000000

def is_valid(grid:list):
    ends = 0
    starts = 0
    for line in grid:
        for el in line:
            if el==2:
                ends+=1
            if el==1:
                starts+=1
    return False if ends!=1 or starts!=1 else True

def redef_grid(grid:list):
    ''' Deleting from grid all 'X' '''
    g=grid.copy()
    if 'X' in g[0]: del g[0]
    if 'X' in g[-1]: del g[-1]
    for line in g:
        while 'X' in line:
            line.remove('X')
    return g

def uni_index(grid:list, pos:tuple):
    return len(grid[0])*pos[0]+pos[1]

def real_index(grid:list, index:int):
    row =index//len(grid[0])
    col=index-row*len(grid[0])
    return (row, col)

def get_neibs(grid:list, index:int):
    def get_vertical(grid:list, index:int):
        return [index+k for k in [len(grid[0]), -len(grid[0])] if index+k>=0 and index+k<uni_index(grid, (len(grid)-1, len(grid[0])-1))]
    def get_horizontal(grid:list, index:int):
        return [index+k for k in [1, -1] if index+k>=(index//len(grid[0]))*(len(grid[0])) and index+k<=uni_index(grid, (index//len(grid[0]), len(grid[0])-1))]
    return get_vertical(grid, index)+get_horizontal(grid, index)

def get_matrix(grid:list):
    last_el = uni_index(grid, (len(grid)-1, len(grid[0])-1))
    elements=len(grid[0])*len(grid)
    matrix=[[INF for _ in range(elements)] for _ in range(elements)]
    for index in range(last_el):
        neibs=get_neibs(grid, index)
        neibs=[neib for neib in neibs if grid[real_index(grid, neib)[0]][real_index(grid, neib)[1]]!=3]
        for neib in neibs:
            matrix[index][neib]=1
    return matrix

def get_start(grid:list):
    for i in range(len(grid)):
        try:
            return (i, grid[i].index(1))
        except ValueError:
            pass

def get_end(grid:list):
    for i in range(len(grid)):
        try:
            return (i, grid[i].index(2))
        except ValueError:
            pass

def Dijkstra(N, S, matrix):
    valid = [True]*N
    weight = [1000000]*N
    weight[S] = 0
    for i in range(N):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(N):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight

grid=redef_grid(grid)
if is_valid(grid):
    matrix=get_matrix(grid)
    paths = Dijkstra(len(grid)*len(grid[0]), uni_index(grid, get_start(grid)), matrix)
    shortest_path = paths[uni_index(grid, get_end(grid))]
    if shortest_path==INF: shortest_path='No solution'
    print(shortest_path)
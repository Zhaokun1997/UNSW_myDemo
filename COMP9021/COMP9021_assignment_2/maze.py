# COMP9021 19T3 - Rachid Hamadi
# Assignment 2 *** Due Sunday Week 10


import copy as cp
import numpy as np
import sys
import os


class MazeError(Exception):
    def __init__(self, message):
        self.message = message


class Maze(object):
    # 类属性
    file_name = ""
    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 方向：上左下右
    # x_dim = 2  # x_dim 应当满足 2 <= x_dim <= 31 --- columns nb
    # y_dim = 2  # y_dim 应当满足 2 <= y_dim <= 41 --- rows nb

    # 地图文件的矩阵
    maze_matrix = []

    # gates
    gates = set()  # 记录门的点
    nb_gates = 0  # 门的数量

    # walls
    # *******要求记录点*******
    walls = []
    nb_walls = 0  # 墙的数量

    # pillar
    # *******要求记录点*******
    pillars = []  # 记录柱子的点
    nb_pillars = 0  # 记录柱子的数量

    # accessible areas
    nb_accessible_areas = 0  # 可连通区域的数量

    # inaccessible inner points
    inaccessible_inner_points = []
    nb_inaccessible_inner_points = 0  # 不可访问的内部点的数量

    # accessible cul-de-sacs
    # *******要求记录点*******
    accessible_cul_de_sacs = []  # 真正的访问点
    nb_accessible_cul_de_sacs = 0  # 可访问的死路的数量

    # entry-exit path
    # *******要求记录点*******
    entry_eixt_path = []  # 记录连线的点
    nb_entry_exit_path = 0  # 可出入路径的数量 ----要求记录点

    # 构造方法
    def __init__(self, filename):
        try:
            self.file_name = filename
            with open(filename, 'r') as maze_data:
                lines = maze_data.readlines()
                for line in lines:
                    if not line.isspace():  # 判断是否是空格
                        each_row = ''.join(line.split())
                        self.maze_matrix.append(list(each_row))
                self.x_dim = len(self.maze_matrix[0])
                self.y_dim = len(self.maze_matrix)
                # 初步检测：矩阵是否符合格式
                if self.check_matrix_valid():
                    if self.check_boundary_valid():
                        pass
                    else:
                        raise MazeError('Input does not represent a maze.')
                else:
                    raise MazeError('Incorrect input.')
        # except MazeError as me:
        #     print(me.message)
        #     sys.exit()
        except FileNotFoundError:
            print('File does not exist!')
            sys.exit()

    # 判断 maze_n.txt 文件是否符合正确的矩阵格式
    def check_matrix_valid(self):
        # print('row number of this maze is : ', len(self.maze_matrix))
        column_num = []  # 记录每一行的列数， 便于后面判断所有列数是否相等
        # check_1:
        if 2 <= len(self.maze_matrix) <= 41:
            for line in self.maze_matrix:
                if 2 <= len(line) <= 31:
                    continue
                else:
                    return False
        else:
            return False

        # check_2:
        for line in self.maze_matrix:
            column_num.append(len(line))
        # print('every column num is : ', column_num)
        for num in column_num:
            if num != column_num[0]:
                return False

        # check_3:
        for line in self.maze_matrix:
            for digit in line:
                if digit not in ['0', '1', '2', '3']:
                    return False

        return True

    # 判断边界是否符合正确的格式
    def check_boundary_valid(self):
        for line in self.maze_matrix:
            if line[-1] == '1' or line[-1] == '3':
                return False
        for digit in self.maze_matrix[len(self.maze_matrix) - 1]:
            if digit == '2' or digit == '3':
                return False
        return True

    # 创建九宫格地图
    def create_grid_view(self, code_dic):
        # 记录九宫格中的每行数据
        rows = []
        for line in self.maze_matrix:
            temp_row = code_dic[line[0]]
            for j in range(1, len(line)):
                temp_row = np.hstack((temp_row, code_dic[line[j]]))  # 水平堆叠九宫格
            rows.append(temp_row)

        # 对应的九宫格地图
        grid_view = rows[0]
        for i in range(1, len(rows)):
            grid_view = np.vstack((grid_view, rows[i]))  # 垂直堆叠九宫格

        # 最终版本9宫格，去掉了边缘两列两行
        final_grid_view = grid_view[0:self.y_dim * 3 - 2, 0:self.x_dim * 3 - 2]

        # print('after converting to grid_view : ')
        # for line in final_grid_view:
        #     print(*line)

        return final_grid_view

    # 找门的位置以及个数
    def get_gates(self, code_dic):
        grid_view = self.create_grid_view(code_dic)
        # 地图细化平滑处理
        for i in range(self.y_dim * 3 - 2):
            for j in range(self.x_dim * 3 - 2):
                if grid_view[i][j] == 0:
                    count_neighber_1 = 0
                    for i_dir, j_dir in self.direction:
                        if 0 <= i + i_dir < self.y_dim * 3 - 2 \
                                and 0 <= j + j_dir < self.x_dim * 3 - 2 \
                                and grid_view[i + i_dir][j + j_dir] == 1:
                            count_neighber_1 += 1
                    if count_neighber_1 == 3:
                        grid_view[i][j] = 1
        # print('finally converting to grid_view : ')
        # for line in grid_view:
        #     print(*line)
        up_side = grid_view[0, 0:len(grid_view[0])]
        right_side = grid_view[0:len(grid_view), len(grid_view[0]) - 1]
        down_side = grid_view[len(grid_view) - 1, 0:len(grid_view[0])]
        left_side = grid_view[0:len(grid_view), 0]

        # 获取门的坐标
        for i in range(len(up_side)):
            if up_side[i] == 0:
                self.gates.add((0, i))
        for j in range(len(right_side)):
            if right_side[j] == 0:
                self.gates.add((j, len(grid_view[0]) - 1))
        for i in range(len(down_side)):
            if down_side[i] == 0:
                self.gates.add((len(grid_view) - 1, i))
        for j in range(len(left_side)):
            if left_side[j] == 0:
                self.gates.add((j, 0))

        array = np.array(grid_view)
        array_T = array.T

        hori_walls = []
        for i in range(len(array)):
            j = 0
            if i % 3 == 0:
                while j < len(array[0]):
                    temp = []
                    length_wall = 0
                    if j % 3 == 0:
                        while array[i][j] == 1:
                            temp.append((i, j))
                            length_wall += 1
                            if j < len(array[0]) - 1:
                                j += 1
                            else:
                                break
                    if length_wall > 2:
                        hori_walls.append(temp)
                    if j < len(array[0]) - 1:
                        j += 1
                    else:
                        break
        vert_walls = []
        for i in range(len(array_T)):
            j = 0
            if i % 3 == 0:
                while j < len(array_T[0]):
                    temp = []
                    length_wall = 0
                    if j % 3 == 0:
                        while array_T[i][j] == 1:
                            temp.append((j, i))
                            length_wall += 1
                            if j < len(array_T[0]) - 1:
                                j += 1
                            else:
                                break
                    if length_wall > 2:
                        vert_walls.append(temp)
                    if j < len(array_T[0]) - 1:
                        j += 1
                    else:
                        break
        walls = []
        for hori_wall in hori_walls:
            walls.append(hori_wall)
            # print(hori_wall)
        for vert_wall in vert_walls:
            walls.append(vert_wall)
            # print(vert_wall)
        # 计算门的个数
        self.nb_gates = list(up_side).count(0) + list(right_side).count(0) \
                        + list(down_side).count(0) + list(left_side).count(0)

        for wall in walls:
            start_point = (wall[0][1] // 3, wall[0][0] // 3)
            end_point = (wall[-1][1] // 3, wall[-1][0] // 3)
            seg = [start_point, end_point]
            self.walls.append(seg)

    # 找到墙的个数
    def get_walls(self, code_dic):
        grid_view = self.create_grid_view(code_dic)
        # 地图细化平滑处理
        for i in range(self.y_dim * 3 - 2):
            for j in range(self.x_dim * 3 - 2):
                if 0 <= i + 1 < len(grid_view) and 0 <= j + 1 < len(grid_view[0]):
                    if grid_view[i][j] == 1 and grid_view[i - 1][j + 1] == 1 \
                            and grid_view[i][j + 1] == 0 and grid_view[i + 1][j] == 0:
                        grid_view[i][j + 1] = 1
                elif i + 1 == len(grid_view) and 0 <= j + 1 < len(grid_view[0]):
                    if grid_view[i][j] == 1 and grid_view[i - 1][j + 1] == 1 \
                            and grid_view[i][j + 1] == 0:
                        grid_view[i][j + 1] = 1
        # print('finally converting to grid_view : ')
        # for line in grid_view:
        #     print(*line)
        color_index = 2
        cp_grid = cp.deepcopy(grid_view)
        for i in range(len(cp_grid)):
            for j in range(len(cp_grid[i])):
                if cp_grid[i][j] == 1:  # 即还没有被染色
                    self.find_walls(i, j, color_index, cp_grid)
                    color_index += 1  # 染色完毕之后，换颜色

        nb_walls = color_index - 2
        return nb_walls

    # 递归找墙
    def find_walls(self, i, j, color_index, cp_grid):
        i_dim = len(cp_grid)
        j_dim = len(cp_grid[0])
        if 0 <= i < i_dim and 0 <= j < j_dim and cp_grid[i][j] == 1:
            cp_grid[i][j] = color_index
            for i_dir, j_dir in self.direction:
                self.find_walls(i + i_dir, j + j_dir, color_index, cp_grid)
        else:
            return

    # 找柱子
    def get_pillars(self):
        matrix = cp.deepcopy(self.maze_matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    if 0 < i < len(matrix) and 0 < j < len(matrix[0]):
                        if (matrix[i - 1][j] != '2' and matrix[i - 1][j] != '3') \
                                and (matrix[i][j - 1] != '1' and matrix[i][j - 1] != '3'):
                            self.pillars.append((j, i))
                            self.nb_pillars += 1
                    elif i == 0 and j == 0:
                        self.pillars.append((j, i))
                        self.nb_pillars += 1
                    elif i == 0 and j != 0:
                        if 0 <= j - 1 < len(matrix[0]):
                            if matrix[i][j - 1] != '1' and matrix[i][j - 1] != '3':
                                self.pillars.append((j, i))
                                self.nb_pillars += 1
                    elif i != 0 and j == 0:
                        if 0 <= i - 1 < len(matrix[0]):
                            if matrix[i - 1][j] != '2' and matrix[i - 1][j] != '3':
                                self.pillars.append((j, i))
                                self.nb_pillars += 1

    # 找可连通区域和内部点
    def get_accessible_areas_and_inaccessible_inner_point(self, code_dic):
        grid_view = self.create_grid_view(code_dic)
        # 地图细化平滑处理
        for i in range(self.y_dim * 3 - 2):
            for j in range(self.x_dim * 3 - 2):
                if grid_view[i][j] == 0:
                    count_neighber_1 = 0
                    for i_dir, j_dir in self.direction:
                        if 0 <= i + i_dir < self.y_dim * 3 - 2 \
                                and 0 <= j + j_dir < self.x_dim * 3 - 2 \
                                and grid_view[i + i_dir][j + j_dir] == 1:
                            count_neighber_1 += 1
                    if count_neighber_1 == 3:
                        grid_view[i][j] = 1
        # print('finally converting to grid_view : ')
        # for line in grid_view:
        #     print(*line)

        # 递归可连通区域
        acc_flag = 2
        for x, y in self.gates:
            if grid_view[x][y] == 0:
                self.find_path(x, y, acc_flag, grid_view)
                acc_flag += 1
        # print('show the accessible areas of grid_view : ')
        # for line in grid_view:
        #     print(*line)
        self.nb_accessible_areas = acc_flag - 2
        # 记录所有的候选点

        m = np.array(grid_view)
        for element in np.argwhere(m == 0):  # 九宫格中选出所有不可达的内部点的坐标
            x = element[0]
            y = element[1]
            self.inaccessible_inner_points.append((x, y))

        temp_inner_points = []
        for line in np.argwhere(m == 0):
            x = line[0] // 3 + 0.5
            y = line[1] // 3 + 0.5
            temp_inner_points.append((x, y))
        inner_points = set(temp_inner_points)
        self.nb_inaccessible_inner_points = len(inner_points)

    # 递归找路径
    def find_path(self, x, y, acc_flag, grid_view):
        i_dim = len(grid_view)
        j_dim = len(grid_view[0])
        if (0 <= x < i_dim) and (0 <= y < j_dim) and (grid_view[x][y] == 0):
            grid_view[x][y] = acc_flag
            for i_dir, j_dir in self.direction:
                self.find_path(x + i_dir, y + j_dir, acc_flag, grid_view)
        else:
            return

    # 找死路和进出口通路
    def get_accessible_cul_de_sacs_and_entry_exit_paths(self, code_dic):
        grid_view = self.create_grid_view(code_dic)
        # 地图细化平滑处理
        for i in range(self.y_dim * 3 - 2):
            for j in range(self.x_dim * 3 - 2):
                if grid_view[i][j] == 0:
                    count_neighber_1 = 0
                    for i_dir, j_dir in self.direction:
                        if 0 <= i + i_dir < self.y_dim * 3 - 2 \
                                and 0 <= j + j_dir < self.x_dim * 3 - 2 \
                                and grid_view[i + i_dir][j + j_dir] == 1:
                            count_neighber_1 += 1
                    if count_neighber_1 == 3:
                        grid_view[i][j] = 1
        # print('finally converting to grid_view : ')
        # for line in grid_view:
        #     print(*line)

        # 填充内部不可访问点
        for i, j in self.inaccessible_inner_points:
            grid_view[i][j] = 1
        # print('after updating the grid_view : ')
        # for line in grid_view:
        #     print(*line)

        # 递归找死路
        for i in range(len(grid_view)):
            for j in range(len(grid_view[0])):
                if grid_view[i][j] == 0:
                    self.mark_dead_points(i, j, grid_view)
                    for x_dir, y_dir in self.direction:
                        self.mark_dead_points(i + x_dir, j + y_dir, grid_view)

        # 复制死路版本的地图
        # 找死路的个数 并 标记所有的死胡同
        dead_path_version_grid = cp.deepcopy(grid_view)
        # print('after marking the dead path : ')
        # for line in dead_path_version_grid:
        #     print(*line)
        cul_de_sacs_points = []
        for i in range(len(dead_path_version_grid)):
            for j in range(len(dead_path_version_grid[0])):
                if dead_path_version_grid[i][j] == 2 and i % 3 == 1 and j % 3 == 1:
                    cul_de_sacs_points.append((j // 3 + 0.5, i // 3 + 0.5))
        self.accessible_cul_de_sacs = cul_de_sacs_points
        # print('accessible_cul_de_sacs points set is : ')
        # print(self.accessible_cul_de_sacs)
        nb_index = 3
        for i in range(len(dead_path_version_grid)):
            for j in range(len(dead_path_version_grid[0])):
                if dead_path_version_grid[i][j] == 2:
                    self.find_dead_path(i, j, nb_index, dead_path_version_grid)
                    nb_index += 1
        self.nb_accessible_cul_de_sacs = nb_index - 3

        # 所有的候选路径
        all_paths = []
        for x, y in self.gates:
            temp_path = []
            self.mark_possible_path(x, y, grid_view, temp_path)
            if temp_path:
                all_paths.append(temp_path)
        # print()
        # print('after marking all possible path : ')
        # for line in grid_view:
        #     print(*line)
        # for path in all_paths:
        #     print(path)

        # 寻找路径中包含门的数量是多少
        final_paths = []
        for path in all_paths:
            count_gates = 0
            for point in path:
                if point in self.gates:
                    count_gates += 1
            if count_gates == 2 and self.have_no_interaction(path, grid_view):  # 是候选路径
                final_paths.append(path)
        # print('the final path is : ')
        # for path in final_paths:
        #     print(path)


        final_grid = cp.deepcopy(grid_view)
        self.nb_entry_exit_path = len(final_paths)

        for path in final_paths:
            for i, j in path:
                final_grid[i][j] = 4

        array = np.array(final_grid)
        array_T = array.T

        hori_paths = []
        for i in range(len(array)):
            j = 0
            while j < len(array[0]):
                temp = []
                length_path = 0
                while array[i][j] == 4:
                    temp.append((i, j))
                    length_path += 1
                    if j < len(array[0]) - 1:
                        j += 1
                    else:
                        break
                if length_path >= 2:
                    hori_paths.append(temp)
                if j < len(array[0]) - 1:
                    j += 1
                else:
                    break
        vert_paths = []
        for i in range(len(array_T)):
            j = 0
            while j < len(array_T[0]):
                temp = []
                length_path = 0
                while array_T[i][j] == 4:
                    temp.append((j, i))
                    length_path += 1
                    if j < len(array_T[0]) - 1:
                        j += 1
                    else:
                        break
                if length_path >= 2:
                    vert_paths.append(temp)
                if j < len(array_T[0]) - 1:
                    j += 1
                else:
                    break
        valid_paths = []
        for hori_path in hori_paths:
            start_point = [hori_path[0][0] // 3 + 0.5, hori_path[0][1] // 3 + 0.5]
            end_point = [hori_path[-1][0] // 3 + 0.5, hori_path[-1][1] // 3 + 0.5]
            if start_point[1] == 0.5 and hori_path[0][1] % 3 == 0:  # 最左侧的出口
                start_point[1] -= 1
            seg = [start_point, end_point]
            valid_paths.append(seg)
        for vert_path in vert_paths:
            start_point = [vert_path[0][0] // 3 + 0.5, vert_path[0][1] // 3 + 0.5]
            end_point = [vert_path[-1][0] // 3 + 0.5, vert_path[-1][1] // 3 + 0.5]
            if start_point[0] == 0.5 and vert_path[0][0] % 3 == 0:
                start_point[0] -= 1
            seg = [start_point, end_point]
            valid_paths.append(seg)
        for sgm in valid_paths:
            temp_seg = []
            for e in sgm:
                temp_seg.append((e[1], e[0]))
            self.entry_eixt_path.append(temp_seg)

    # 判断是否存在交叉点
    def have_no_interaction(self, path, grid_view):
        for (x, y) in path:
            deep_count = 0
            for x_dir, y_dir in self.direction:
                if (0 <= x + x_dir < len(grid_view)) and (0 <= y + y_dir < len(grid_view[0])) and grid_view[x + x_dir][
                    y + y_dir] == 3:
                    deep_count += 1
            if deep_count == 3:
                return False
        return True

    # 标记可能路径
    def mark_possible_path(self, x, y, grid_view, temp_path):
        if (0 <= x < len(grid_view)) and (0 <= y < len(grid_view[0])) and grid_view[x][y] == 0:
            temp_path.append((x, y))
            grid_view[x][y] = 3
            for x_dir, y_dir in self.direction:
                self.mark_possible_path(x + x_dir, y + y_dir, grid_view, temp_path)
        else:
            return

    # 标记对应的死路路径
    def find_dead_path(self, i, j, nb_index, dead_path_version_grid):
        i_dim = len(dead_path_version_grid)
        j_dim = len(dead_path_version_grid[0])
        if (0 <= i < i_dim) and (0 <= j < j_dim) and (dead_path_version_grid[i][j] == 2):
            dead_path_version_grid[i][j] = nb_index
            for i_dir, j_dir in self.direction:
                self.find_dead_path(i + i_dir, j + j_dir, nb_index, dead_path_version_grid)
        else:
            return

    # 标记死路对应的点
    def mark_dead_points(self, i, j, grid_view):
        if (0 <= i < len(grid_view)) and (0 <= j < len(grid_view[0])) and grid_view[i][j] == 0:
            count = 0
            for x_dir, y_dir in self.direction:
                if 0 <= i + x_dir < len(grid_view) and 0 <= j + y_dir < len(grid_view[0]):
                    if grid_view[i + x_dir][j + y_dir] >= 1:
                        count += 1

                else:  # 越界了
                    pass
            if count == 3:
                grid_view[i][j] = 2
                for x_dir, y_dir in self.direction:
                    self.mark_dead_points(i + x_dir, j + y_dir, grid_view)
            return
        else:
            return

    # 输出所有性质
    def attribute_display(self):

        if self.nb_gates == 0:
            print(f'The maze has no gate.')
        elif self.nb_gates == 1:
            print(f'The maze has a single gate.')
        elif self.nb_gates > 1:
            print(f'The maze has {self.nb_gates} gates.')

        if self.nb_walls == 0:
            print(f'The maze has no wall.')
        elif self.nb_walls == 1:
            print(f'The maze has walls that are all connected.')
        elif self.nb_walls > 1:
            print(f'The maze has {self.nb_walls} sets of walls that are all connected.')

        if self.nb_inaccessible_inner_points == 0:
            print(f'The maze has no inaccessible inner point.')
        elif self.nb_inaccessible_inner_points == 1:
            print(f'The maze has a unique inaccessible inner point.')
        elif self.nb_inaccessible_inner_points > 1:
            print(f'The maze has {self.nb_inaccessible_inner_points} inaccessible inner points.')

        if self.nb_accessible_areas == 0:
            print(f'The maze has no accessible area.')
        elif self.nb_accessible_areas == 1:
            print(f'The maze has a unique accessible area.')
        elif self.nb_accessible_areas > 1:
            print(f'The maze has {self.nb_accessible_areas} accessible areas.')

        if self.nb_accessible_cul_de_sacs == 0:
            print(f'The maze has no accessible cul-de-sac.')
        elif self.nb_accessible_cul_de_sacs == 1:
            print(f'The maze has accessible cul-de-sacs that are all connected.')
        elif self.nb_accessible_cul_de_sacs > 1:
            print(
                f'The maze has {self.nb_accessible_cul_de_sacs} sets of accessible cul-de-sacs that are all connected.')

        if self.nb_entry_exit_path == 0:
            print(f'The maze has no entry-exit path with no intersection not to cul-de-sacs.')
        elif self.nb_entry_exit_path == 1:
            print(f'The maze has a unique entry-exit path with no intersection not to cul-de-sacs.')
        elif self.nb_entry_exit_path > 1:
            print(f'The maze has {self.nb_entry_exit_path} entry-exit paths with no intersections not to cul-de-sacs.')

    # 分析迷宫图
    def analyse(self):
        # code 九宫格字典
        code_dic_1 = {'0': ((1, 0, 1),
                            (0, 0, 0),
                            (1, 0, 1)),

                      '1': ((1, 1, 1),
                            (0, 0, 0),
                            (1, 0, 1)),

                      '2': ((1, 0, 1),
                            (1, 0, 0),
                            (1, 0, 1)),

                      '3': ((1, 1, 1),
                            (1, 0, 0),
                            (1, 0, 1))}

        code_dic_2 = {'0': ((0, 0, 0),
                            (0, 0, 0),
                            (0, 0, 0)),

                      '1': ((1, 1, 1),
                            (0, 0, 0),
                            (0, 0, 0)),

                      '2': ((1, 0, 0),
                            (1, 0, 0),
                            (1, 0, 0)),

                      '3': ((1, 1, 1),
                            (1, 0, 0),
                            (1, 0, 0))}

        # 输出
        # gates
        self.get_gates(code_dic_1)

        # walls
        self.nb_walls = self.get_walls(code_dic_2)

        # pillars
        self.get_pillars()

        # accessible areas and inaccessible inner points
        self.get_accessible_areas_and_inaccessible_inner_point(code_dic_1)

        # accessible cul-de-sacs and entry-exit path
        self.get_accessible_cul_de_sacs_and_entry_exit_paths(code_dic_1)

        # display
        self.attribute_display()

    # 生成迷宫图
    def display(self):
        # code 九宫格字典
        code_dic_1 = {'0': ((1, 0, 1),
                            (0, 0, 0),
                            (1, 0, 1)),

                      '1': ((1, 1, 1),
                            (0, 0, 0),
                            (1, 0, 1)),

                      '2': ((1, 0, 1),
                            (1, 0, 0),
                            (1, 0, 1)),

                      '3': ((1, 1, 1),
                            (1, 0, 0),
                            (1, 0, 1))}

        code_dic_2 = {'0': ((0, 0, 0),
                            (0, 0, 0),
                            (0, 0, 0)),

                      '1': ((1, 1, 1),
                            (0, 0, 0),
                            (0, 0, 0)),

                      '2': ((1, 0, 0),
                            (1, 0, 0),
                            (1, 0, 0)),

                      '3': ((1, 1, 1),
                            (1, 0, 0),
                            (1, 0, 0))}

        # 输出
        # gates
        self.get_gates(code_dic_1)

        # walls
        self.nb_walls = self.get_walls(code_dic_2)

        # pillars
        self.get_pillars()

        # accessible areas and inaccessible inner points
        self.get_accessible_areas_and_inaccessible_inner_point(code_dic_1)

        # accessible cul-de-sacs and entry-exit path
        self.get_accessible_cul_de_sacs_and_entry_exit_paths(code_dic_1)

        walls = self.walls
        pillars = self.pillars
        accessible_cul_de_sacs = self.accessible_cul_de_sacs
        entry_eixt_path = self.entry_eixt_path

        file_name = self.file_name.split('.')[0] + '.tex'
        if os.path.exists(file_name):
            os.remove(file_name)
        with open(file_name, 'w') as derived_file:
            derived_file.write('\\documentclass[10pt]{article}\n')
            derived_file.write('\\usepackage{tikz}\n')
            derived_file.write('\\usetikzlibrary{shapes.misc}\n')
            derived_file.write('\\usepackage[margin=0cm]{geometry}\n')
            derived_file.write('\\pagestyle{empty}\n')
            derived_file.write('\\tikzstyle{every node}=[cross out, draw, red]\n')
            derived_file.write('\n')
            derived_file.write('\\begin{document}\n')
            derived_file.write('\n')
            derived_file.write('\\vspace*{\\fill}\n')
            derived_file.write('\\begin{center}\n')
            derived_file.write('\\begin{tikzpicture}[x=0.5cm, y=-0.5cm, ultra thick, blue]\n')

            # draw walls
            derived_file.write('% Walls\n')
            for wall in walls:
                derived_file.write(f'    \\draw ({wall[0][0]},{wall[0][1]}) -- ({wall[1][0]},{wall[1][1]});\n')

            # draw pillars
            derived_file.write('% Pillars\n')
            for pillar in pillars:
                derived_file.write(f'    \\fill[green] ({pillar[0]},{pillar[1]}) circle(0.2);\n')

            # accessible cul-de-sacs
            derived_file.write('% Inner points in accessible cul-de-sacs\n')
            for dead in accessible_cul_de_sacs:
                derived_file.write(f'    \\node at ({dead[0]},{dead[1]}) ' + '{}' + ';\n')

            # Entry-exit paths
            derived_file.write('% Entry-exit paths without intersections\n')
            for entry in entry_eixt_path:
                derived_file.write(
                    f'    \\draw[dashed, yellow] ({entry[0][0]},{entry[0][1]}) -- ({entry[1][0]},{entry[1][1]});\n')

            derived_file.write('\\end{tikzpicture}\n')
            derived_file.write('\\end{center}\n')
            derived_file.write('\\vspace*{\\fill}\n')
            derived_file.write('\n')
            derived_file.write('\\end{document}\n')

        # print('here is walls:')
        # for wall in walls:
        #     print(wall)
        #
        # print('here is pillars:')
        # for pillar in pillars:
        #     print(pillar)
        #
        # print('here is dead culs:')
        # for dead in accessible_cul_de_sacs:
        #     print(dead)
        #
        # print('here is entry-path:')
        # for entry in entry_eixt_path:
        #     print(entry)

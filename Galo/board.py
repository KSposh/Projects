class board:
    def __init__(self, size, player_1, player_2):
        self.size = size
        self.board = self.init_board_structure(size)
        print(self.board)
        self.player_1 = player_1
        self.player_2 = player_2

    def check_win_condition(self):
        pass

    def init_board(self, size):
        board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append('')
            board.append(row)
        return board

    def init_board_structure(self, size):
        board = []
        for i in range(2 * size - 1):
            row = []
            if i % 2 == 1:
                for j in range(2 * size - 1):
                    if j % 2 == 1:
                        row.append('|')
                    else:
                        row.append('')
                board.append(row)
            else:
                board.append('-')
        return board

    def current_state(self):
        for row in self.board:
            for column in row:
                print(column)
            print("\n")

board(3, 'b1', 'b2')

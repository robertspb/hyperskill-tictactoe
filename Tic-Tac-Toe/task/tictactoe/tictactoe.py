class TicTacToe:

    board = [[' ' for _ in range(3)] for _ in range(3)]
    states = ['X', 'O']
    state = 'X'

    def start(self):
        while True:
            move = input('Enter the coordinates:').split()
            if move[0].isalpha() or move[1].isalpha():
                print('You should enter numbers!')
            elif move[0] not in '123' or move[1] not in '123':
                print('Coordinates should be from 1 to 3!')
            else:
                move = list(map(int, move))
                r, c = move[0] - 1, move[1] - 1
                if self.board[r][c] == ' ':
                    self.board[r][c] = self.state
                    self.state = self.states[1] if self.state == self.states[0] else self.states[0]
                    break
                else:
                    print('This cell is occupied! Choose another one!')

        self.print_board()
        self.status_check()

    def status_check(self):
        s = ''.join([''.join([j for j in i]) for i in self.board])
        lines = [s[:3], s[3:6], s[6:], s[:7:3], s[1:8:3], s[2::3], s[::4], s[2:7:2]]
        X = s.count('X')
        O = s.count('O')
        if abs(X - O) > 1 or ('XXX' in lines and 'OOO' in lines):
            print('Impossible')
        elif 'XXX' in lines:
            print('X wins')
        elif 'OOO' in lines:
            print('O wins')
        elif X + O < 9:
            self.start()
        elif X + O == 9:
            print('Draw')

    def print_board(self):
        print(f'''
        ---------
        | {self.board[0][2]} {self.board[1][2]} {self.board[2][2]} |
        | {self.board[0][1]} {self.board[1][1]} {self.board[2][1]} |
        | {self.board[0][0]} {self.board[1][0]} {self.board[2][0]} |
        ---------
        ''')


game = TicTacToe()
game.print_board()
game.start()

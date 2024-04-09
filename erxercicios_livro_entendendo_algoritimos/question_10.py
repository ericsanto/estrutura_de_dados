class HashSoccerPlayer:
    def __init__(self):
        self.name = ''
        self.player = None
        self.__list_gols = []
        self.total_gols = 0

    def register_player(self, name: str) -> str:
        self.name = name
        return self.name

    def register_quantity_gol(self, quantity_player: int) -> list:
        self.player = quantity_player
        list_gols = []
        for c in range(0, self.player):
            gols = int(input(f'Quantos gols fez na partida {c + 1} ?'))
            list_gols = list_gols + [gols]
        self.__list_gols = list_gols
        return self.__list_gols

    def sum_gols(self) -> int:
        for x in self.__list_gols:
            self.total_gols += x
        return self.total_gols

    def register_name_and_quantity_gols_in_hash(self) -> dict:
        table_hash = {}
        table_hash['name'] = self.name
        table_hash['gols'] = self.__list_gols
        table_hash['total'] = self.total_gols
        return table_hash


player_1 = HashSoccerPlayer()
player_1.register_player('Eric')
print(player_1.name)

player_1.register_quantity_gol(5)
print(player_1.sum_gols())

print(player_1.register_name_and_quantity_gols_in_hash())

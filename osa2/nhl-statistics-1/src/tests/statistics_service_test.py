import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.assists, 53)

    def test_search_missing_player(self):
        player = self.stats.search("Nykänen")
        self.assertEqual(player, None)

    def test_get_team(self):
        list_of_players = self.stats.team("EDM")
        self.assertEqual(len(list_of_players), 3)

    def test_get_top_players(self):
        top3 = self.stats.top(3)
        self.assertEqual(top3[0].name, "Gretzky")
        self.assertEqual(top3[1].name, "Lemieux")
        self.assertEqual(top3[2].name, "Yzerman")


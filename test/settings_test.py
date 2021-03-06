import unittest

from settings import Settings

class SettingsTest(unittest.TestCase):

    def test_number_of_players(self):
        for n in range(5, 11):
            self.assertEqual(Settings(number_of_players=n).number_of_players, n)

    def test_too_few_players_raises_error(self):
        with self.assertRaises(ValueError):
            Settings(number_of_players=4)

    def test_too_many_players_raises_error(self):
        with self.assertRaises(ValueError):
            Settings(number_of_players=11)

    def test_spies_plus_antifa_equal_total(self):
        for n in range(5, 11):
            settings = Settings(number_of_players=n)
            spies = settings.number_of_spies
            antifa = settings.number_of_antifa
            players = settings.number_of_players
            self.assertEqual(spies + antifa, n)
            self.assertEqual(spies + antifa, players)


if __name__ == '__main__':
    unittest.main()

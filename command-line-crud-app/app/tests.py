from django.test import TestCase
from app import models


# This is to see the name of the models
# class Games(models.Model):
#     name = models.TextField()
#     release_year = models.IntegerField()
#     main_genre = models.TextField()
#     publisher = models.TextField()
#     main_character = models.TextField()

# Create your tests here.
class TestGames(TestCase):
    def test_add_game(self):
        game = models.add_game(
            "Half-Life",
            1998,
            "FPS",
            "Valve",
            "Gordon Freeman",
            )
        
        self.assertEqual(game.id, 1)
        self.assertEqual(game.name, "Half-Life")
        self.assertEqual(game.release_year, 1998)
        self.assertEqual(game.main_genre, "FPS")
        self.assertEqual(game.developer, "Valve")
        self.assertEqual(game.main_character, "Gordon Freeman")

    def test_view_all(self):

        Games_Data = [
            {
                "name":"Half Life",
                "release_year":1998,
                "main_genre":"FPS",
                "developer":"Valve",
                "main_character":"Gordon Freeman",
            },
            {
                "name":"Portal 2",
                "release_year":2011,
                "main_genre":"Puzzle",
                "developer":"Valve",
                "main_character":"Chell",
            },
            {
                "name":"Legend of Zelda (Majoras Mask)",
                "release_year":2000,
                "main_genre":"Action-Adventure",
                "developer":"Nintendo",
                "main_character":"Link",
            },
            {
                "name":"Baldurs gate 3",
                "release_year":2023,
                "main_genre":"RPG",
                "developer":"Larian Studios",
                "main_character":"Tav (Custom Character)",
            },
        ]
        for Game_Data in Games_Data:
            models.add_game(
                Game_Data["name"],
                Game_Data["release_year"],
                Game_Data["main_genre"],
                Game_Data["developer"],
                Game_Data["main_character"]
            )

        games = models.view_All()

        self.assertEqual(len(games),len(Games_Data))

        Games_Data = sorted(Games_Data, key=lambda c: c["name"])
        games = sorted(games, key=lambda c: c.name)

        for data, game in zip(Games_Data,games):
            self.assertEqual(data["name"], game.name)
            self.assertEqual(data["release_year"], game.release_year)
            self.assertEqual(data["main_genre"], game.main_genre)
            self.assertEqual(data["developer"], game.developer)
            self.assertEqual(data["main_character"], game.main_character)

    def test_can_search_by_name(self):
        Games_Data = [
            {
                "name":"Half Life",
                "release_year":1998,
                "main_genre":"FPS",
                "developer":"Valve",
                "main_character":"Gordon Freeman",
            },
            {
                "name":"Portal 2",
                "release_year":2011,
                "main_genre":"Puzzle",
                "developer":"Valve",
                "main_character":"Chell",
            },
            {
                "name":"Legend of Zelda (Majoras Mask)",
                "release_year":2000,
                "main_genre":"Action-Adventure",
                "developer":"Nintendo",
                "main_character":"Link",
            },
            {
                "name":"Baldurs gate 3",
                "release_year":2023,
                "main_genre":"RPG",
                "developer":"Larian Studios",
                "main_character":"Tav (Custom Character)",
            },
        ]
        for Game_Data in Games_Data:
            models.add_game(
                Game_Data["name"],
                Game_Data["release_year"],
                Game_Data["main_genre"],
                Game_Data["developer"],
                Game_Data["main_character"]
            )

        self.assertIsNone(models.view_by_game_name("sssss"))

        game = models.view_by_game_name("Half Life")

        self.assertIsNotNone(game)
        self.assertEqual(game.developer, "Valve")
        
    def test_view_by_dev(self):
        Games_Data = [
            {
                "name":"Half Life",
                "release_year":1998,
                "main_genre":"FPS",
                "developer":"Valve",
                "main_character":"Gordon Freeman",
            },
            {
                "name":"Portal 2",
                "release_year":2011,
                "main_genre":"Puzzle",
                "developer":"Valve",
                "main_character":"Chell",
            },
            {
                "name":"Legend of Zelda (Majoras Mask)",
                "release_year":2000,
                "main_genre":"Action-Adventure",
                "developer":"Nintendo",
                "main_character":"Link",
            },
            {
                "name":"Baldurs gate 3",
                "release_year":2023,
                "main_genre":"RPG",
                "developer":"Larian Studios",
                "main_character":"Tav (Custom Character)",
            },
        ]
        for Game_Data in Games_Data:
            models.add_game(
                Game_Data["name"],
                Game_Data["release_year"],
                Game_Data["main_genre"],
                Game_Data["developer"],
                Game_Data["main_character"]
            )
        self.assertEqual(len(models.view_by_publisher("Valve")), 2)

    def test_update_publisher(self):

        Games_Data = [
            {
                "name":"Half Life",
                "release_year":1998,
                "main_genre":"FPS",
                "developer":"Valve",
                "main_character":"Gordon Freeman",
            },
            {
                "name":"Portal 2",
                "release_year":2011,
                "main_genre":"Puzzle",
                "developer":"Valve",
                "main_character":"Chell",
            },
            {
                "name":"Legend of Zelda (Majoras Mask)",
                "release_year":2000,
                "main_genre":"Action-Adventure",
                "developer":"EA",
                "main_character":"Link",
            },
            {
                "name":"Baldurs gate 3",
                "release_year":2023,
                "main_genre":"RPG",
                "developer":"Larian Studios",
                "main_character":"Tav (Custom Character)",
            },
        ]
        for Game_Data in Games_Data:
            models.add_game(
                Game_Data["name"],
                Game_Data["release_year"],
                Game_Data["main_genre"],
                Game_Data["developer"],
                Game_Data["main_character"]
            )
        models.update_publisher("Legend of Zelda (Majoras Mask)", "Nintendo")

        self.assertEqual(
            models.view_by_game_name("Legend of Zelda (Majoras Mask)").developer, "Nintendo"
        )

    def test_delete_game(self):
        Games_Data = [
            {
                "name":"Half Life",
                "release_year":1998,
                "main_genre":"FPS",
                "developer":"Valve",
                "main_character":"Gordon Freeman",
            },
            {
                "name":"Portal 2",
                "release_year":2011,
                "main_genre":"Puzzle",
                "developer":"Valve",
                "main_character":"Chell",
            },
            {
                "name":"Legend of Zelda (Majoras Mask)",
                "release_year":2000,
                "main_genre":"Action-Adventure",
                "developer":"EA",
                "main_character":"Link",
            },
            {
                "name":"Baldurs gate 3",
                "release_year":2023,
                "main_genre":"RPG",
                "developer":"Larian Studios",
                "main_character":"Tav (Custom Character)",
            },
        ]
        for Game_Data in Games_Data:
            models.add_game(
                Game_Data["name"],
                Game_Data["release_year"],
                Game_Data["main_genre"],
                Game_Data["developer"],
                Game_Data["main_character"]
            )

        models.delete_game("Portal 2")

        self.assertEqual(len(models.view_All()), 3)

        
import unittest
from Six_Degrees_of_Bacon import difficulty_setup, player_name_validation, cast_list_parser


class MyTestCase(unittest.TestCase):
    def test_difficulty_setup(self):
        self.diff_setting = "medium"  # Input prompt entry
        expected = 5
        actual = difficulty_setup()
        self.assertEqual(expected, actual)

    def test_difficulty_setup2(self):
        self.diff_setting = 7  # Invalid input prompt entry
        with self.assertRaises(SystemExit):
            difficulty_setup()

    def test_player_name_validation(self):
        with self.assertRaises(SystemExit):  # Names containing a/all number(s) will produce a System Exit
            player_name_validation("123")

    def test_player_name_validation2(self):
        player_name = "Steven"  # Valid input
        expected = "Alright Steven! Let's see if you got what it takes!"
        actual = player_name_validation(player_name)
        self.assertEqual(expected, actual)

    def test_cast_list_parser(self):
        url = "https://www.imdb.com/title/tt0303933/"  # Valid URL
        expected = ['Nick Cannon', 'Zoe Saldana', 'Orlando Jones', 'Leonard Roberts', 'GQ', 'Jason Weaver',
                    'Earl Poitier', 'Candace Carey', 'Shay Roundtree', 'Miguel A. Gaetan', 'J. Anthony Brown',
                    'Afemo Omilami', 'Angela Elayne Gibbs', 'Tyreese Burnett', 'Brandon Hirsch', 'Omar J. Dorsey',
                    'Al Wiggins', 'Nicholas B. Thomas', 'Petey Pablo', 'Stuart Scott', 'Courtney James Stewart',
                    'Von Coulter', 'Jason Sims-Prewitt', 'George A. Peters II', 'Gary Yates', 'Rob Cleveland',
                    'Enoch King', 'A.J.', 'Free', 'Reggie Gay', 'Ryan Cameron', 'Blu Cantrell', 'Erin Brantley',
                    'Kiara Nicole Ely', 'Stacey A. Fann', 'Christy Gamble', 'Brianne Landry', 'Pauline S. Lewis',
                    'Glenda Morton', 'Shamea Morton', 'Jenear Wimbley', 'Tracie Wright', 'Kalev Carrow', 'Emmy Collins',
                    'Aimee Davis', 'Jayson Frederick', 'Kristol Grant Blanks', 'GlenNeta Griffin', 'Gerrit Hamilton',
                    'Gavin Kelly', 'Ryan Kilgore', 'Heather S. Michaels', 'William Palmer Jr.', 'Arvell Poe',
                    'Jamil Purnell', 'Alexis Rousseau', 'Steve Warren']
        actual = cast_list_parser(url)
        self.assertEqual(expected, actual)

    def test_cast_list_parser2(self):
        url = "https://www.imdb.com/title/"  # Invalid URL
        expected = []
        actual = cast_list_parser(url)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

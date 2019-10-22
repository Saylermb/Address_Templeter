from address_templeter import parse, clean
import unittest


class CleanFuncTest(unittest.TestCase):

    @staticmethod
    def test_clean_1():
        parse("")

    @staticmethod
    def test_parse_2():
        parse("1,2,3,4,5,6,7")

    def test_address_1(self):
        self.assertEqual(clean("город Калиниград, Садово Красная ул., 8а",
                               house=True, index=True, address_pretext=True),
                         'Калиниград Садово Красная улица 8а'
                         )

    def test_address_2(self):
        self.assertEqual(clean("город Калиниград Садово-Красная ул. 184 - Б", house=True, index=True),
                         'Калиниград Садово-Красная 184-Б',
                         )

    def test_without_other(self):
        self.assertEqual(
            clean('м. Київ, вул. В. Гетьмана, 10/37 (на розі вул. В. Гетьмана та вул. Виборзької - на другому поверсі',
                  house=True, index=True),
            'Київ В Гетьмана 10/37'
        )

    def test_clean_without_name(self):
        self.assertEqual(clean('Ясниноватский р-н, Донецкая область,'
                               ' улица Садовая, 26а, магазин Ашан', house=True, index=True, ),
                         'Ясниноватский Донецкая Садовая 26а'
                         )

    def test_clean_index(self):
        self.assertEqual(clean("г. Авдеевка, Ясиноватского района, Донецкой обл, Садовая 26-а 10234",
                               house=True, index=True),
                         '10234 Авдеевка Ясиноватского Донецкой Садовая 26-а'
                         )

    def test_big_name(self):
        self.assertEqual(clean("Ивано - Франковская область, село Малиново, улица 50-лет ссср, 26 Б",
                               house=True, index=True),
                         'Ивано-Франковская Малиново 50-лет ссср 26Б'
                         )

    def test_without_less_digit(self):
        self.assertEqual(clean("г-д Донецк, ул Садовая, 26а, сдесь могда быть ваша реклама 0 1 0 11",
                               house=True, index=True),
                         'Донецк Садовая 26а'
                         )

    def test_less_text(self):
        self.assertEqual(clean("Ясниноватский район, возле белого магазина, улица Садовая, 26а", house=True),
                         'Ясниноватский Садовая 26а'
                         )

    def test_within_space(self):
        self.assertEqual(clean("Ювилейная ул. 21 / 22", house=True, index=True),
                         'Ювилейная 21/22'
                         )

    def test_within_many_space(self):
        self.assertEqual(clean("г Киев,    Киевская обл.                     Н. Амосова               12 Б",
                               house=True, index=True, region_pretext=True),
                         'Киев Киевская область Н Амосова 12Б'
                         )

    def test_without_title_and_punctuation(self):
        self.assertEqual(clean("г донецк куйбышева 26 а", house=True, index=True),
                         'донецк куйбышева 26а'
                         )

    def test_without_space(self):
        self.assertLessEqual(clean("г.Киев", place_pretext=True),
                             'г Киев'
                             )


class ParseFuncTest(unittest.TestCase):

    def test_parse_1(self):
        self.assertListEqual(parse("город Калиниград, 50-лет ссср ул. 8а"),
                         [('город', 'PlacePretext'),
                          ('Калиниград', 'Place'),
                          (',', 'Comma'),
                          ('50-лет', 'Street'),
                          ('ссср', 'Street'),
                          ('ул', 'StreetPretext'),
                          ('8а', 'HouseNumber')]
                         )

    def test_parse_2(self):
        self.assertListEqual(parse("г. Судак Солнечная 9 а"),
                         [('г', 'PlacePretext'),
                          ('Судак', 'Place'),
                          ('Солнечная', 'Street'),
                          ('9', 'HouseNumber'),
                          ('а', 'HouseNumber')]
                         )
    @staticmethod
    def test_parse_3():
        parse("1,2,3,4,5,6,7")

    def test_without_address(self):
        parsed = [word for word in parse("Ясень, ясень, как так ясень?!") if word[1] not in ['OtherText', 'Comma']]
        self.assertLessEqual(len(parsed), 1)


if __name__ == '__main__':
    unittest.main()
    # s = clean("город Калиниград Садово-Красная ул. 184 - Б", house=True, index=True)
    # print(s)
    # assert s == 'Калиниград Садово-Красная 184-Б'
    # s = parse("г. Судак Солнечная 9 а")
    # print(s)
    #
    # print(time() - t1)

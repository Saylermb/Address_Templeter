from address_templeter import parse, clean
from time import time


if __name__ == '__main__':

    t1 =time()
    s = clean('м. Київ, вул. В. Гетьмана, 10/37 (на розі вул. В. Гетьмана та вул. Виборзької - на другому поверсі', house=True, index=True)
    print(s)
    assert s == 'Київ В Гетьмана 10/37'
    s = clean("Ясниноватский р-н, Донецкая область, улица Садовая, 26а, магазин Ашан", house=True, index=True, )
    print(parse("Ясниноватский р-н, Донецкая область, улица Садовая, 26а, магазин Ашан"))
    print(s)
    assert s == 'Ясниноватский Донецкая Садовая 26а'
    s = clean("г. Авдеевка, Ясиноватского района, Донецкой обл, Садовая 26-а 10234", house=True, index=True)  # индекс
    print(s)
    assert s == '10234 Авдеевка Ясиноватского Донецкой Садовая 26-а'
    s = clean(
        "Ивано - Франковская область, село Малиново, улица 50-лет ссср, 26 Б", house=True, index=True)  # наименования с большим количеством слов
    print(s)
    assert s == 'Ивано-Франковская Малиново 50-лет ссср 26Б'
    s = clean("г-д Донецк, ул Садовая, 26а, сдесь могда быть ваша реклама 0 1 0 11", house=True, index=True)  # лишние цифры
    print(s)
    assert s == 'Донецк Садовая 26а'
    s = clean("Ясниноватский район, возле белого магазина, улица Садовая, 26а", house=True)  # лишний текст
    print(s)
    assert s == 'Ясниноватский Садовая 26а'
    s = clean("Ювилейная ул. 21 / 22", house=True, index=True)  # разделённый адрес пробелами
    print(s)
    assert s == 'Ювилейная 21/22'
    s = clean("г донецк куйбышева 26 а", house=True, index=True)  # отсутствие знаков припенания и заглавных букв
    print(s)
    assert s == 'донецк куйбышева 26а'
    s = parse("Ясень, ясень, как так ясень?!")  # просто хрень)
    print(s)
    s = clean("г.Киев", place_pretext=True)  # отсутствие пробелов
    print(s)
    assert s == 'г Киев'
    s = clean("город Калиниград, Садово Красная ул., 8а", house=True, index=True, address_pretext=True)
    print(s)
    assert s == 'Калиниград Садово Красная улица 8а'
    s = clean("г Киев,    Киевская обл.                     Н. Амосова               12 Б", house=True, index=True, region_pretext=True)
    print(s)
    assert s == 'Киев Киевская область Н Амосова 12Б'
    s = parse("город Калиниград, 50-лет ссср ул. 8а")
    print(s)
    s = clean("город Калиниград Садово-Красная ул. 184 - Б", house=True, index=True)
    print(s)
    assert s == 'Калиниград Садово-Красная 184-Б'
    s = parse("г. Судак Солнечная 9 а")
    print(s)
    print(time() - t1)



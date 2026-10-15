# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


def test_sifre_gucu():
    assert sifre_gucu("abc") == "zayıf"
    assert sifre_gucu("1234567") == "zayıf"
    assert sifre_gucu("12345678") == "orta"
    assert sifre_gucu("abcdefghijk") == "orta"
    assert sifre_gucu("123456789012") == "güçlü"


def test_sifre_bos():
    try:
        sifre_gucu("")
        assert False
    except ValueError:
        assert True


def test_otopark_ucreti():
    assert otopark_ucreti(0) == 0
    assert otopark_ucreti(15) == 0
    assert otopark_ucreti(16) == 20
    assert otopark_ucreti(60) == 20
    assert otopark_ucreti(61) == 40
    assert otopark_ucreti(180) == 40
    assert otopark_ucreti(181) == 60


def test_otopark_negatif():
    try:
        otopark_ucreti(-1)
        assert False
    except ValueError:
        assert True


def test_yuzde_degisim():
    assert yuzde_degisim(200, 250) == 25.0
    assert yuzde_degisim(200, 150) == -25.0
    assert yuzde_degisim(100, 100) == 0.0
    assert yuzde_degisim(50, 100) == 100.0


def test_eski_deger_sifir():
    try:
        yuzde_degisim(0, 100)
        assert False
    except ValueError:
        assert True

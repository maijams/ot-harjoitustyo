import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        # Saldo on senteissä
        self.kassapaate = Kassapaate(100000, 0, 0)
    
    def test_kassan_alustus_saldo_toimii(self):
        self.assertEqual(str(self.kassapaate), "Kassa: 1000.0€. Myynti: edulliset 0kpl, maukkaat 0kpl")
    
    # Käteisostot edullisesti:
    def test_kateisosto_edullisesti_maksu_riittaa_kassa_ja_lounasmaara_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(str(self.kassapaate), "Kassa: 1002.4€. Myynti: edulliset 1kpl, maukkaat 0kpl")

    def test_kateisosto_edullisesti_maksu_riittaa_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(vaihtoraha, 760)

    def test_kateisosto_edullisesti_maksu_ei_riita_kassa_ja_lounasmaara_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(str(self.kassapaate), "Kassa: 1000.0€. Myynti: edulliset 0kpl, maukkaat 0kpl")

    def test_kateisosto_edullisesti_maksu_ei_riita_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
    
    # Käteisostot maukkaasti:
    def test_kateisosto_maukkaasti_maksu_riittaa_kassa_ja_lounasmaara_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(str(self.kassapaate), "Kassa: 1004.0€. Myynti: edulliset 0kpl, maukkaat 1kpl")

    def test_kateisosto_maukkaasti_maksu_riittaa_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(vaihtoraha, 600)

    def test_kateisosto_maukkaasti_maksu_ei_riita_kassa_ja_lounasmaara_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(str(self.kassapaate), "Kassa: 1000.0€. Myynti: edulliset 0kpl, maukkaat 0kpl")

    def test_kateisosto_maukkaasti_maksu_ei_riita_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
        
    # Korttiostot edullisesti:
    def test_korttiosto_edullisesti_maksu_riittaa_kassa_ja_lounasmaara_oikein(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate), "Kassa: 1000.0€. Myynti: edulliset 1kpl, maukkaat 0kpl")

    def test_korttiosto_edullisesti_maksu_riittaa_veloitus_oikein(self):
        kortti = Maksukortti(1000)
        veloitus = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(veloitus, True)

    def test_korttiosto_edullisesti_maksu_ei_riita_kassa_ja_lounasmaara_oikein(self):
        kortti = Maksukortti(100)        
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate), "Kassa: 1000.0€. Myynti: edulliset 0kpl, maukkaat 0kpl")

    def test_korttiosto_edullisesti_maksu_ei_riita_veloitus_oikein(self):
        kortti = Maksukortti(100)       
        veloitus = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(veloitus, False)
        
    # Korttiostot maukkaasti:
    def test_korttiosto_maukkaasti_maksu_riittaa_kassa_ja_lounasmaara_oikein(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate), "Kassa: 1000.0€. Myynti: edulliset 0kpl, maukkaat 1kpl")

    def test_korttiosto_maukkaasti_maksu_riittaa_veloitus_oikein(self):
        kortti = Maksukortti(1000) 
        veloitus = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(veloitus, True)

    def test_korttiosto_maukkaasti_maksu_ei_riita_kassa_ja_lounasmaara_oikein(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(self.kassapaate), "Kassa: 1000.0€. Myynti: edulliset 0kpl, maukkaat 0kpl")

    def test_korttiosto_maukkaasti_maksu_ei_riita_veloitus_oikein(self):
        kortti = Maksukortti(100)
        veloitus = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(veloitus, False)
        
    # Rahan lataus kortille:
    def test_lataa_rahaa_kortin_saldo_muuttuu_kun_summa_positiivinen(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 2000)
        self.assertEqual(kortti.saldo, 2100)
        
    def test_lataa_rahaa_kassan_saldo_kasvaa_kun_summa_positiivinen(self):
        kortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti, 2000)
        self.assertEqual(str(self.kassapaate), "Kassa: 1020.0€. Myynti: edulliset 0kpl, maukkaat 0kpl")
        
    def test_lataa_rahaa_ei_tee_mitaan_jos_summa_negatiivinen(self):
        kortti = Maksukortti(100)
        lataus = self.kassapaate.lataa_rahaa_kortille(kortti, -2000)
        self.assertEqual(lataus, None)
    
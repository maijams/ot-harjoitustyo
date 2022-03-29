class Kassapaate:
    def __init__(self, kassa, edulliset, maukkaat):
        self.kassassa_rahaa = kassa
        self.edulliset = edulliset
        self.maukkaat = maukkaat

    def syo_edullisesti_kateisella(self, maksu):
        if maksu >= 240:
            self.kassassa_rahaa = self.kassassa_rahaa + 240
            self.edulliset += 1
            return maksu - 240
        else:
            return maksu

    def syo_maukkaasti_kateisella(self, maksu):
        if maksu >= 400:
            self.kassassa_rahaa = self.kassassa_rahaa + 400
            self.maukkaat += 1
            return maksu - 400
        else:
            return maksu

    def syo_edullisesti_kortilla(self, kortti):
        if kortti.saldo >= 240:
            kortti.ota_rahaa(240)
            self.edulliset += 1
            return True
        else:
            return False

    def syo_maukkaasti_kortilla(self, kortti):
        if kortti.saldo >= 400:
            kortti.ota_rahaa(400)
            self.maukkaat += 1
            return True
        else:
            return False

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
        else:
            return
        
    def __str__(self):
        saldo_euroissa = round(self.kassassa_rahaa / 100, 2)

        return f"Kassa: {saldo_euroissa}€. Myynti: edulliset {self.edulliset}kpl, maukkaat {self.maukkaat}kpl"


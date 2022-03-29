# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on toimia liikuntapäiväkirjana, eli paikkana jonne käyttäjä voi tallentaa tekemiensä urheilusuoritusten tiedot ja tarkastella niitä myöhemmin uudestaan. Sovellus antaa tilastoja menneistä suorituksista, esim. liikunnan parissa vietetyt tunnit kuluvan viikon aikana tai viimeisen vuoden aikana juostut kilometrit. Käyttäjän on mahdollista asettaa itselleen myös rajattu määrä erilaisia liikuntatavoitteita, esim. tee neljä urheilusuoritusta joka viikko. Sovellusta käytetään rekisteröityneenä käyttäjänä, mahdollistaen näin useamman käyttäjän olemassaolon.

## Käyttäjät

Alussa käytössä on vain yksi käyttäjärooli, _normaali käyttäjä_. Myöhemmässä vaiheessa sovellukseen on mahdollista lisätä myös laajemmilla oikeuksilla varustettu _pääkäyttäjä_, joka voisi mm. poistaa olemassaolevia tilejä.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda käyttäjätunnuksen
  - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 4 merkkiä
  - Salasanalle ei perusversiossa ole muita turvallisuusvaatimuksia kuin pituus (vähintään 6 merkkiä)
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuminen tapahtuu syöttämällä olemassaoleva käyttäjätunnus ja salasana 
  - Kirjautuminen ei onnistu jos käyttäjää ei ole olemassa tai salasana ei täsmää

### Kirjautumisen jälkeen

- Käyttäjä voi lisätä uuden urheilusuorituksen tietoineen: 
  - suorituspäivä
  - laji (valmiista valikoimasta)
  - käytetty aika 
  - mahdolliset kilometrit (lajiriippuvainen)
- Käyttäjä voi poistaa urheilusuorituksen
- Käyttäjä voi tarkastella menneitä suorituksia uusimmasta vanhimpaan annetulla aikavälillä
- Käyttäjä voi tarkastella tilastoja menneistä suorituksista (esim. viimeisen kuukauden liikuntatunnit) 
- Käyttäjä voi lisätä itselleen liikuntatavoitteita ja seurata niiden toteutumista (esim. tee kaksi juoksusuoritusta viikossa)
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

Ajankäytön puitteissa sovellusta on mahdollista laajentaa perusversion jälkeen esimerkiksi seuraavilla ominaisuuksilla:

- Vanhojen suoritusten muokkaaminen
- Käyttäjätunnuksen vaihtaminen
- Salasanan vaihtaminen
- Vanhojen suoritusten tarkastelu muokatussa järjestyksessä, esim. suorituksen keston mukaan
- Vanhojen suoritusten tarkastelu rajaamalla, esim. lajin perusteella
- Harjoitustietojen jakaminen muiden käyttäjien kanssa
- Käyttäjätunnuksen ja siihen liittyvän datan poisto

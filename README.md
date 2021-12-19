# Tietokantasovellus – harjoitustyö

## Keskustelusovellus

[Linkki sovellukseen Herokussa](https://tsoha-fngforum.herokuapp.com/)

### Yleiskuvaus
Sovellusta käyttääkseen luodaan aluksi käyttäjätunnus, jolla voi myöhemminkin kirjautua sovellukseen sisään. Kirjauduttua käyttäjä pääsee etusivulle, jossa ilmoitetaan saapuneista yksityisviestetistä, mikäli niitä on saapunut. Ylävalikosta voi siirtyä haluttuun sovelluksen toimintoon tai osaan. Profiilista näkyy käyttäjän omat käyttäjätiedot Foorumilla on aihealueita, joiden alle voi luoda omia keskusteluketjuja tai lukea ja lisätä viestejä jo lisättyihin keskusteluketjuihin. Omia viestejä voi poistaa. Lisäksi ylläpitäjä voi luoda aihealueita ja poistaa viestejä, keskusteluita ja aihealueita. Yhteystiedoissa näkyy listana käyttäjän yhteystietoihinsa lisäämät käyttäjäprofiilit. Käyttäjäprofiilin voi lisätä yhteystietoihin heidän profiilisivuiltaan, joita voi etsiä hakutoiminnolla tai keskustelufoorumilta, mikäli ovat sinne viestejä lisänneet. Viesteistä näkee käyttäjän henkilökohtaisesti saadut viestit lähettäjäkohtaisesti. Lukemattomat viestit ilmoitetaan erikseen. Etsi-sivulta voidaan etsiä hakusanalla foorumiviestejä, käyttäjäprofiileja ja käyttäjälle itselleen lähetettyjä yksityisviestejä. Lisäksi käyttäjä voi kirjautua sovelluksesta ulos.

Sovellus on tehty osana Helsingin yliopiston Aineopintojen harjoitustyö: tietokantasovellus -kurssia.

### Lopullinen sovellus (19.12.2021)
Lopulliseen sovellukseen sisältyy kaikki alunperin 1. välipalautuksessa suunnitellut ominaisuudet. Lisäksi siinä pystyy lisäämään käyttäjiä yhteystietoihin yksityisviestien lähettämistä varten ja käyttämään hakutoimintoa myös käyttäjäprofiilien ja saapuneiden yksityisviestien etsimiseen. Lisäksi ylläpitäjä voi lisätä muita käyttäjiä ylläpitäjiksi ja jäädyttää muita käyttäjäprofiileja, jolloin nämä käyttäjät eivät voi kirjoittaa keskustelufoorumille, ennen kuin heidän käyttöoikeus palautetaan.

### Arvioijalle
Kurssin arvioijaa varten sovellukseen on luotu ylläpitäjäprofiili, jolla voi testata sovelluksen toimintaa ylläpitäjän roolissa. Tämän ylläpitäjäprofiilin käyttäjänimi on "admin" ja salasana "admin123". Nämä profiilitiedot on annettu tähän nimenomaan kurssin ja sovelluksen arviointia ja arvioijaa varten ja tulen poistamaan profiilin kurssin arvostelun jälkeen.

### Alunperin suunnitellut ominaisuudet
* sovellukseen voi luoda käyttäjätunnuksen ja kirjautua joko käyttäjän tai ylläpitäjän roolissa
* sovelluksessa on eri aiheisia keskustelualueita, joita ylläpitäjä voi luoda
* keskustelualueille voi luoda keskusteluketjuja käyttäjänä ja ylläpitäjänä
* keskustelualueille voi kirjoittaa viestejä ja poistaa omia viestejä
* ylläpitäjällä on mahdollisuus poistaa viestejä tai keskusteluita
* sovelluksessa on hakutoiminto, jolla voi hakea viestejä keskusteluista
* käyttäjillä on profiili, josta voi nähdä käyttäjätietoja, kuten tilin luontiajan ja viestimäärän
* käyttäjät voivat lähettää keskenään yksityisviestejä
* ulkoasun parantelu (välipalautus 3)

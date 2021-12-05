# Tietokantasovellus – harjoitustyö

## Keskustelusovellus

[Linkki sovellukseen Herokussa](https://tsoha-fngforum.herokuapp.com/)

### Yleiskuvaus
Sovellus sisältää keskustelufoorumin, jota käyttääkseen on luotava käyttäjätunnus. Keskustelufoorumi koostuu eri aihealuein rajatuista viestiketjualueista. Käyttäjä voi luoda alueille omia keskustelulankoja, joihin voi kirjoittaa viestejä ja keskustella aihepiiriin liittyen.

### Sovelluksen tila (5.12.2021)
Tällä hetkellä sovellukseen on luotu karkeimmat perusominaisuudet:
* kirjautumis- ja rekisteröitymistoiminto, jonka alustava validointiominaisuus vaatii käyttäjänimeltä vähintään 2 ja salasanalta vähintään 5 merkkiä.
* kirjauduttua mahdollisuus tarkastella profiilisivua, jossa näkyy käyttäjänimi, viestimäärä, liittymisaika ja admin-status
* kirjauduttua mahdollisuus mennä keskustelualueelle, jonne voi luoda omia aihealueita ja siirtyä aihealueiden omille sivuille (samannimisiä alueita ei voi luoda)
* aihealueiden sivuilla mahdollisuus luoda omia keskustelulankoja
* keskustelulankoihin on mahdollisuus kirjoittaa viestejä, joissa näkyy käyttäjänimi ja viestin kirjoitusaika (UTC 0)
* omat viestit pystyy poistamaan
* mahdollisuus kirjautua ulos

### Suunniteltuja ominaisuuksia

* sovellukseen voi luoda käyttäjätunnuksen ja kirjautua joko käyttäjän tai ylläpitäjän roolissa
* sovelluksessa on eri aiheisia keskustelualueita, joita ylläpitäjä voi luoda
* keskustelualueille voi luoda keskusteluketjuja käyttäjänä ja ylläpitäjänä
* keskustelualueille voi kirjoittaa viestejä ja poistaa omia viestejä
* ylläpitäjällä on mahdollisuus poistaa viestejä tai keskusteluita
* sovelluksessa on hakutoiminto, jolla voi hakea viestejä keskusteluista
* käyttäjillä on profiili, josta voi nähdä käyttäjätietoja, kuten tilin luontiajan ja viestimäärän
* käyttäjät voivat lähettää keskenään yksityisviestejä
* ulkoasun parantelu

# kayttoliittyma

Tavoitteet:
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan päivityksiä.
* Käyttäjä näkee sovellukseen lisätyt päivitykset. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät (mahdollisesti poistetut) päivitykset.
* Käyttäjä pystyy etsimään päivityksiä hakusanalla tai muulla perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä päivityksiä.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät päivitykset.
* Käyttäjä pystyy valitsemaan päivitykselle yhden tai useamman luokittelun (esim. päivityksen tyyppi, käsittelytila (vastaanotettu, käsitellään, käsitelty), ja tärkeysaste).
* Käyttäjä pystyy kommentoimaan ja päivittämään toisten käyttäjien päivityksiä.
* (Jos mahdollista) Kayttöliittymä toimii pohjana joka täyttää kriteerit tehtävänannolle. Tämän jälkeen pohja on avoinna mahdollisille lisäosille ja toiminnoille joihin kaikki käyttäjät voivat myös lisätä päivityksiä ja kommentteja.

Nykyinen tila:
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen, sekä lisäämään itsellensä profiilikuvan.
* Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan päivityksiä.
* Käyttäjä näkee sovellukseen lisätyt päivitykset. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät päivitykset.
* Käyttäjä pystyy etsimään päivityksiä hakusanalla tai muulla perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä päivityksiä.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät päivitykset.
* Käyttäjä pystyy valitsemaan päivitykselle yhden tai useamman luokittelun (esim. päivityksen tyyppi, käsittelytila (vastaanotettu, käsitellään, käsitelty), ja tärkeysaste).
* Käyttäjä pystyy kommentoimaan toisten käyttäjien päivityksiä.

Muita huomioita:
* Sovelluksen toimintaa on testattu suurella tietomäärällä. Indeksit ovat lisätty tietokantaan. Omilla testauksilla etusivun sekä keskustelujen lataukset kestivät ~0.01s, ja käyttäjien profiilien lataukset kestivät noin 0.1-0.2s. Sovelluksen mukana liitetty seed.py -tiedosto jolla voi tätä testata omalla koneella.

Asennusohjeet (Linux):
* kopioi repositorio koneellesi
* suorita ladatussa kansiossa seuraavat:
* `python3 -m venv venv`
* `source venv/bin/activate`
* `pip install flask`
* `flask run`

Asennusohjeet (Windows):
* kopioi repositorio koneellesi
* suorita ladatussa kansiossa seuraavat:
* `python3 -m venv venv`
* `venv/Scripts/Activate.ps1`
* `pip install flask`
* `flask run`

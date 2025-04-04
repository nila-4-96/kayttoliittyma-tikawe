# kayttoliittymä

Tavoitteet:
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan päivityksiä.
* Käyttäjä näkee sovellukseen lisätyt päivitykset. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät (mahdollisesti poistetut) päivitykset.
* Käyttäjä pystyy etsimään päivityksiä hakusanalla tai muulla perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä päivityksiä.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät päivitykset.
* Käyttäjä pystyy valitsemaan päivitykselle yhden tai useamman luokittelun (esim. päivityksen tyyppi, käsittelytila (vastaanotettu, käsitellään, käsitelty), ja tärkeysaste).
* Käyttäjä pystyy kommentoimaan ja päivittämään toisten käyttäjien päivityksiä.
* (Jos mahdollista) Kayttöliittymä toimii pohjana joka täyttää kriteerit tehtävänannolle. Tämän jälkeen pohja on avoinna mahdollisille lisäosille ja toiminnoille joihin kaikki käyttäjät voivat myös lisätä päivityksiä ja kommentteja (esim. kalenteri, ostoslista, yms.).

Nykyinen tila:
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan päivityksiä.
* Käyttäjä näkee sovellukseen lisätyt päivitykset. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät päivitykset, sekä pystyy lisäämään kommentteja niihin.
* Käyttäjä pystyy etsimään päivityksiä hakusanalla. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä päivityksiä.
* Käyttäjä pääsee käsiksi muiden profiileihin, josta näkyy profiililla tehdyt julkaisut, julkaisujen määrän, sekä ensimmäisen ja viimeisimmän julkaisun.
* Käyttäjä pystyy lisäämään itselleen profiilikuvan sekä näkemään muiden profiilikuvia.

Asennusohjeet (Linux):
* Kloonaa repositorio
* Mene repositorioon terminaalissa
* Suorita "python -m venv venv"
* Suorita "source venv/bin/activate"
* Suorita "pip install flask"
* Suorita "flask run"
* Terminaali antaa kopioitavan url-osoitteen jolla pääset sovellukseen

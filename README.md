# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/da5757d555424d7e1408e4855363da04.jpg" title="What Happened To The Heart? - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/bab022a4cc4a16f5bab01c6c95e6be8d.jpg" title="The Gods We Can Touch - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9c019286f3282154a84d5f149e2b938c.jpg" title="A6 - Lights"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ad4fc37ea08fc33ec7e90b240a6c1127.jpg" title="Violin Dreams, Vol. 3 - Violin Sky"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/29a8d2761c2134f79985b33ef5af923a.jpg" title="Quiet Sea - Cello Cloud"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f54f3b6ef26445a5bbb8a72f0f7830bd.png" title="True - Avicii"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c804b2219fb1978fd44013c9bfa5e24.jpg" title="Endless Summer - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ff3a3705f5124d058bdf2d6d657d8dcf.jpg" title="Summer's Ending Soon - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c72c1fc14df87703feac7154aca343e6.jpg" title="Dreams You Don't Forget - NIGHT TRAVELER"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/700416badcde194ec1319d86b4d22b0a.jpg" title="Dopamine - BØRNS"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8c77e9f509c4dd3bca8d3ac6b5344ce5.png" title="Evolve - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/66a212ca52b0b2005837c8b8c549378b.jpg" title="Seulement L'amour - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/22fae11f52714165e3efeca3c14084ea.jpg" title="Origins (Deluxe) - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/dab20b6fd212607827a48bad65bbcb41.jpg" title="Runaways (feat. Bonnie McKee) - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3b34f6f1b339e9857fb276c318cb8b05.jpg" title="All My Demons Greeting Me As A Friend (Deluxe) - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/55ca082aea21d717eb5f3ba9173296f4.jpg" title="Memories - Coastal"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3515b67af73e63bab25618ae90d9afec.jpg" title="The Cure to Loneliness - Jai Wolf"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b37c7cc2f9e724f39649dd077f660341.jpg" title="Sound of the Universe - Star Cassette"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/be445cb440ee11b70ef9f0d12e760d5d.jpg" title="All Of Those Nights - The Lightning Kids"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5526cfe62a8b32bc1cbcde8460e82784.jpg" title="Heroes - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63e9b188c786835f816db3924a4e9308.jpg" title="Winged Dreams - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37fd0fc15ff5e506a1cade4bb9a963dd.png" title="All My Demons Greeting Me as a Friend - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ac269a71e1803ee7fe6bdda4ddb7f4f5.jpg" title="Heimferd - Danheim"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5f17e3e0b2d9da727719cfbec615fcb1.png" title="Stormdans - Danheim"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c0c12ac9f2afc4ac0a8924b9ac1a6c72.jpg" title="Genesis - David A. Molina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/52a7cfefbb075f71860ad604a282d1de.jpg" title="Owen - RØRE"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fe279f351afc31c94f550ea4a7ec69db.png" title="Astral projection (Deluxe Edition) - Aaron Hibell"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/54c180355bd972ed5ddf8879e969b8ce.jpg" title="Conscious - Francis Wells"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/99947e68c0f44af76f1559af8734afd0.jpg" title="Gunship - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/65da997c7d585ccc09d77d156e3b7c7a.png" title="Tilt - Hannah Parrott"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ffc0e1d52f4e4f16cf0349f8caca29e5.png" title="Smoke + Mirrors - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/21c2ff5360bea7b92f0a43bb794ec1f9.jpg" title="Shadows / Light - Kollen"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7e9623e023b650e1963691fb09b5182e.jpg" title="Eternal Embers - Meltt"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/db2739d39f1d32aeeb09d4887b64ec40.jpg" title="Night Traveler, Vol. 1 - NIGHT TRAVELER"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cc2b6ab328381075488b0b67e96a69e3.jpg" title="Purity Ring - Purity Ring"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2c0247a1f7455918667d3ce1fbe51fea.png" title="Fortanach - Sebastian Plano"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7ee20728f8196c50f5d81292824d603d.jpg" title="Electric Dreams - Siamese Youth"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/96cfa8204737ca4e92a5da6f4b7a4a7e.jpg" title="How I Got Home - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/bc5f692abf06456610cfb7fe7c9969d5.jpg" title="Wanderers - The G"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/271fe787620fe27994ff66616d529e1f.jpg" title="Kids - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/38cd7d135051d0759da0199810273027.jpg" title="Monsters - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/debfd82986a73ee82c651cc4a3e914f5.jpg" title="Night Drive - Timecop1983"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/950ca20d9253f8aad15a129884dadc97.jpg" title="Kala - Trevor Hall"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d142003879651ad399cd94cdcf0ca8f1.jpg" title="Digital Memories :: Analog Emotions (Deluxe Edition) - Ace Marino"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/01c483a1301b672919acc6e924c91ff6.jpg" title="What Happened To The Heart? (Deluxe) - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/05164ba8eb074e355815dc6a5d800521.jpg" title="You Can’t Run From Yourself (From "Kaiju No. 8") - Aurora"> </p>

          
## 👩🏽‍💻 What you'll need
* A README.md file.
* Last.fm API key
  * Fill [this form](https://www.last.fm/api/account/create) to instantly get one. Requires a last.fm account.
* Set up a GitHub Secret called ```LASTFM_API_KEY``` with the value given by last.fm.
* Also set up a ```LASTFM_USER``` GitHub Secret with the user you'll get the weekly charts for.
* Add a ```<!-- lastfm -->``` tag in your README.md file, with two blank lines below it. The album covers will be placed here.

## Instructions
To use this release, add a ```lastfm.yml``` workflow file to the ```.github/workflows``` folder in your repository with the following code:
```diff
name: lastfm-weekly-chart

on:
  schedule:
    - cron: '2 0 * * *'
  workflow_dispatch:

jobs:
  lastfm:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: lastfm to markdown
        uses: darynwhite/lastfm-weekly-chart@2.0
        with:
          LASTFM_API_KEY: ${{ secrets.LASTFM_API_KEY }}
          LASTFM_USER: ${{ secrets.LASTFM_USER }}
          # INCLUDE_LINK: true # Optional. Defaults is false. If you want to include the link to the album page, set this to true.
          # IMAGE_COUNT: 6 # Optional. Defaults to 10. Feel free to remove this line if you want. Last.fm API will produce up to 50 albums.
          # IMAGE_SIZE: 'medium' # "small", "medium", "large", "extralarge", "mega", default is medium if not included
      - name: commit changes
        continue-on-error: true
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add -A
          git commit -m "Updated last.fm's weekly chart" -a

      - name: push changes
        continue-on-error: true
        uses: ad-m/github-push-action@v0.6.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}\
          branch: main
```
The cron job is scheduled to run once a day because Last.fm's API updates weekly chart data daily at 00:00, it's useless to make more than 1 request per day because you'll get the same information back every time. You can manually run the workflow in case Last.fm's API was down at the time, going to the Actions tab in your repository.

## 🚧 To do
* Add the ability to decide between top charts: albums, artists, or tracks
* Feel free to open an issue or send a pull request for anything you believe would be useful.

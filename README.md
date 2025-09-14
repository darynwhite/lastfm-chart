# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/99947e68c0f44af76f1559af8734afd0.jpg" title="Gunship - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c9add86eac5aa56f7e36f916e4095380.gif" title="The Last Goodbye Tour Live - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9c019286f3282154a84d5f149e2b938c.jpg" title="A6 - Lights"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3a732f7dd6ddc9f50e84c97875b6192c.jpg" title="A Moment Apart (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5526cfe62a8b32bc1cbcde8460e82784.jpg" title="Heroes - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7ade51bd6cd0175a05549e68a04bea54.jpg" title="The Last Goodbye (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/11f907bafcbdb99b99a175761f9566cd.jpg" title="Nocturnal - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/38cd7d135051d0759da0199810273027.jpg" title="Monsters - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b853fde2d4783803ce144d1c1b4ae87e.jpg" title="Days of Thunder - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2f4a947ad91af4cca347fd5822488a22.jpg" title="Endless Summer (5 Year Anniversary Edition) - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a7403c29da998233a0ce507bf321862b.jpg" title="Somnia - Abbott"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/54c180355bd972ed5ddf8879e969b8ce.jpg" title="Conscious - Francis Wells"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ca8770d5ef7f08ffda7e5daa6d8b308e.jpg" title="Night Visions (Deluxe) - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b37c7cc2f9e724f39649dd077f660341.jpg" title="Sound of the Universe - Star Cassette"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c804b2219fb1978fd44013c9bfa5e24.jpg" title="Endless Summer - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f54f3b6ef26445a5bbb8a72f0f7830bd.png" title="True - Avicii"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/700416badcde194ec1319d86b4d22b0a.jpg" title="Dopamine - BØRNS"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d4fe7a92abab0637aa358edbe54284c7.jpg" title="Appaloosa Bones - Gregory Alan Isakov"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9de1a08a9d1da269d71fcec90b7769b8.jpg" title="A Way Home - Omar Raafat"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7a4535e88a384512c5e8fdda28245485.jpg" title="Music for Mountains - Thomas James White"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b32f0d69a9f0ee06d441a02daff65569.jpg" title="Skye - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d142003879651ad399cd94cdcf0ca8f1.jpg" title="Digital Memories :: Analog Emotions (Deluxe Edition) - Ace Marino"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3161828bdc75f7f630ab308591ebf748.jpg" title="The Silence in Between - Bob Moses"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f43c175cb56876dd49e05a0140fdfe70.jpg" title="Two Vines (Deluxe) - Empire of the Sun"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c93902899b5f5d89a17dacedb752709d.jpg" title="The Land of in Between - Hannah Parrott"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8c77e9f509c4dd3bca8d3ac6b5344ce5.png" title="Evolve - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a271fbaaaa024a1dca49a5b7aeb23166.png" title="Black Bear - Andrew Belle"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4bceb7d8a100400cb77468144ee60347.png" title="Intense - Armin van Buuren"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/376685303a8f2dbf996fffc3bf9ccee9.jpg" title="After Dark (Deluxe Edition) - Essenger"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/657b1b8d097f482fb5f6a63a494af70e.jpg" title="The Weatherman - Gregory Alan Isakov"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/00f4aef783c07afd0bd8e33f84051362.png" title="The Sweet Escape - Gwen Stefani"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cf5dfd0844f086798d1c8a8a69aabe7a.png" title="In Another Life - Kevin Graham"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/895edacacf2d35b4ce223b91948f16c6.jpg" title="Coast - Kollen"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f19fa5c55be9ba54e5593cadc7aa9268.jpg" title="Moderns - EP - Moderns"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ee921b50595b79d570778df4791860d0.jpg" title="Dead Hearts - Nouveau Arcade"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0605ac94ee875e46631c7d33fed07bb7.jpg" title="Ashley - RØRE"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/52a7cfefbb075f71860ad604a282d1de.jpg" title="Owen - RØRE"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d3cf8de714db8ae71fca77a095d2a368.jpg" title="Space and Time (Deluxe Edition) - The Bad Dreamers"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ff3a3705f5124d058bdf2d6d657d8dcf.jpg" title="Summer's Ending Soon - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63e9b188c786835f816db3924a4e9308.jpg" title="Winged Dreams - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f2bdf437849a9aa2d4c2451e3621f1ec.png" title="Tim - Avicii"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e7667409a4e033043d4c85895aae0d49.jpg" title="6’s to 9’s (Remixes) - Big Wild"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5fbcfb7258117e88cb73b45e25c88b01.jpg" title="Parachutes - Coldplay"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c0c12ac9f2afc4ac0a8924b9ac1a6c72.jpg" title="Genesis - David A. Molina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d3e505d83b826f875236cebf3c47bac0.jpg" title="Evening Machines - Gregory Alan Isakov"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9dc7bf5dc2c74a1b9f7a62b37520cfab.jpg" title="This Empty Northern Hemisphere - Gregory Alan Isakov"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1065769c7075a95c857ab4af93b71561.jpg" title="The Vale Of Shadows - Gunship"> </p>

          
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

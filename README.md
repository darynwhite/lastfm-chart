# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/3a732f7dd6ddc9f50e84c97875b6192c.jpg" title="A Moment Apart (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/99947e68c0f44af76f1559af8734afd0.jpg" title="Gunship - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d4ae381d45f9fc9ac7e687e33178a93b.jpg" title="In Return (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c804b2219fb1978fd44013c9bfa5e24.jpg" title="Endless Summer - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9c019286f3282154a84d5f149e2b938c.jpg" title="A6 - Lights"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7ade51bd6cd0175a05549e68a04bea54.jpg" title="The Last Goodbye (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5526cfe62a8b32bc1cbcde8460e82784.jpg" title="Heroes - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8816946dc53e5400bda5c0bb1ee487a.jpg" title="Summer's Gone (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/700416badcde194ec1319d86b4d22b0a.jpg" title="Dopamine - BØRNS"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/889c0c3371311a85f09e786b454af69d.jpg" title="Synthian (Deluxe Edition) - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b37c7cc2f9e724f39649dd077f660341.jpg" title="Sound of the Universe - Star Cassette"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/54c180355bd972ed5ddf8879e969b8ce.jpg" title="Conscious - Francis Wells"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d142003879651ad399cd94cdcf0ca8f1.jpg" title="Digital Memories :: Analog Emotions (Deluxe Edition) - Ace Marino"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c4df325ed3bd69531e1d3b7fa2619348.jpg" title="Clean Eyes (The Midnight Remix) - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d3cf8de714db8ae71fca77a095d2a368.jpg" title="Space and Time (Deluxe Edition) - The Bad Dreamers"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0c4b4d65203882c7b78bb629f38cb3c2.jpg" title="Horror Show (The Instrumentals) - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/271fe787620fe27994ff66616d529e1f.jpg" title="Kids - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/55ca082aea21d717eb5f3ba9173296f4.jpg" title="Memories - Coastal"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/376685303a8f2dbf996fffc3bf9ccee9.jpg" title="After Dark (Deluxe Edition) - Essenger"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d4fe7a92abab0637aa358edbe54284c7.jpg" title="Appaloosa Bones - Gregory Alan Isakov"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a4bc05c59aa286d875d031437df390f.jpg" title="The Beginning - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ee921b50595b79d570778df4791860d0.jpg" title="Dead Hearts - Nouveau Arcade"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ff3a3705f5124d058bdf2d6d657d8dcf.jpg" title="Summer's Ending Soon - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b4972f03656762528c4e9e0b1e27198c.jpg" title="What Remains - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6bab5c0a5693f17d0c9340910a2049cb.jpg" title="The Unspeakable World - Adi Goldstein"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a271fbaaaa024a1dca49a5b7aeb23166.png" title="Black Bear - Andrew Belle"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f54f3b6ef26445a5bbb8a72f0f7830bd.png" title="True - Avicii"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/66a212ca52b0b2005837c8b8c549378b.jpg" title="Seulement L'amour - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f43c175cb56876dd49e05a0140fdfe70.jpg" title="Two Vines (Deluxe) - Empire of the Sun"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/657b1b8d097f482fb5f6a63a494af70e.jpg" title="The Weatherman - Gregory Alan Isakov"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8d20d80f6006b41329f03c449488f856.jpg" title="The Video Game Champion - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b38a015d5838d73e22fd5d96de494bd4.jpg" title="Becoming - Judah Earl"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/895edacacf2d35b4ce223b91948f16c6.jpg" title="Coast - Kollen"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8a029622f04b20b92c9aa11e88c94791.jpg" title="Shapes and Outlines (Remixes) - Scavenger Hunt"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b853fde2d4783803ce144d1c1b4ae87e.jpg" title="Days of Thunder - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/38cd7d135051d0759da0199810273027.jpg" title="Monsters - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7a4535e88a384512c5e8fdda28245485.jpg" title="Music for Mountains - Thomas James White"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b32f0d69a9f0ee06d441a02daff65569.jpg" title="Skye - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63e9b188c786835f816db3924a4e9308.jpg" title="Winged Dreams - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4bceb7d8a100400cb77468144ee60347.png" title="Intense - Armin van Buuren"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3b34f6f1b339e9857fb276c318cb8b05.jpg" title="All My Demons Greeting Me As A Friend (Deluxe) - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3161828bdc75f7f630ab308591ebf748.jpg" title="The Silence in Between - Bob Moses"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0e82f7d31a9733670f92d4a0dd0ef644.jpg" title="Love Minus 80 - Bunny X"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c0c12ac9f2afc4ac0a8924b9ac1a6c72.jpg" title="Genesis - David A. Molina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d614912e82b94e6f3c054c08f0f099fa.jpg" title="Moss - David Celeste"> </p>

          
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

# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/85d3be3438d7b31d7e5f7ec71c39a603.jpg" title="Cracker Island (Deluxe) - Gorillaz"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c718e6a741403ac46d45b7195e52b826.jpg" title="Dance Mode! - Bluey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/211d2fa9cff0ca90a33fbc64df7a205b.jpg" title="Lamomali Totem - -M-"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f9d044b65b5a6db501f76d63403402e6.png" title="Everybody Scream - Florence + the Machine"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/497547fe04cabbf4686ea5cbfb781f11.png" title="Paris Unplugged - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a4b0ca89a071af2b87aa9e24cd7b9294.jpg" title="Viking War Trance - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/282c3bf58a2d2d9b99be592321d8760c.jpg" title="A Frame of Mind - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a2cc80f9f588dbd4cfe7e8a511e78f25.jpg" title="SYML - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/66a212ca52b0b2005837c8b8c549378b.jpg" title="Seulement L'amour - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/af5ee011b7f8ce55a0e49954ef5c1f54.jpg" title="DRYVE (Deluxe) - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/abd9c1b19f80191621f521d2a3689c19.jpg" title="Sacred Spaces - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/99e31f65ce379bce221e24807944cfbc.jpg" title="The Payback - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f7bf3cb16552735edc4e240b2d88650c.jpg" title="Shepherd Moons - Enya"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8c77e9f509c4dd3bca8d3ac6b5344ce5.png" title="Evolve - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3b34f6f1b339e9857fb276c318cb8b05.jpg" title="All My Demons Greeting Me As A Friend (Deluxe) - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e5456f90c6ec3a5508a8729130a1c3b5.jpg" title="Bluey the Album (Music from the Original TV Series) - Bluey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0ad59976ae86471b1aecfcd449f2e25e.jpg" title="80s Kids - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3df392d519ea4eecce0b67083ac15050.jpg" title="Fatou - Fatoumata Diawara"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9c019286f3282154a84d5f149e2b938c.jpg" title="A6 - Lights"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a6ee015fe1bc4d86cdb9b7c76778e7a6.jpg" title="Strange Trails - Lord Huron"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4d6a333808f4a1e7cd69d30ed457248e.jpg" title="A Day Without Rain - Enya"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/675daa7ad71cd7dc682c13cfa2365a97.jpg" title="Watermark (2009 Remaster) - Enya"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a191a2114b6d7ca2691cfdc678b896b.jpg" title="Mørketid - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37fd0fc15ff5e506a1cade4bb9a963dd.png" title="All My Demons Greeting Me as a Friend - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f2b16f1c0c5ed1edf3d7772e79d49098.jpg" title="Starlight Remixes - Jai Wolf"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6c82a3ba98f8660110dcd8989d883d50.jpg" title="The Day My Father Died - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63e9b188c786835f816db3924a4e9308.jpg" title="Winged Dreams - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/700416badcde194ec1319d86b4d22b0a.jpg" title="Dopamine - BØRNS"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fa484d70bb0317be7c8a010868dc61d7.jpg" title="No Perfect Love - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e793951f5d8fc2de696ea880f9bd8437.jpg" title="The Memory of Trees - Enya"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/271483e955d2b255160f3361a7f5fb78.jpg" title="Demon Days - Gorillaz"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7940fbb1df766b4683951aed490a8b5a.jpg" title="Fine Line - Harry Styles"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0553855155afbee981f9e460021522c5.jpg" title="Mercury - Acts 1 & 2 - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ce3293d7fa03c4decb1c43bbc70fd4ec.jpg" title="The Roads - Jonah Kagen"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37495917b4e632c097de92248b3f90ff.jpg" title="A Moment Apart - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/87138bbda83bd0ae8b4da2b6cab9b66a.jpg" title="Everybody Else Is Doing It, So Why Can't We? - The Cranberries"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8b544204fe15dd7f16bfc3476f98914.jpg" title="Desire - The Lightning Kids"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c804b2219fb1978fd44013c9bfa5e24.jpg" title="Endless Summer - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5526cfe62a8b32bc1cbcde8460e82784.jpg" title="Heroes - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/debfd82986a73ee82c651cc4a3e914f5.jpg" title="Night Drive - Timecop1983"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9df88bfe6a60e90533a9ce876c3fccc5.jpg" title="Infinity - W O L F C L U B"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0e82f7d31a9733670f92d4a0dd0ef644.jpg" title="Love Minus 80 - Bunny X"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e6ba2e725c70bd0a559e373852da5333.jpg" title="Heartbeats - Coastal"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d6e7200ad6360100997770fa3f3c08ae.jpg" title="Hugrheim - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4b2cb98b03adf07f3d618a47fd60f775.jpg" title="Skjaldmö - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/34cac131ba9b246d7d683850be9df63a.jpg" title="Völva's Chant - Eihwar"> </p>

          
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

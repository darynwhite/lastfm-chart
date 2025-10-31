# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e5456f90c6ec3a5508a8729130a1c3b5.jpg" title="Bluey the Album (Music from the Original TV Series) - Bluey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c718e6a741403ac46d45b7195e52b826.jpg" title="Dance Mode! - Bluey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a4b0ca89a071af2b87aa9e24cd7b9294.jpg" title="Viking War Trance - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/497547fe04cabbf4686ea5cbfb781f11.png" title="Paris Unplugged - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a2cc80f9f588dbd4cfe7e8a511e78f25.jpg" title="SYML - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/abd9c1b19f80191621f521d2a3689c19.jpg" title="Sacred Spaces - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63e9b188c786835f816db3924a4e9308.jpg" title="Winged Dreams - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4d6a333808f4a1e7cd69d30ed457248e.jpg" title="A Day Without Rain - Enya"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f7bf3cb16552735edc4e240b2d88650c.jpg" title="Shepherd Moons - Enya"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3b34f6f1b339e9857fb276c318cb8b05.jpg" title="All My Demons Greeting Me As A Friend (Deluxe) - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5f57e62ee82c1a4b337d779bd02ef073.jpg" title="Meniscus - David Celeste"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d6e7200ad6360100997770fa3f3c08ae.jpg" title="Hugrheim - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4b2cb98b03adf07f3d618a47fd60f775.jpg" title="Skjaldmö - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f2b16f1c0c5ed1edf3d7772e79d49098.jpg" title="Starlight Remixes - Jai Wolf"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2c0247a1f7455918667d3ce1fbe51fea.png" title="Fortanach - Sebastian Plano"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6c82a3ba98f8660110dcd8989d883d50.jpg" title="The Day My Father Died - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b32f0d69a9f0ee06d441a02daff65569.jpg" title="Skye - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/47d6fc9e62e7ff1551e1b07dcca79e02.jpg" title="Berserkr - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a863bde41cc86fe11d54634b544342a9.jpg" title="Ragnarök - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/34cac131ba9b246d7d683850be9df63a.jpg" title="Völva's Chant - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a6b02765495e036a960baa612cc2875d.jpg" title="Yggdrasil's Renewal - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/675daa7ad71cd7dc682c13cfa2365a97.jpg" title="Watermark (2009 Remaster) - Enya"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/21c2ff5360bea7b92f0a43bb794ec1f9.jpg" title="Shadows / Light - Kollen"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/52a7cfefbb075f71860ad604a282d1de.jpg" title="Owen - RØRE"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b4972f03656762528c4e9e0b1e27198c.jpg" title="What Remains - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1ed117d6268d1a26546c1ddd06227233.jpg" title="Days Again - David Celeste"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/66a212ca52b0b2005837c8b8c549378b.jpg" title="Seulement L'amour - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4d200ea01f148360fb3f1e6d045b4a73.jpg" title="Berserkr (Viking War Trance Reforged) - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cc9f07c6aa8ec63664ef1034502c7129.jpg" title="Fenrir - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e0023f6c9540017f80653003603b5c56.jpg" title="The Feast of Thor - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6909a21dd6f1c7efbb560229914a68eb.jpg" title="The Forge - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4c4db5e992a74740078357e6e44cce59.jpg" title="The New Vikings - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/68cb7bd9a5634902a65bcd1c947464db.png" title="Amarantine - Enya"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a6a9b43f9f53a543d932296da0401038.png" title="Dark Sky Island - Enya"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e793951f5d8fc2de696ea880f9bd8437.jpg" title="The Memory of Trees - Enya"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/99947e68c0f44af76f1559af8734afd0.jpg" title="Gunship - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8c77e9f509c4dd3bca8d3ac6b5344ce5.png" title="Evolve - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/895edacacf2d35b4ce223b91948f16c6.jpg" title="Coast - Kollen"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9c019286f3282154a84d5f149e2b938c.jpg" title="A6 - Lights"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37495917b4e632c097de92248b3f90ff.jpg" title="A Moment Apart - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/96cfa8204737ca4e92a5da6f4b7a4a7e.jpg" title="How I Got Home - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8b544204fe15dd7f16bfc3476f98914.jpg" title="Desire - The Lightning Kids"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2f4a947ad91af4cca347fd5822488a22.jpg" title="Endless Summer (5 Year Anniversary Edition) - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/debfd82986a73ee82c651cc4a3e914f5.jpg" title="Night Drive - Timecop1983"> </p>

          
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

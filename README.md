# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e5456f90c6ec3a5508a8729130a1c3b5.jpg" title="Bluey the Album (Music from the Original TV Series) - Bluey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a4b0ca89a071af2b87aa9e24cd7b9294.jpg" title="Viking War Trance - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63e9b188c786835f816db3924a4e9308.jpg" title="Winged Dreams - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c718e6a741403ac46d45b7195e52b826.jpg" title="Dance Mode! - Bluey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b32f0d69a9f0ee06d441a02daff65569.jpg" title="Skye - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/155aa622a72e545eb62173cf1223e15e.png" title="Birna - Wardruna"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5f57e62ee82c1a4b337d779bd02ef073.jpg" title="Meniscus - David Celeste"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b4972f03656762528c4e9e0b1e27198c.jpg" title="What Remains - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/895edacacf2d35b4ce223b91948f16c6.jpg" title="Coast - Kollen"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/47d6fc9e62e7ff1551e1b07dcca79e02.jpg" title="Berserkr - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d6e7200ad6360100997770fa3f3c08ae.jpg" title="Hugrheim - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5e132aafb8481f6fed27cfe7fe78576c.jpg" title="Ragnar's Last Raid - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a863bde41cc86fe11d54634b544342a9.jpg" title="Ragnarök - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4b2cb98b03adf07f3d618a47fd60f775.jpg" title="Skjaldmö - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e0023f6c9540017f80653003603b5c56.jpg" title="The Feast of Thor - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6909a21dd6f1c7efbb560229914a68eb.jpg" title="The Forge - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/34cac131ba9b246d7d683850be9df63a.jpg" title="Völva's Chant - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a6b02765495e036a960baa612cc2875d.jpg" title="Yggdrasil's Renewal - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/21c2ff5360bea7b92f0a43bb794ec1f9.jpg" title="Shadows / Light - Kollen"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a4bc05c59aa286d875d031437df390f.jpg" title="The Beginning - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/52a7cfefbb075f71860ad604a282d1de.jpg" title="Owen - RØRE"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7a4535e88a384512c5e8fdda28245485.jpg" title="Music for Mountains - Thomas James White"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/edd2112eb9f0d142689937c4638380b8.jpg" title="Madagascar: Escape 2 Africa (Music from the Motion Picture) - Various Artists"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1ed117d6268d1a26546c1ddd06227233.jpg" title="Days Again - David Celeste"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4d200ea01f148360fb3f1e6d045b4a73.jpg" title="Berserkr (Viking War Trance Reforged) - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cc9f07c6aa8ec63664ef1034502c7129.jpg" title="Fenrir - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4c4db5e992a74740078357e6e44cce59.jpg" title="The New Vikings - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c3856e8bc2f4fa3a644ba58d96dcf272.jpg" title="Valhalla - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a09e7d8f3207ba70b080d1184b47db15.jpg" title="Novella - Jordan Critz"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9de1a08a9d1da269d71fcec90b7769b8.jpg" title="A Way Home - Omar Raafat"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2c0247a1f7455918667d3ce1fbe51fea.png" title="Fortanach - Sebastian Plano"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c4d02c195fcd225447e6f959bb9418b6.jpg" title="Weep No More - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1d4dc832bd3c4ed181ea404eed9ffc77.jpg" title="Seeds - David Celeste"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c85198ed7c569c5ff0d6afb765125c7c.jpg" title="Truth Elastic - David Celeste"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/54c180355bd972ed5ddf8879e969b8ce.jpg" title="Conscious - Francis Wells"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c4bd9586a632f9abd9894964ece8aff5.jpg" title="Sierra - Inola"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6bab5c0a5693f17d0c9340910a2049cb.jpg" title="The Unspeakable World - Adi Goldstein"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/488c1cd998e80dec58b42b3330f9bcaf.jpg" title="Of This Blood - Daridel"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/66ec56cc965240b0fda3b73fa7c2e1ed.jpg" title="Senua's Saga: Hellblade II (Original Soundtrack) - David García Díaz"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e3e7c98dd8ec5d57d565f96cbb4229b9.png" title="Tales of Old: Echoes of Heritage - Devel Sullivan"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/70d029eda64eb8d415803a149f29398e.jpg" title="Horizon - Dominik A. Hecker"> </p>

          
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

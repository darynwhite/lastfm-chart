# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/c90f4bd7d8218ab0f67de086e6b1063e.jpg" title="Jasper - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b1980c8760bc014d550434a61e920212.jpg" title="Josephine Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/95716b6e75284516307f57088aa41cf5.jpg" title="Duality - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4e452d7e6079b1575444d874a2538c42.jpg" title="Niagara Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a5c3187cd2e856a58bf5b31ac15092f.png" title="Playa La Manzanilla - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9b4f0aeaacebbed4f77b21d4cd059673.png" title="Still on My Mind (Deluxe Edition) - Dido"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/529645dcda01fd7f3d63fba1c760ff5b.jpg" title="Tofino - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3a732f7dd6ddc9f50e84c97875b6192c.jpg" title="A Moment Apart (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a4b0ca89a071af2b87aa9e24cd7b9294.jpg" title="Viking War Trance - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b1d92e309570dfbf344a79911227bbbb.jpg" title="Ions - Turboslash"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c9add86eac5aa56f7e36f916e4095380.gif" title="The Last Goodbye Tour Live - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d0e9c11f3db6c1497f42a1cac8755c0f.png" title="The Last Summer (Deluxe Edition) - R Plus"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37495917b4e632c097de92248b3f90ff.jpg" title="A Moment Apart - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8816946dc53e5400bda5c0bb1ee487a.jpg" title="Summer's Gone (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b57b4740f3930e93ddcb5e978754228b.jpg" title="Voices of the Forest - Pajama Boy"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/76e740fce240ddbfee0cf13d5fee4c1b.jpg" title="Planetarium - Protocols"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5526cfe62a8b32bc1cbcde8460e82784.jpg" title="Heroes - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/777750d519bc4d9da03a5becc45fba58.jpg" title="Mirth & Mayhem (Chapter II) - Fugee"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9c2b118758e93f33ac1efc93624442ac.jpg" title="Lost Journey Memories - Girl from Nowhere"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f5212d1e36ac4dac817c133be39d9c73.png" title="Lindsey Stirling - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63ae49d15df3c1acd2a89ca2294cc039.jpg" title="Singing Sands - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c72c1fc14df87703feac7154aca343e6.jpg" title="Dreams You Don't Forget - NIGHT TRAVELER"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ed2eadee2980ffb1f1f995a4965d00c9.jpg" title="Songs About People Including Myself (Deluxe Edition) - The Bad Dreamers"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c804b2219fb1978fd44013c9bfa5e24.jpg" title="Endless Summer - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b48cf08f855336dc32c48ba0f7362bd9.jpg" title="Horror Show - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/16e39fd39917aa2f93d8ad09530a07fc.jpg" title="DRIVE - Tiësto"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b4972f03656762528c4e9e0b1e27198c.jpg" title="What Remains - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d142003879651ad399cd94cdcf0ca8f1.jpg" title="Digital Memories :: Analog Emotions (Deluxe Edition) - Ace Marino"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4f1db0a6b971f9d5c02f3405bea09adb.jpg" title="You'll Be Alright, Kid (Chapter 1) - Alex Warren"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fe0771a88192919d93a06eddbbf51447.jpg" title="The Stories We Forgot - Andreas Kübler"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/817d2848d85995369e1dba0f364f2411.png" title="Opus - Eric Prydz"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3495bf3cc42429b1d919dde5eaf15ed4.jpg" title="Forgotten Odes - Eternal Eclipse"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/311e75e628397a442d473cef00ec88f4.jpg" title="Decay of the Mainframe - Ferus Melek"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8634719c5059a5723ce12b44dff60e4c.jpg" title="Maverick (Atlas B-Sides) - FM-84"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8d20d80f6006b41329f03c449488f856.jpg" title="The Video Game Champion - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3410c69b8e221724593c87cc25b972d7.jpg" title="Kingdom Two Crowns: Norse Lands Soundtrack (Extended) - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> </p>

          
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

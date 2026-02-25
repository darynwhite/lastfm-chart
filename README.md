# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/b1980c8760bc014d550434a61e920212.jpg" title="Josephine Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9e37f6c83d397a307b7fcf1460536781.jpg" title="Great Ocean Road - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a5c3187cd2e856a58bf5b31ac15092f.png" title="Playa La Manzanilla - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c90f4bd7d8218ab0f67de086e6b1063e.jpg" title="Jasper - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/95716b6e75284516307f57088aa41cf5.jpg" title="Duality - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/529645dcda01fd7f3d63fba1c760ff5b.jpg" title="Tofino - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4e452d7e6079b1575444d874a2538c42.jpg" title="Niagara Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a4b0ca89a071af2b87aa9e24cd7b9294.jpg" title="Viking War Trance - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b32f0d69a9f0ee06d441a02daff65569.jpg" title="Skye - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63e9b188c786835f816db3924a4e9308.jpg" title="Winged Dreams - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b4972f03656762528c4e9e0b1e27198c.jpg" title="What Remains - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3a732f7dd6ddc9f50e84c97875b6192c.jpg" title="A Moment Apart (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b1d92e309570dfbf344a79911227bbbb.jpg" title="Ions - Turboslash"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/57eef49f35b45d7de1cda68f5fd1b914.jpg" title="Sing 2 (Original Motion Picture Soundtrack) - Various Artists"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7e2e2c4c746bccca426d1770dd81e0a6.jpg" title="Sing (Original Motion Picture Soundtrack / Deluxe) - Various Artists"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/00f4aef783c07afd0bd8e33f84051362.png" title="The Sweet Escape - Gwen Stefani"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/dc5b100d3f4d4cf288f94fc182d7c383.jpg" title="Undux - Kaskade"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/edd2112eb9f0d142689937c4638380b8.jpg" title="Madagascar: Escape 2 Africa (Music from the Motion Picture) - Various Artists"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c4d02c195fcd225447e6f959bb9418b6.jpg" title="Weep No More - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37495917b4e632c097de92248b3f90ff.jpg" title="A Moment Apart - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b57b4740f3930e93ddcb5e978754228b.jpg" title="Voices of the Forest - Pajama Boy"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/76e740fce240ddbfee0cf13d5fee4c1b.jpg" title="Planetarium - Protocols"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5526cfe62a8b32bc1cbcde8460e82784.jpg" title="Heroes - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d6f7b0341cbe4398e951b361cb6f2b2c.jpg" title="Walkerworld - Alan Walker"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1cd59f70b7505dc1c43d7a207d21fe0e.jpg" title="Freyja's Calling - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/dc9b979787316b03698db1b265f349fb.jpg" title="Ancient Paths - Enzalla"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/777750d519bc4d9da03a5becc45fba58.jpg" title="Mirth & Mayhem (Chapter II) - Fugee"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9c2b118758e93f33ac1efc93624442ac.jpg" title="Lost Journey Memories - Girl from Nowhere"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63ae49d15df3c1acd2a89ca2294cc039.jpg" title="Singing Sands - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/786fc4cc2d3280b7749f6994190fb9d1.jpg" title="We Are Stardust - LukHash"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8816946dc53e5400bda5c0bb1ee487a.jpg" title="Summer's Gone (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7fc43684bb10569ac2a57f847b1a86e9.jpg" title="Pinkfong Animal Songs - Pinkfong"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c252c625f0ec6784ed170ed0a5862328.png" title="Paradise Again - Swedish House Mafia"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/16e39fd39917aa2f93d8ad09530a07fc.jpg" title="DRIVE - Tiësto"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fe0771a88192919d93a06eddbbf51447.jpg" title="The Stories We Forgot - Andreas Kübler"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/26bd3e9d20adfe47cb96d2b2d15fe6d7.jpg" title="If I Don't See You Again - BPMoore"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/aa3baf579d62ef1c6f7368c7f33672e1.jpg" title="Komorebi - BPMoore"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c0c12ac9f2afc4ac0a8924b9ac1a6c72.jpg" title="Genesis - David A. Molina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/af5ee011b7f8ce55a0e49954ef5c1f54.jpg" title="DRYVE (Deluxe) - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5e132aafb8481f6fed27cfe7fe78576c.jpg" title="Ragnar's Last Raid - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6909a21dd6f1c7efbb560229914a68eb.jpg" title="The Forge - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2054d34d5bab757abfd0ae6c1a926938.jpg" title="Digital Chaos - Elfl"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/817d2848d85995369e1dba0f364f2411.png" title="Opus - Eric Prydz"> </p>

          
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

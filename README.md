# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63e9b188c786835f816db3924a4e9308.jpg" title="Winged Dreams - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3a732f7dd6ddc9f50e84c97875b6192c.jpg" title="A Moment Apart (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/99947e68c0f44af76f1559af8734afd0.jpg" title="Gunship - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b32f0d69a9f0ee06d441a02daff65569.jpg" title="Skye - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a579cc24c2a6220fa329f481e074d5a0.jpg" title="A6EXTENDED - Lights"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b4972f03656762528c4e9e0b1e27198c.jpg" title="What Remains - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/661ada0e5b6925b9d781dfaf63b96d88.jpg" title="Live at Lafayette - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/eff458477e890e6377fc426007616dbe.jpg" title="Dark All Day (Instrumentals) - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2d163e141a0c8a5bafb515a3fd5a6af5.jpg" title="The Mountain - Gorillaz"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f5270041983b7b838c2093f3042927d2.jpg" title="Echo Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63ae49d15df3c1acd2a89ca2294cc039.jpg" title="Singing Sands - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/85ee26d039d6495895f5e952d4df35d9.jpg" title="Summer's Gone - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0e70b058436e0a97c45207fe4680a9bf.jpg" title="GUNSHIP (Instrumentals) - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c90f4bd7d8218ab0f67de086e6b1063e.jpg" title="Jasper - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a4b0ca89a071af2b87aa9e24cd7b9294.jpg" title="Viking War Trance - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d0b420f56c1f50fd0ad0f460a477371d.jpg" title="Romantique - Jordan Critz"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c4d02c195fcd225447e6f959bb9418b6.jpg" title="Weep No More - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7e2e2c4c746bccca426d1770dd81e0a6.jpg" title="Sing (Original Motion Picture Soundtrack / Deluxe) - Various Artists"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/aa3baf579d62ef1c6f7368c7f33672e1.jpg" title="Komorebi - BPMoore"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b7c6f3dadc54e467d7b596c3652be8f4.jpg" title="Tell Me When the World Stops Ending - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a09e7d8f3207ba70b080d1184b47db15.jpg" title="Novella - Jordan Critz"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a5c3187cd2e856a58bf5b31ac15092f.png" title="Playa La Manzanilla - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c559c72336be9cfcf12f2634521d548a.jpg" title="Infinity - Michael Vignola"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7fc43684bb10569ac2a57f847b1a86e9.jpg" title="Pinkfong Animal Songs - Pinkfong"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/52a7cfefbb075f71860ad604a282d1de.jpg" title="Owen - RØRE"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5526cfe62a8b32bc1cbcde8460e82784.jpg" title="Heroes - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/73c397b11f2ae3062951082a0d4ffd01.png" title="Waves - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ac4d74337de3d9e00323bda25067f074.jpg" title="Kingdom - Arcade High"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/00f4aef783c07afd0bd8e33f84051362.png" title="The Sweet Escape - Gwen Stefani"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ca322effcd218041a89adbc28c63c9ba.jpg" title="PEP - Lights"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0605ac94ee875e46631c7d33fed07bb7.jpg" title="Ashley - RØRE"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/debfd82986a73ee82c651cc4a3e914f5.jpg" title="Night Drive - Timecop1983"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ad4fc37ea08fc33ec7e90b240a6c1127.jpg" title="Violin Dreams, Vol. 3 - Violin Sky"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e5456f90c6ec3a5508a8729130a1c3b5.jpg" title="Bluey the Album (Music from the Original TV Series) - Bluey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/26bd3e9d20adfe47cb96d2b2d15fe6d7.jpg" title="If I Don't See You Again - BPMoore"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7ed34387ae83322bcc0a1f76625ce308.jpg" title="Komorebi (Reworks) - BPMoore"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0c94c86afc2e69bdb65bbe3875af3634.jpg" title="Leather Temple - Carpenter Brut"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c0c12ac9f2afc4ac0a8924b9ac1a6c72.jpg" title="Genesis - David A. Molina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1cd59f70b7505dc1c43d7a207d21fe0e.jpg" title="Freyja's Calling - Eihwar"> </p>

          
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

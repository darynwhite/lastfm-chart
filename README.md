# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3a732f7dd6ddc9f50e84c97875b6192c.jpg" title="A Moment Apart (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/661ada0e5b6925b9d781dfaf63b96d88.jpg" title="Live at Lafayette - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/99947e68c0f44af76f1559af8734afd0.jpg" title="Gunship - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/85ee26d039d6495895f5e952d4df35d9.jpg" title="Summer's Gone - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ac4d74337de3d9e00323bda25067f074.jpg" title="Kingdom - Arcade High"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7fc43684bb10569ac2a57f847b1a86e9.jpg" title="Pinkfong Animal Songs - Pinkfong"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e5456f90c6ec3a5508a8729130a1c3b5.jpg" title="Bluey the Album (Music from the Original TV Series) - Bluey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0c94c86afc2e69bdb65bbe3875af3634.jpg" title="Leather Temple - Carpenter Brut"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/71626987f1c390c96b7f851f6d45b2b2.jpg" title="Atlas - FM-84"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/73373b8ae807b85cd48af94098edf0e6.jpg" title="Moderns - Moderns"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3917cae81c0ab6a71aa718ee233d3005.jpg" title="Breaking Up - all the damn vampires"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/91a0db98c65a6d41c6be93a644328469.png" title="Love like an Ocean - Austin Fray"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/81c89a3bfac3fa2b098fb6fd62b11c1d.jpg" title="Leather Terror - Carpenter Brut"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ef1138fa8ef53d3bdafba9fc6d8ce19c.jpg" title="Berserker [Feat. Dave Lombardo] - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b91306cb19bedec5a26f14729070eb7c.jpg" title="China in Your Hand (feat. Tim Cappello) - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/84d982a6389e4d09d328e4cc596bee8f.jpg" title="CTHULHU - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f9a6c00d6e6d335ec4db783058f7251c.jpg" title="Eleanor Rigby - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b2e21980dcea9d6b963c04535ca2c895.jpg" title="Mad World - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a1e60a766645a19d37ebef41185516a1.jpg" title="Send Me An Angel - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b7c6f3dadc54e467d7b596c3652be8f4.jpg" title="Tell Me When the World Stops Ending - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1065769c7075a95c857ab4af93b71561.jpg" title="The Vale Of Shadows - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8d20d80f6006b41329f03c449488f856.jpg" title="The Video Game Champion - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/00f4aef783c07afd0bd8e33f84051362.png" title="The Sweet Escape - Gwen Stefani"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/622afc3ebae6786da46c20c78ec7f187.jpg" title="Sentimental - Miami Nights 1984"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f9e81719429bb2a5b9162008faa41333.jpg" title="Sing (Original Motion Picture Soundtrack Deluxe) - Nick Kroll & Reese Witherspoon"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ed2eadee2980ffb1f1f995a4965d00c9.jpg" title="Songs About People Including Myself (Deluxe Edition) - The Bad Dreamers"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d3cf8de714db8ae71fca77a095d2a368.jpg" title="Space and Time (Deluxe Edition) - The Bad Dreamers"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5526cfe62a8b32bc1cbcde8460e82784.jpg" title="Heroes - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ba94778da3408d44cb8e9f1ba965224d.jpg" title="My Delorean - Timecop1983"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/64772d9e49a0b819ff07aa13957e01de.jpg" title="Bots Don't Cry - Trevor Something"> </p>

          
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

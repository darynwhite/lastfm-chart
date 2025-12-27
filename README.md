# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/6d8092b0c5c550eced96c7593ec9d151.jpg" title="Kaskade Christmas Deluxe - Kaskade"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c90f4bd7d8218ab0f67de086e6b1063e.jpg" title="Jasper - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f5270041983b7b838c2093f3042927d2.jpg" title="Echo Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d40551abbc08130b690acc64e51c6607.png" title="Christmas (Deluxe 10th Anniversary Edition) - Michael Bublé"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0ea1f680b8c9884266c56f37340b1b7c.jpg" title="I Dream Of Christmas (Extended) - Norah Jones"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/864eff2973cf26721a04df6507c1ab67.jpg" title="A Charlie Brown Christmas [2012 Remastered & Expanded Edition] - Vince Guaraldi Trio"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3ee4ff8a44b547d28f3020ff8d2d31d8.jpg" title="What A Night! A Christmas Album - Harry Connick, Jr."> <img src="https://lastfm.freetls.fastly.net/i/u/34s/33483a740afc298be82eb8e799750f4b.jpg" title="A Pentatonix Christmas Deluxe - Pentatonix"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/72e0f8cd5fc2df808c6b478c4797880e.jpg" title="Snow Waltz - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/26dad4b17fd36ec94b6bb154eec17e8f.jpg" title="Warmer In The Winter (Deluxe Edition) - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63ae49d15df3c1acd2a89ca2294cc039.jpg" title="Singing Sands - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/715bd82463f74ae2bf5aec55d3bfddcc.jpg" title="When My Heart Finds Christmas - Harry Connick, Jr."> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ffc4a6e9d0ac31f4aa31e4812f925103.jpg" title="The Songs the Season Brings, Vols. 1-4 - Beta Radio"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a5c3187cd2e856a58bf5b31ac15092f.png" title="Playa La Manzanilla - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3da8f5454f35a9cae73175113a23484f.jpg" title="Bing At Christmas - Bing Crosby"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9e37f6c83d397a307b7fcf1460536781.jpg" title="Great Ocean Road - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b1980c8760bc014d550434a61e920212.jpg" title="Josephine Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cc8e6c6cf1eaa64efd7f8f2d542b76cf.png" title="A Ben Rector Christmas - Ben Rector"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e130b388ea12684a6ae966c5a9da7e52.jpg" title="Bridal Veil Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4e452d7e6079b1575444d874a2538c42.jpg" title="Niagara Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ed5339e8710c8131e03fd0c81ad3c56f.jpg" title="Lake Wakatipu - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c8cc833e2085065d2b43cd0e5300076.jpg" title="Shuswap Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/529645dcda01fd7f3d63fba1c760ff5b.jpg" title="Tofino - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/84ae65bf64483855ed89b307c58ef15d.jpg" title="This Christmas - Jess Glynne"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/50ca1f960fe2e4d1af069c3b8fcb25ff.jpg" title="Spotify Singles - Christmas - Jon Batiste"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3ea95e5f646d0b74ba63e729e8c93c00.jpg" title="Do You Hear What I Hear? - Andrea Bocelli"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7f3ab00fc2864d73cb4903995eb64e4e.jpg" title="I Dream Of Christmas (Deluxe) - Norah Jones"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d7854d459270ee0f7494c5b0619b6706.jpg" title="Mirror Master - Young the Giant"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a0d2a9123d3a2c4dca4a46415e0a4e11.jpg" title="Imagine - Armin van Buuren"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d6e7200ad6360100997770fa3f3c08ae.jpg" title="Hugrheim - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5dfbba3f6d7d860d2bcc5f7917bea2d3.jpg" title="And on Earth, Peace - Salt Of The Sound"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9319defe8e7c983537347ae52d942656.jpg" title="It's a Holiday Soul Party - Sharon Jones & The Dap-Kings"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/140036e36b484aeca2c8ff63ce460a8d.jpg" title="Sirens of the Sea - Above & Beyond"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/68b6aa6accb74b3b8c8320295d8b2133.jpg" title="All the Best - ATB"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1d131d8e6e13431abeb2c02c1bc2a08a.jpg" title="Distant Earth (Deluxe Version) - ATB"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/94ba45aa7bf704cdc6dc0ad97fee6e2b.jpg" title="The New Daylight - Dash Berlin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fa69254c380cde627ab6772be81e831d.jpg" title="Christmas Time Is Here b/w Christmas Time Is Here (Version Mary) - Khruangbin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/59216dbc238285ac3b240f855237e515.jpg" title="Everyday is Christmas (Deluxe Edition) - Sia"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/563eb940816eec03de47f0e7fb9d0c82.jpg" title="Right Back - Yuri Kane"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2dea73a8712a7ccd61787961a0313e92.jpg" title="On A Good Day (Metropolis) - Above"> </p>

          
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

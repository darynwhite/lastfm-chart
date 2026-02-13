# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/c90f4bd7d8218ab0f67de086e6b1063e.jpg" title="Jasper - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3a732f7dd6ddc9f50e84c97875b6192c.jpg" title="A Moment Apart (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c9add86eac5aa56f7e36f916e4095380.gif" title="The Last Goodbye Tour Live - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7ade51bd6cd0175a05549e68a04bea54.jpg" title="The Last Goodbye (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b1980c8760bc014d550434a61e920212.jpg" title="Josephine Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4e452d7e6079b1575444d874a2538c42.jpg" title="Niagara Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/95716b6e75284516307f57088aa41cf5.jpg" title="Duality - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a4b0ca89a071af2b87aa9e24cd7b9294.jpg" title="Viking War Trance - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a5c3187cd2e856a58bf5b31ac15092f.png" title="Playa La Manzanilla - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9e37f6c83d397a307b7fcf1460536781.jpg" title="Great Ocean Road - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8816946dc53e5400bda5c0bb1ee487a.jpg" title="Summer's Gone (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d4ae381d45f9fc9ac7e687e33178a93b.jpg" title="In Return (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f5270041983b7b838c2093f3042927d2.jpg" title="Echo Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/529645dcda01fd7f3d63fba1c760ff5b.jpg" title="Tofino - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63ae49d15df3c1acd2a89ca2294cc039.jpg" title="Singing Sands - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c718e6a741403ac46d45b7195e52b826.jpg" title="Dance Mode! - Bluey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ed5339e8710c8131e03fd0c81ad3c56f.jpg" title="Lake Wakatipu - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7ab9da3c4fd89b55c8deab4729bee528.png" title="Trophy Mountain - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c804b2219fb1978fd44013c9bfa5e24.jpg" title="Endless Summer - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37495917b4e632c097de92248b3f90ff.jpg" title="A Moment Apart - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a4bc05c59aa286d875d031437df390f.jpg" title="The Beginning - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/16e39fd39917aa2f93d8ad09530a07fc.jpg" title="DRIVE - Tiësto"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d5958ccf1f07c002491235ca3b9767de.jpg" title="Wails (Songs for Grief) - Alexandra Blakely"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fe0771a88192919d93a06eddbbf51447.jpg" title="The Stories We Forgot - Andreas Kübler"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e130b388ea12684a6ae966c5a9da7e52.jpg" title="Bridal Veil Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d6f7b0341cbe4398e951b361cb6f2b2c.jpg" title="Walkerworld - Alan Walker"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1cd59f70b7505dc1c43d7a207d21fe0e.jpg" title="Freyja's Calling - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7940fbb1df766b4683951aed490a8b5a.jpg" title="Fine Line - Harry Styles"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cb85495b0bfd40ebc0ba63618ad5b551.png" title="Shatter Me - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7fc43684bb10569ac2a57f847b1a86e9.jpg" title="Pinkfong Animal Songs - Pinkfong"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/168f82eeef4e127a336d647d0b81a799.png" title="FanTaisia Ambience, Vol. 2 - Thomas J. Curran"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/edd2112eb9f0d142689937c4638380b8.jpg" title="Madagascar: Escape 2 Africa (Music from the Motion Picture) - Various Artists"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/488c1cd998e80dec58b42b3330f9bcaf.jpg" title="Of This Blood - Daridel"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/86c68338f464a97424b5b8e175542974.jpg" title="Thank You (Not So Bad) - Dimitri Vegas & Like Mike"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3495bf3cc42429b1d919dde5eaf15ed4.jpg" title="Forgotten Odes - Eternal Eclipse"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/71626987f1c390c96b7f851f6d45b2b2.jpg" title="Atlas - FM-84"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/00f4aef783c07afd0bd8e33f84051362.png" title="The Sweet Escape - Gwen Stefani"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/85ee26d039d6495895f5e952d4df35d9.jpg" title="Summer's Gone - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/97506189f8b2031b2b6a43dda841383e.jpg" title="The Last Goodbye - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2a54ef64de03a88b21ec42dd7c711e53.jpg" title="Salt & Silence - Said The Sky"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5526cfe62a8b32bc1cbcde8460e82784.jpg" title="Heroes - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b48cf08f855336dc32c48ba0f7362bd9.jpg" title="Horror Show - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/271fe787620fe27994ff66616d529e1f.jpg" title="Kids - The Midnight"> </p>

          
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

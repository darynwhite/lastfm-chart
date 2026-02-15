# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/3a732f7dd6ddc9f50e84c97875b6192c.jpg" title="A Moment Apart (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c90f4bd7d8218ab0f67de086e6b1063e.jpg" title="Jasper - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c9add86eac5aa56f7e36f916e4095380.gif" title="The Last Goodbye Tour Live - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/95716b6e75284516307f57088aa41cf5.jpg" title="Duality - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4e452d7e6079b1575444d874a2538c42.jpg" title="Niagara Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9b4f0aeaacebbed4f77b21d4cd059673.png" title="Still on My Mind (Deluxe Edition) - Dido"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7ade51bd6cd0175a05549e68a04bea54.jpg" title="The Last Goodbye (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a4b0ca89a071af2b87aa9e24cd7b9294.jpg" title="Viking War Trance - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b1980c8760bc014d550434a61e920212.jpg" title="Josephine Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f5270041983b7b838c2093f3042927d2.jpg" title="Echo Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9e37f6c83d397a307b7fcf1460536781.jpg" title="Great Ocean Road - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a5c3187cd2e856a58bf5b31ac15092f.png" title="Playa La Manzanilla - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c804b2219fb1978fd44013c9bfa5e24.jpg" title="Endless Summer - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c718e6a741403ac46d45b7195e52b826.jpg" title="Dance Mode! - Bluey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37495917b4e632c097de92248b3f90ff.jpg" title="A Moment Apart - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c58a52dc481bbb5158f9691e1f1f70e4.jpg" title="Siðr - Vígundr"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a4bc05c59aa286d875d031437df390f.jpg" title="The Beginning - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cb85495b0bfd40ebc0ba63618ad5b551.png" title="Shatter Me - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/529645dcda01fd7f3d63fba1c760ff5b.jpg" title="Tofino - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/debfd82986a73ee82c651cc4a3e914f5.jpg" title="Night Drive - Timecop1983"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d6f7b0341cbe4398e951b361cb6f2b2c.jpg" title="Walkerworld - Alan Walker"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fe0771a88192919d93a06eddbbf51447.jpg" title="The Stories We Forgot - Andreas Kübler"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/168f82eeef4e127a336d647d0b81a799.png" title="FanTaisia Ambience, Vol. 2 - Thomas J. Curran"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/16e39fd39917aa2f93d8ad09530a07fc.jpg" title="DRIVE - Tiësto"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/10408aee66f2cc81f20b0a7037b91205.jpg" title="A Light On The Hill - Andreas Kübler"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7940fbb1df766b4683951aed490a8b5a.jpg" title="Fine Line - Harry Styles"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7fc43684bb10569ac2a57f847b1a86e9.jpg" title="Pinkfong Animal Songs - Pinkfong"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b9f9febd880dbe9ce34efea03e779818.jpg" title="The Lost Years - The Strike"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/edd2112eb9f0d142689937c4638380b8.jpg" title="Madagascar: Escape 2 Africa (Music from the Motion Picture) - Various Artists"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9df88bfe6a60e90533a9ce876c3fccc5.jpg" title="Infinity - W O L F C L U B"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/488c1cd998e80dec58b42b3330f9bcaf.jpg" title="Of This Blood - Daridel"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/86c68338f464a97424b5b8e175542974.jpg" title="Thank You (Not So Bad) - Dimitri Vegas & Like Mike"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/442cbaebe4fa097a79aba53edf2aaefc.jpg" title="Little Love - Elderbrook"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3495bf3cc42429b1d919dde5eaf15ed4.jpg" title="Forgotten Odes - Eternal Eclipse"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/71626987f1c390c96b7f851f6d45b2b2.jpg" title="Atlas - FM-84"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f6a9640156204dbe55b831cd30641b75.jpg" title="Satellites - GAMPER & DADONI"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/00f4aef783c07afd0bd8e33f84051362.png" title="The Sweet Escape - Gwen Stefani"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a563a1e6b833fc4d394bccf5dd7f72a4.jpg" title="Worlds Apart - Killstarr"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/01ebc7fa73b5ff16b585dc4fca0a75f3.jpg" title="No Hope State (GUNSHIP remix) - Lionface"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/dcaa744eba5808a1026e9c693c96acaf.jpg" title="Synthian - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/97506189f8b2031b2b6a43dda841383e.jpg" title="The Last Goodbye - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c252c625f0ec6784ed170ed0a5862328.png" title="Paradise Again - Swedish House Mafia"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c4df325ed3bd69531e1d3b7fa2619348.jpg" title="Clean Eyes (The Midnight Remix) - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d3cf8de714db8ae71fca77a095d2a368.jpg" title="Space and Time (Deluxe Edition) - The Bad Dreamers"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/79b5f8ccbf7b93c114e1b75879b5bc22.jpg" title="Fm - The Lightning Kids"> </p>

          
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

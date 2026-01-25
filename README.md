# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c90f4bd7d8218ab0f67de086e6b1063e.jpg" title="Jasper - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b1980c8760bc014d550434a61e920212.jpg" title="Josephine Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4e452d7e6079b1575444d874a2538c42.jpg" title="Niagara Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a4bc05c59aa286d875d031437df390f.jpg" title="The Beginning - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0c4b4d65203882c7b78bb629f38cb3c2.jpg" title="Horror Show (The Instrumentals) - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a5c3187cd2e856a58bf5b31ac15092f.png" title="Playa La Manzanilla - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/889c0c3371311a85f09e786b454af69d.jpg" title="Synthian (Deluxe Edition) - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/89cfda3a0da1a6ef6f32df88a80aaf90.jpg" title="Stillwater: Vol. 1 (Apple TV+ Original Series Soundtrack) - Kishi Bashi"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/99947e68c0f44af76f1559af8734afd0.jpg" title="Gunship - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9e37f6c83d397a307b7fcf1460536781.jpg" title="Great Ocean Road - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c804b2219fb1978fd44013c9bfa5e24.jpg" title="Endless Summer - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8d20d80f6006b41329f03c449488f856.jpg" title="The Video Game Champion - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/529645dcda01fd7f3d63fba1c760ff5b.jpg" title="Tofino - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63ae49d15df3c1acd2a89ca2294cc039.jpg" title="Singing Sands - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c9add86eac5aa56f7e36f916e4095380.gif" title="The Last Goodbye Tour Live - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8816946dc53e5400bda5c0bb1ee487a.jpg" title="Summer's Gone (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5bfd15751e53493ac9bb7af3632894fc.jpg" title="Béla Fleck & Abigail Washburn - Béla Fleck"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/dc5b100d3f4d4cf288f94fc182d7c383.jpg" title="Undux - Kaskade"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5526cfe62a8b32bc1cbcde8460e82784.jpg" title="Heroes - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d6f7b0341cbe4398e951b361cb6f2b2c.jpg" title="Walkerworld - Alan Walker"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6990c00edfa3af889bd48ab7b738de0e.jpg" title="Soon Comes Night - Carling & Will"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b9c6c9c5345f4d62c370e9bb2fbc6cb3.jpg" title="Formations - HawkTail"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fafced51af0a546384ce47b49e1ab341.jpg" title="Kx5 - kx5"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/82ae532ba0ffabcb4ae06708b9637fdf.jpg" title="I'll Wait - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c252c625f0ec6784ed170ed0a5862328.png" title="Paradise Again - Swedish House Mafia"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4011010ab1b2388cdf92c61afc637c11.jpg" title="Song of the Traveling Daughter (Bonus Track Version) - Abigail Washburn"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f0cf7332eecac872f8f285913967a7e7.jpg" title="Genesys II - Anyma"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5afe56fc6f01e5276e7e68ca2521598c.jpg" title="Herja - Danheim"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/138781cf56a8d3f1e67eb46ed6a0bd35.jpg" title="Nightcall - Essenger"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3410c69b8e221724593c87cc25b972d7.jpg" title="Kingdom Two Crowns: Norse Lands Soundtrack (Extended) - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/95716b6e75284516307f57088aa41cf5.jpg" title="Duality - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6f63d2fd323ac23d4f8a15f3ff09b280.jpg" title="Howl - A Tergo Lupi"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8e30f6f724f3c03c82d3fb5352ac51e.jpg" title="Walkerworld 2.0 - Alan Walker"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8f6af29213ee7a3bb5456af0d8aeadff.jpg" title="Echo In the Valley - Béla Fleck"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9a2c1ffd7f39ff69b3b1d6c82bafc793.jpg" title="Throw Down Your Heart: The Complete Africa Sessions - Béla Fleck"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3d3d6d2b41544f42b8f750b6abdbd180.png" title="A Rush of Blood to the Head - Coldplay"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1cae8d2ec21c7ad6c6b23559d86ab0a9.jpg" title="Jardins migrateurs - Constantinople"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3495bf3cc42429b1d919dde5eaf15ed4.jpg" title="Forgotten Odes - Eternal Eclipse"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9609be9267d8bb819018fff6dc1652e1.jpg" title="Place of Growth - HawkTail"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e5a997b83ae3cc6426cc8378d1578a56.jpg" title="DUSK - Hayla"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8a0231ab72ddaa63594ebe50e0dfaeb.jpg" title="Rise of The Wise - Jauz"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/25fc026ca0b539c43028ed67ba59a1b2.jpg" title="Skip, Hop and Wobble - Jerry Douglas"> </p>

          
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

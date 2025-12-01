# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/f5270041983b7b838c2093f3042927d2.jpg" title="Echo Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c90f4bd7d8218ab0f67de086e6b1063e.jpg" title="Jasper - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63ae49d15df3c1acd2a89ca2294cc039.jpg" title="Singing Sands - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/95716b6e75284516307f57088aa41cf5.jpg" title="Duality - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d40551abbc08130b690acc64e51c6607.png" title="Christmas (Deluxe 10th Anniversary Edition) - Michael Bublé"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/26dad4b17fd36ec94b6bb154eec17e8f.jpg" title="Warmer In The Winter (Deluxe Edition) - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0ea1f680b8c9884266c56f37340b1b7c.jpg" title="I Dream Of Christmas (Extended) - Norah Jones"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/33483a740afc298be82eb8e799750f4b.jpg" title="A Pentatonix Christmas Deluxe - Pentatonix"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/08299b0209da9912f380404686840e58.jpg" title="A Legendary Christmas - John Legend"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6d8092b0c5c550eced96c7593ec9d151.jpg" title="Kaskade Christmas Deluxe - Kaskade"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/72e0f8cd5fc2df808c6b478c4797880e.jpg" title="Snow Waltz - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/16e39fd39917aa2f93d8ad09530a07fc.jpg" title="DRIVE - Tiësto"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3ee4ff8a44b547d28f3020ff8d2d31d8.jpg" title="What A Night! A Christmas Album - Harry Connick, Jr."> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d069853d4480ae689182753a92bf9fcd.jpg" title="DRIVE Continuous DJ Mix - Tiësto"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/864eff2973cf26721a04df6507c1ab67.jpg" title="A Charlie Brown Christmas [2012 Remastered & Expanded Edition] - Vince Guaraldi Trio"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/715bd82463f74ae2bf5aec55d3bfddcc.jpg" title="When My Heart Finds Christmas - Harry Connick, Jr."> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3410c69b8e221724593c87cc25b972d7.jpg" title="Kingdom Two Crowns: Norse Lands Soundtrack (Extended) - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/282c3bf58a2d2d9b99be592321d8760c.jpg" title="A Frame of Mind - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9e37f6c83d397a307b7fcf1460536781.jpg" title="Great Ocean Road - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a5c3187cd2e856a58bf5b31ac15092f.png" title="Playa La Manzanilla - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3da8f5454f35a9cae73175113a23484f.jpg" title="Bing At Christmas - Bing Crosby"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ed5339e8710c8131e03fd0c81ad3c56f.jpg" title="Lake Wakatipu - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e130b388ea12684a6ae966c5a9da7e52.jpg" title="Bridal Veil Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/aef76153fac847de492126d416b1647e.png" title="The London Sessions - Tiësto"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ffc4a6e9d0ac31f4aa31e4812f925103.jpg" title="The Songs the Season Brings, Vols. 1-4 - Beta Radio"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8636bbaee9b7eceac0952921238a22e1.jpg" title="Love On The Edge Of Desire - The Lightning Kids"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0c4b4d65203882c7b78bb629f38cb3c2.jpg" title="Horror Show (The Instrumentals) - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e7afa92b8a8e4ecc3e5e7b1a0ec18e6b.png" title="Arcane league of legends: season 2 (soundtrack from the animated series) - Arcane"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37fd0fc15ff5e506a1cade4bb9a963dd.png" title="All My Demons Greeting Me as a Friend - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cc8e6c6cf1eaa64efd7f8f2d542b76cf.png" title="A Ben Rector Christmas - Ben Rector"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a4bc05c59aa286d875d031437df390f.jpg" title="The Beginning - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e51ad8d9c902894c41eae5406dfae03f.jpg" title="Where They Landed - BE/HOLD"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ffc0e1d52f4e4f16cf0349f8caca29e5.png" title="Smoke + Mirrors - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9c019286f3282154a84d5f149e2b938c.jpg" title="A6 - Lights"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37495917b4e632c097de92248b3f90ff.jpg" title="A Moment Apart - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c804b2219fb1978fd44013c9bfa5e24.jpg" title="Endless Summer - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b32f0d69a9f0ee06d441a02daff65569.jpg" title="Skye - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/66a56a70b0b5d8f19408b4a36b642c3b.jpg" title="Empty Streets - After Dark"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ae02aa9e5045384e79539f7587d43d09.jpg" title="Youth - aurora wave"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/45e46efa8719a8eb560fb50855531270.png" title="Slow Orbit - Ghost in Delay"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a07718112577313de2fb78645b859677.png" title="last night you said you missed me - Hazlett"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9e1dc1739e38d10229dc417e617f3134.jpg" title="Detective Story - Isidor"> </p>

          
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

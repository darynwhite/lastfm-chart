# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/6d8092b0c5c550eced96c7593ec9d151.jpg" title="Kaskade Christmas Deluxe - Kaskade"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d40551abbc08130b690acc64e51c6607.png" title="Christmas (Deluxe 10th Anniversary Edition) - Michael Bublé"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f5270041983b7b838c2093f3042927d2.jpg" title="Echo Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/33483a740afc298be82eb8e799750f4b.jpg" title="A Pentatonix Christmas Deluxe - Pentatonix"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c90f4bd7d8218ab0f67de086e6b1063e.jpg" title="Jasper - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/72e0f8cd5fc2df808c6b478c4797880e.jpg" title="Snow Waltz - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/26dad4b17fd36ec94b6bb154eec17e8f.jpg" title="Warmer In The Winter (Deluxe Edition) - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ffc4a6e9d0ac31f4aa31e4812f925103.jpg" title="The Songs the Season Brings, Vols. 1-4 - Beta Radio"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/715bd82463f74ae2bf5aec55d3bfddcc.jpg" title="When My Heart Finds Christmas - Harry Connick, Jr."> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3da8f5454f35a9cae73175113a23484f.jpg" title="Bing At Christmas - Bing Crosby"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63ae49d15df3c1acd2a89ca2294cc039.jpg" title="Singing Sands - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0ea1f680b8c9884266c56f37340b1b7c.jpg" title="I Dream Of Christmas (Extended) - Norah Jones"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3ee4ff8a44b547d28f3020ff8d2d31d8.jpg" title="What A Night! A Christmas Album - Harry Connick, Jr."> <img src="https://lastfm.freetls.fastly.net/i/u/34s/864eff2973cf26721a04df6507c1ab67.jpg" title="A Charlie Brown Christmas [2012 Remastered & Expanded Edition] - Vince Guaraldi Trio"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/08299b0209da9912f380404686840e58.jpg" title="A Legendary Christmas - John Legend"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a5c3187cd2e856a58bf5b31ac15092f.png" title="Playa La Manzanilla - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e130b388ea12684a6ae966c5a9da7e52.jpg" title="Bridal Veil Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ed5339e8710c8131e03fd0c81ad3c56f.jpg" title="Lake Wakatipu - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/95716b6e75284516307f57088aa41cf5.jpg" title="Duality - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cc8e6c6cf1eaa64efd7f8f2d542b76cf.png" title="A Ben Rector Christmas - Ben Rector"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9e37f6c83d397a307b7fcf1460536781.jpg" title="Great Ocean Road - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c8cc833e2085065d2b43cd0e5300076.jpg" title="Shuswap Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/874958bdf0bf4f9c3aa5e90f1b57426a.jpg" title="Waterton Lakes - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/50ca1f960fe2e4d1af069c3b8fcb25ff.jpg" title="Spotify Singles - Christmas - Jon Batiste"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/717e255b6fcc47e3845180d1cb249092.png" title="Tracks in the Snow - The Civil Wars"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/16e39fd39917aa2f93d8ad09530a07fc.jpg" title="DRIVE - Tiësto"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/842b56f7710a429efde801a5bc218fc6.jpg" title="Peak District - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cfb32acc44fd2a22965e8ed12b4e0dda.jpg" title="FABLES, ACT I - Ekaterina Shelehova"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/84ae65bf64483855ed89b307c58ef15d.jpg" title="This Christmas - Jess Glynne"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a191a2114b6d7ca2691cfdc678b896b.jpg" title="Mørketid - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/282c3bf58a2d2d9b99be592321d8760c.jpg" title="A Frame of Mind - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3ea95e5f646d0b74ba63e729e8c93c00.jpg" title="Do You Hear What I Hear? - Andrea Bocelli"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ca7dcc5389a5316c0be959ae146cedaf.jpg" title="Comfort In Chaos - John Summit"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0b4521a6a84edb00f2a5bb8c35d3916a.png" title="Nomé Naku - Nomé Naku"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3dea6f6a6f1f4ce5d84d67221f2ce89d.jpg" title="After the storm - Ofdrykkja"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/058c273b14e7110725c2653880e639f1.jpg" title="Palomar Parade - Sons of the East"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6f0db1e7b2a74eebce9f709f76db3eba.png" title="Holidays Rule - Various Artists"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0f77b772e4a8a1096f53dc3d08e079bd.jpg" title="where do we end up when life goes on? (Deluxe Edition) - vian izak"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4698b933381a99dffdea6d0cd291f188.jpg" title="Bodies in Flight - Amelia Magdalena"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5e55d7c5a69162cd5c9a3a8551282241.jpg" title="The End Where I Begin - Amelia Magdalena"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a81389d27757cdfa90d4b3b85a6e65c4.jpg" title="When It Was Now - Atlas Genius"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4cd8ce91201d6d0a38b5b032b027a258.jpg" title="III - Candles & Beginnings - Auri"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c8235dab6027e15473e5c1f6abe24855.jpg" title="Superdream - Big Wild"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3b2ef685748ead643355510c3c919e29.jpg" title="So Certain (Something Reminds Me) - Blanco White"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/096678635d28a6c2813494bb2ba35f8d.jpg" title="desolate - ByErik ヵ"> </p>

          
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

# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e8ba53e4eb981b3dec8e72574248560f.jpg" title="Immortalized (Deluxe Edition) - Disturbed"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f5270041983b7b838c2093f3042927d2.jpg" title="Echo Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c90f4bd7d8218ab0f67de086e6b1063e.jpg" title="Jasper - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9e37f6c83d397a307b7fcf1460536781.jpg" title="Great Ocean Road - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a5c3187cd2e856a58bf5b31ac15092f.png" title="Playa La Manzanilla - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63ae49d15df3c1acd2a89ca2294cc039.jpg" title="Singing Sands - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/95716b6e75284516307f57088aa41cf5.jpg" title="Duality - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ed5339e8710c8131e03fd0c81ad3c56f.jpg" title="Lake Wakatipu - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e130b388ea12684a6ae966c5a9da7e52.jpg" title="Bridal Veil Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7ade51bd6cd0175a05549e68a04bea54.jpg" title="The Last Goodbye (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8816946dc53e5400bda5c0bb1ee487a.jpg" title="Summer's Gone (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/282c3bf58a2d2d9b99be592321d8760c.jpg" title="A Frame of Mind - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3410c69b8e221724593c87cc25b972d7.jpg" title="Kingdom Two Crowns: Norse Lands Soundtrack (Extended) - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a191a2114b6d7ca2691cfdc678b896b.jpg" title="Mørketid - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/66a212ca52b0b2005837c8b8c549378b.jpg" title="Seulement L'amour - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c8cc833e2085065d2b43cd0e5300076.jpg" title="Shuswap Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/874958bdf0bf4f9c3aa5e90f1b57426a.jpg" title="Waterton Lakes - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/842b56f7710a429efde801a5bc218fc6.jpg" title="Peak District - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0c4b4d65203882c7b78bb629f38cb3c2.jpg" title="Horror Show (The Instrumentals) - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e5456f90c6ec3a5508a8729130a1c3b5.jpg" title="Bluey the Album (Music from the Original TV Series) - Bluey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a4bc05c59aa286d875d031437df390f.jpg" title="The Beginning - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/096678635d28a6c2813494bb2ba35f8d.jpg" title="desolate - ByErik ヵ"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ffc0e1d52f4e4f16cf0349f8caca29e5.png" title="Smoke + Mirrors - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9c019286f3282154a84d5f149e2b938c.jpg" title="A6 - Lights"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b32f0d69a9f0ee06d441a02daff65569.jpg" title="Skye - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63e9b188c786835f816db3924a4e9308.jpg" title="Winged Dreams - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1d7294f31fa14d5acdb50963f53015a5.png" title="Ceremonials (Deluxe Edition) - Florence + the Machine"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3a732f7dd6ddc9f50e84c97875b6192c.jpg" title="A Moment Apart (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/debfd82986a73ee82c651cc4a3e914f5.jpg" title="Night Drive - Timecop1983"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b2e51674629feb5f41afe26c2a64b575.jpg" title=""Eine kleine Nachtmusik" - Mozart for Winter - Wolfgang Amadeus Mozart"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/19f29d16e30889b6cacd3eb8bf7e9192.jpg" title="Sailing - Alan Walker"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2588058f67e6fabcaff9811c0a2de9c3.jpg" title="Arcane league of legends: season 2 (soundtrack from the animated series) - Arcane"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37fd0fc15ff5e506a1cade4bb9a963dd.png" title="All My Demons Greeting Me as a Friend - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0e82f7d31a9733670f92d4a0dd0ef644.jpg" title="Love Minus 80 - Bunny X"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cfb32acc44fd2a22965e8ed12b4e0dda.jpg" title="FABLES, ACT I - Ekaterina Shelehova"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6ea4743cde9f2c5ca98a4cda735bacb4.jpg" title="My Mother Told Me - Ekaterina Shelehova"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cd9ee4d27628bdd6455d0f932946e46a.jpg" title="Another Touch - Elderbrook"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/41894236e2df21f5a0821179a03efd7c.jpg" title="Ask That God - Empire of the Sun"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2ebebd9a9f327c38d4e20ff0d04c100b.jpg" title="Mozart & Haydn for Horn & String Quartet - Felix Klieser"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/153cb088d5989154e6f90d78903f7450.jpg" title="Dance Fever - Florence + the Machine"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/240109b9b447f74cbfd11a4897374fc9.jpg" title="In My Arms - Illenium"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f51ff8d64b42135bcfe1c1579daec20d.jpg" title="In My Arms (KREAM Remix) - Illenium"> </p>

          
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

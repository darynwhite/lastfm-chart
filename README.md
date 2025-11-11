# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ac269a71e1803ee7fe6bdda4ddb7f4f5.jpg" title="Heimferd - Danheim"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a191a2114b6d7ca2691cfdc678b896b.jpg" title="Mørketid - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/282c3bf58a2d2d9b99be592321d8760c.jpg" title="A Frame of Mind - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f25ea79c455d2db06983f3b044cfd632.jpg" title="Í Ævir - Elinborg"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/df180b1a50e62cd2f26b8e4d179255e0.jpg" title="Love Is Like (Deluxe) - Maroon 5"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a4bc05c59aa286d875d031437df390f.jpg" title="The Beginning - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a4b0ca89a071af2b87aa9e24cd7b9294.jpg" title="Viking War Trance - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c718e6a741403ac46d45b7195e52b826.jpg" title="Dance Mode! - Bluey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c93902899b5f5d89a17dacedb752709d.jpg" title="The Land of in Between - Hannah Parrott"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ac63d205e527587451185e8f4d247ac7.jpg" title="Islet - Lindy-Fay Hella"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8aeb595c16551c909d9a1e6f90c32237.jpg" title="Hide - A Tergo Lupi"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/65da997c7d585ccc09d77d156e3b7c7a.png" title="Tilt - Hannah Parrott"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5526cfe62a8b32bc1cbcde8460e82784.jpg" title="Heroes - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/dadb0f42782f4295b7fd1cab4d4b1909.jpg" title="Dark Iron - Tiko Tiko"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63e9b188c786835f816db3924a4e9308.jpg" title="Winged Dreams - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/895edacacf2d35b4ce223b91948f16c6.jpg" title="Coast - Kollen"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f1b7d143c3a51fab755d3e453b07fa41.jpg" title="Eventyr II: Ættesanger - Kveld"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0c4b4d65203882c7b78bb629f38cb3c2.jpg" title="Horror Show (The Instrumentals) - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b32f0d69a9f0ee06d441a02daff65569.jpg" title="Skye - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/80cc7ee1a3d0c194f082b4feb3e96a77.png" title="Everybody Scream (Chamber Version) - Florence + the Machine"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/dcd595c00fa7122ec3e8cfcbcca71933.jpg" title="Estes - Judah Earl"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5afe56fc6f01e5276e7e68ca2521598c.jpg" title="Herja - Danheim"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/39cf604f9911853687368525ff1a9d51.jpg" title="Sjórok - Elinborg"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3df392d519ea4eecce0b67083ac15050.jpg" title="Fatou - Fatoumata Diawara"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/00f4aef783c07afd0bd8e33f84051362.png" title="The Sweet Escape - Gwen Stefani"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/96da77ffe81a20dee8eefe6c5c440977.jpg" title="Myrkr - Heldom"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1b48cd702f76b97c0b1be11fbb144bba.jpg" title="Vaknan - Heldom"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/49f0383ffa35456ba42b45305084fc7f.jpg" title="The Gospel Truth (Bonus Track Version) - Ida Sand"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3410c69b8e221724593c87cc25b972d7.jpg" title="Kingdom Two Crowns: Norse Lands Soundtrack (Extended) - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/79cba4d788d08c3429dbd92879a27d76.jpg" title="Eventyr I: Strid - Kveld"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f04407ac26465e7010150ace0c4bf8db.jpg" title="Dimensions - Ryan Taubert"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c804b2219fb1978fd44013c9bfa5e24.jpg" title="Endless Summer - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/442119ac078cba1ec65cd7dc6d894321.jpg" title="A Dream Through Open Eyes - The Strike"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/bdc19d5b400ee45d97ee7b070821c941.jpg" title="Better Believe - Tiko Tiko"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ad4fc37ea08fc33ec7e90b240a6c1127.jpg" title="Violin Dreams, Vol. 3 - Violin Sky"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e6555e743a42d348bfb1e76978825268.jpg" title="Runaljod - Ragnarok - Wardruna"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c717c383ef8ba187092f14dcba657c68.jpg" title="Odyssey - Aaron Hibell"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/354fb4e0f24a29d04000f77e0c4ce52f.jpg" title="Twilight Zone - Aaron Hibell"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b4972f03656762528c4e9e0b1e27198c.jpg" title="What Remains - Abilene"> </p>

          
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

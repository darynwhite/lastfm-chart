# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a191a2114b6d7ca2691cfdc678b896b.jpg" title="Mørketid - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ac269a71e1803ee7fe6bdda4ddb7f4f5.jpg" title="Heimferd - Danheim"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/282c3bf58a2d2d9b99be592321d8760c.jpg" title="A Frame of Mind - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/211d2fa9cff0ca90a33fbc64df7a205b.jpg" title="Lamomali Totem - -M-"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/df180b1a50e62cd2f26b8e4d179255e0.jpg" title="Love Is Like (Deluxe) - Maroon 5"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a4bc05c59aa286d875d031437df390f.jpg" title="The Beginning - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/99e31f65ce379bce221e24807944cfbc.jpg" title="The Payback - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a4b0ca89a071af2b87aa9e24cd7b9294.jpg" title="Viking War Trance - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f25ea79c455d2db06983f3b044cfd632.jpg" title="Í Ævir - Elinborg"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ac63d205e527587451185e8f4d247ac7.jpg" title="Islet - Lindy-Fay Hella"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8aeb595c16551c909d9a1e6f90c32237.jpg" title="Hide - A Tergo Lupi"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0ad59976ae86471b1aecfcd449f2e25e.jpg" title="80s Kids - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/af5ee011b7f8ce55a0e49954ef5c1f54.jpg" title="DRYVE (Deluxe) - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/66a212ca52b0b2005837c8b8c549378b.jpg" title="Seulement L'amour - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/00f4aef783c07afd0bd8e33f84051362.png" title="The Sweet Escape - Gwen Stefani"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f1b7d143c3a51fab755d3e453b07fa41.jpg" title="Eventyr II: Ættesanger - Kveld"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5526cfe62a8b32bc1cbcde8460e82784.jpg" title="Heroes - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0c4b4d65203882c7b78bb629f38cb3c2.jpg" title="Horror Show (The Instrumentals) - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b32f0d69a9f0ee06d441a02daff65569.jpg" title="Skye - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c718e6a741403ac46d45b7195e52b826.jpg" title="Dance Mode! - Bluey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3410c69b8e221724593c87cc25b972d7.jpg" title="Kingdom Two Crowns: Norse Lands Soundtrack (Extended) - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a6ee015fe1bc4d86cdb9b7c76778e7a6.jpg" title="Strange Trails - Lord Huron"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0dfc45f8ca8d06375bf275acf6314d2c.jpg" title="Woodland - The Paper Kites"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63e9b188c786835f816db3924a4e9308.jpg" title="Winged Dreams - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0e82f7d31a9733670f92d4a0dd0ef644.jpg" title="Love Minus 80 - Bunny X"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/39cf604f9911853687368525ff1a9d51.jpg" title="Sjórok - Elinborg"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3df392d519ea4eecce0b67083ac15050.jpg" title="Fatou - Fatoumata Diawara"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/80cc7ee1a3d0c194f082b4feb3e96a77.png" title="Everybody Scream (Chamber Version) - Florence + the Machine"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/96da77ffe81a20dee8eefe6c5c440977.jpg" title="Myrkr - Heldom"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1b48cd702f76b97c0b1be11fbb144bba.jpg" title="Vaknan - Heldom"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/49f0383ffa35456ba42b45305084fc7f.jpg" title="The Gospel Truth (Bonus Track Version) - Ida Sand"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8c77e9f509c4dd3bca8d3ac6b5344ce5.png" title="Evolve - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/87138bbda83bd0ae8b4da2b6cab9b66a.jpg" title="Everybody Else Is Doing It, So Why Can't We? - The Cranberries"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/442119ac078cba1ec65cd7dc6d894321.jpg" title="A Dream Through Open Eyes - The Strike"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ad4fc37ea08fc33ec7e90b240a6c1127.jpg" title="Violin Dreams, Vol. 3 - Violin Sky"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9df88bfe6a60e90533a9ce876c3fccc5.jpg" title="Infinity - W O L F C L U B"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e6555e743a42d348bfb1e76978825268.jpg" title="Runaljod - Ragnarok - Wardruna"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b4972f03656762528c4e9e0b1e27198c.jpg" title="What Remains - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/21fee130705b381b5087ee22a3244fb1.jpg" title="Nightshade - Andrew Belle"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1c3e9db49f7ba396e15eda9985b7a30a.png" title="II - Those We Don't Speak Of - Auri"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4cd8ce91201d6d0a38b5b032b027a258.jpg" title="III - Candles & Beginnings - Auri"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/700416badcde194ec1319d86b4d22b0a.jpg" title="Dopamine - BØRNS"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e6ba2e725c70bd0a559e373852da5333.jpg" title="Heartbeats - Coastal"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5afe56fc6f01e5276e7e68ca2521598c.jpg" title="Herja - Danheim"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/afd0ead8692b8e9dbcdb941da4ab5e03.jpg" title="Munarvagr - Danheim"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/abb20fe6cb1f02d8cb0f47d33c5f1e55.jpg" title="Skapanir - Danheim"> </p>

          
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

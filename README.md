# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/c9add86eac5aa56f7e36f916e4095380.gif" title="The Last Goodbye Tour Live - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3a732f7dd6ddc9f50e84c97875b6192c.jpg" title="A Moment Apart (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3b34f6f1b339e9857fb276c318cb8b05.jpg" title="All My Demons Greeting Me As A Friend (Deluxe) - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f54f3b6ef26445a5bbb8a72f0f7830bd.png" title="True - Avicii"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7ade51bd6cd0175a05549e68a04bea54.jpg" title="The Last Goodbye (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d4ae381d45f9fc9ac7e687e33178a93b.jpg" title="In Return (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9c019286f3282154a84d5f149e2b938c.jpg" title="A6 - Lights"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8c77e9f509c4dd3bca8d3ac6b5344ce5.png" title="Evolve - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8816946dc53e5400bda5c0bb1ee487a.jpg" title="Summer's Gone (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2c1865ea719cad02d91852b2f3ee5ab4.jpg" title="Avicii Forever - Avicii"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f2bdf437849a9aa2d4c2451e3621f1ec.png" title="Tim - Avicii"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c804b2219fb1978fd44013c9bfa5e24.jpg" title="Endless Summer - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7e11890eb230518924d132ee1e31ec37.jpg" title="Stories - Avicii"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c1e4c4a2fb354132c100b3f654e6f34d.png" title="The Days / Nights - Avicii"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37495917b4e632c097de92248b3f90ff.jpg" title="A Moment Apart - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63e9b188c786835f816db3924a4e9308.jpg" title="Winged Dreams - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7a0fd61905374089c0898055aab50fa9.jpg" title="In Return - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9de1a08a9d1da269d71fcec90b7769b8.jpg" title="A Way Home - Omar Raafat"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0605ac94ee875e46631c7d33fed07bb7.jpg" title="Ashley - RØRE"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/52a7cfefbb075f71860ad604a282d1de.jpg" title="Owen - RØRE"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b7be747d414943fdc3f4de682eac3c7c.jpg" title="Ghost Stories - Coldplay"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5f57e62ee82c1a4b337d779bd02ef073.jpg" title="Meniscus - David Celeste"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a4bc05c59aa286d875d031437df390f.jpg" title="The Beginning - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2a19a6b7e1d9470db7f447e5a4aa73b8.png" title="Save The World - Swedish House Mafia"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a271fbaaaa024a1dca49a5b7aeb23166.png" title="Black Bear - Andrew Belle"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37fd0fc15ff5e506a1cade4bb9a963dd.png" title="All My Demons Greeting Me as a Friend - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/54c180355bd972ed5ddf8879e969b8ce.jpg" title="Conscious - Francis Wells"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/00f4aef783c07afd0bd8e33f84051362.png" title="The Sweet Escape - Gwen Stefani"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/22fae11f52714165e3efeca3c14084ea.jpg" title="Origins (Deluxe) - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/895edacacf2d35b4ce223b91948f16c6.jpg" title="Coast - Kollen"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a0e4f50e2d4611b8956f7f15f0b00aa.jpg" title="Don't You Worry Child - Swedish House Mafia"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b9f9febd880dbe9ce34efea03e779818.jpg" title="The Lost Years - The Strike"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b32f0d69a9f0ee06d441a02daff65569.jpg" title="Skye - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/bab022a4cc4a16f5bab01c6c95e6be8d.jpg" title="The Gods We Can Touch - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e7667409a4e033043d4c85895aae0d49.jpg" title="6’s to 9’s (Remixes) - Big Wild"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/99947e68c0f44af76f1559af8734afd0.jpg" title="Gunship - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7e9623e023b650e1963691fb09b5182e.jpg" title="Eternal Embers - Meltt"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/85ee26d039d6495895f5e952d4df35d9.jpg" title="Summer's Gone - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/23e374d5e82f1c744be303591fe40d6c.jpg" title="Shadowverse - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7a4535e88a384512c5e8fdda28245485.jpg" title="Music for Mountains - Thomas James White"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a7403c29da998233a0ce507bf321862b.jpg" title="Somnia - Abbott"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b4972f03656762528c4e9e0b1e27198c.jpg" title="What Remains - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6ee30bddb52af8502fb2ce57af8db8cc.jpg" title="Different World - Alan Walker"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8e30f6f724f3c03c82d3fb5352ac51e.jpg" title="Walkerworld 2.0 - Alan Walker"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/05164ba8eb074e355815dc6a5d800521.jpg" title="You Can’t Run From Yourself (From "Kaiju No. 8") - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/700416badcde194ec1319d86b4d22b0a.jpg" title="Dopamine - BØRNS"> </p>

          
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

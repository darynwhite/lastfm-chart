# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/c7e16a3e89f26dead6fe558d3cca05db.jpg" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37fd0fc15ff5e506a1cade4bb9a963dd.png" title="All My Demons Greeting Me as a Friend - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/bab022a4cc4a16f5bab01c6c95e6be8d.jpg" title="The Gods We Can Touch - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4e096ace46c5972db5a1418436fa312d.jpg" title="Machines of Our Disgrace (Definitive Edition) - Circle of Dust"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/138ef7f85ff467332c7c91411b6f6fcb.jpg" title="Infections Of A Different Kind (Step I) - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a6ee015fe1bc4d86cdb9b7c76778e7a6.jpg" title="Strange Trails - Lord Huron"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/985a9305c6d55203a6894678d5caf846.jpg" title="A Different Kind of Human (Step II) - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/700416badcde194ec1319d86b4d22b0a.jpg" title="Dopamine - BØRNS"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e7afa92b8a8e4ecc3e5e7b1a0ec18e6b.png" title="Arcane league of legends: season 2 (soundtrack from the animated series) - Arcane"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/01ab0b7f9f31e851680a38d26ae5ce51.jpg" title="Age of Aquarius - Perturbator"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c568cffcae3c9b243f6c4a7315bb6eb5.jpg" title="COSMOPOLIS - Miami Nights 1984"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/282c3bf58a2d2d9b99be592321d8760c.jpg" title="A Frame of Mind - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/52a7cfefbb075f71860ad604a282d1de.jpg" title="Owen - RØRE"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b32f0d69a9f0ee06d441a02daff65569.jpg" title="Skye - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/da5757d555424d7e1408e4855363da04.jpg" title="What Happened To The Heart? - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4b93f253a639282614d8e60af6b0f1fe.jpg" title="Bathing Beach - Novo Amor"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a2cc80f9f588dbd4cfe7e8a511e78f25.jpg" title="SYML - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0dfc45f8ca8d06375bf275acf6314d2c.jpg" title="Woodland - The Paper Kites"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a7403c29da998233a0ce507bf321862b.jpg" title="Somnia - Abbott"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/05164ba8eb074e355815dc6a5d800521.jpg" title="You Can’t Run From Yourself (From "Kaiju No. 8") - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c0c12ac9f2afc4ac0a8924b9ac1a6c72.jpg" title="Genesis - David A. Molina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1ef6aa0dae3d4bb8ffc15451099bb20a.jpg" title="Lungs (Deluxe Edition) - Florence + the Machine"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0605ac94ee875e46631c7d33fed07bb7.jpg" title="Ashley - RØRE"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63e9b188c786835f816db3924a4e9308.jpg" title="Winged Dreams - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3410c69b8e221724593c87cc25b972d7.jpg" title="Kingdom Two Crowns: Norse Lands Soundtrack (Extended) - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9c019286f3282154a84d5f149e2b938c.jpg" title="A6 - Lights"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1dbcea314e7b428d9aa223b68f4bdfb3.png" title="In a Time Lapse - Ludovico Einaudi"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9de1a08a9d1da269d71fcec90b7769b8.jpg" title="A Way Home - Omar Raafat"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ede631c6f72d4c038cba52ed39b28aeb.png" title="Je te laisserai des mots - Patrick Watson"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7a380e2889653a6178aa7f0c0f06648c.jpg" title="Goodbye (from the series Arcane League of Legends) - Ramsey"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/673870cbe7338b38997242ca0c815404.png" title="Basement beds - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b4972f03656762528c4e9e0b1e27198c.jpg" title="What Remains - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/819f2320ada234a224044b5d71f20b04.png" title="To Be Loved - Askjell"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/153cb088d5989154e6f90d78903f7450.jpg" title="Dance Fever - Florence + the Machine"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f5da82b742fb22616940e753b579579f.jpg" title="Long Lost - Lord Huron"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/16fdad2898a167de51428b9ccbd2317a.jpg" title="Hurry Up, We're Dreaming - M83"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37d7f424151142d987c12a477c1f5ec6.png" title="Oblivion (Original Motion Picture Soundtrack) - M83"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/681494b7afd7fbd7c744336b48707f14.jpg" title="Dark Corners and Alchemy - mehro"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c4d4c0a0eafab05190f78e6bf3c9c121.jpg" title="SKY ON FIRE - mehro"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8c61e9e5bfde31c0001c5e8966003b4e.jpg" title="In My Body - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0c03d883e3345b201087f61d1147ab8e.jpg" title="Mr. Sandman - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9623fa347e66c86a073e5c642d0198e6.jpg" title="Symmetry - SYML"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c5d1ec740991ed3e169b0722ae868402.jpg" title="Dear Wormwood - The Oh Hellos"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/60f5adb94eac599cc542c35c2d520091.jpg" title="Butterflies (feat. AURORA) - Tom Odell"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e81465325ebad4095da698eddfb8a9b6.png" title="Ethereal - txmy"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/031e3bd90c1744c2887c9de323d58093.png" title="The Golden Age - Woodkid"> </p>

          
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

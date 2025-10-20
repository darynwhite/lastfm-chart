# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/37fd0fc15ff5e506a1cade4bb9a963dd.png" title="All My Demons Greeting Me as a Friend - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a4b0ca89a071af2b87aa9e24cd7b9294.jpg" title="Viking War Trance - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8816946dc53e5400bda5c0bb1ee487a.jpg" title="Summer's Gone (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0c4b4d65203882c7b78bb629f38cb3c2.jpg" title="Horror Show (The Instrumentals) - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3410c69b8e221724593c87cc25b972d7.jpg" title="Kingdom Two Crowns: Norse Lands Soundtrack (Extended) - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a6ee015fe1bc4d86cdb9b7c76778e7a6.jpg" title="Strange Trails - Lord Huron"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a7403c29da998233a0ce507bf321862b.jpg" title="Somnia - Abbott"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/bab022a4cc4a16f5bab01c6c95e6be8d.jpg" title="The Gods We Can Touch - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/700416badcde194ec1319d86b4d22b0a.jpg" title="Dopamine - BØRNS"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/282c3bf58a2d2d9b99be592321d8760c.jpg" title="A Frame of Mind - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a4bc05c59aa286d875d031437df390f.jpg" title="The Beginning - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/52a7cfefbb075f71860ad604a282d1de.jpg" title="Owen - RØRE"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b32f0d69a9f0ee06d441a02daff65569.jpg" title="Skye - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/985a9305c6d55203a6894678d5caf846.jpg" title="A Different Kind of Human (Step II) - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/138ef7f85ff467332c7c91411b6f6fcb.jpg" title="Infections Of A Different Kind (Step I) - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0dfc45f8ca8d06375bf275acf6314d2c.jpg" title="Woodland - The Paper Kites"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c3ade32b7c45f80ef395ac7cfc2af0f1.jpg" title="Dreaming in Color - Judah Earl"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0605ac94ee875e46631c7d33fed07bb7.jpg" title="Ashley - RØRE"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b4972f03656762528c4e9e0b1e27198c.jpg" title="What Remains - Abilene"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e7afa92b8a8e4ecc3e5e7b1a0ec18e6b.png" title="Arcane league of legends: season 2 (soundtrack from the animated series) - Arcane"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3b34f6f1b339e9857fb276c318cb8b05.jpg" title="All My Demons Greeting Me As A Friend (Deluxe) - Aurora"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/488c1cd998e80dec58b42b3330f9bcaf.jpg" title="Of This Blood - Daridel"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e75c6fe7df0c4cefb230704cc1adb0ce.png" title="Plans - Death Cab for Cutie"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/47d6fc9e62e7ff1551e1b07dcca79e02.jpg" title="Berserkr - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cc9f07c6aa8ec63664ef1034502c7129.jpg" title="Fenrir - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d6e7200ad6360100997770fa3f3c08ae.jpg" title="Hugrheim - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5e132aafb8481f6fed27cfe7fe78576c.jpg" title="Ragnar's Last Raid - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a863bde41cc86fe11d54634b544342a9.jpg" title="Ragnarök - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/34cac131ba9b246d7d683850be9df63a.jpg" title="Völva's Chant - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a6b02765495e036a960baa612cc2875d.jpg" title="Yggdrasil's Renewal - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/650b9600b10b93394ddf84d1a17540d2.jpg" title="The Lion's Roar - First Aid Kit"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1ef6aa0dae3d4bb8ffc15451099bb20a.jpg" title="Lungs (Deluxe Edition) - Florence + the Machine"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/412666166e68b26c9aecb0f26dbe0a56.jpg" title="Wisen - Francis Wells"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8d20d80f6006b41329f03c449488f856.jpg" title="The Video Game Champion - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/96da77ffe81a20dee8eefe6c5c440977.jpg" title="Myrkr - Heldom"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8c77e9f509c4dd3bca8d3ac6b5344ce5.png" title="Evolve - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/dcd595c00fa7122ec3e8cfcbcca71933.jpg" title="Estes - Judah Earl"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5380d4e6ccf259c6b37053cf283739fe.jpg" title="Ghosts - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6707cc02ba6af379fdf7ddc8af7c64e2.jpg" title="Helvegen - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/390f8b073a6dc92bb39954341414ad78.jpg" title="Mechanical Bull (Expanded Edition) - Kings of Leon"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9c019286f3282154a84d5f149e2b938c.jpg" title="A6 - Lights"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ab5fafed3484610025812a001ca7a67e.png" title="So Tonight That I Might See - Mazzy Star"> </p>

          
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

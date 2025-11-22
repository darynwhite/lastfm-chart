# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e8ba53e4eb981b3dec8e72574248560f.jpg" title="Immortalized (Deluxe Edition) - Disturbed"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c9add86eac5aa56f7e36f916e4095380.gif" title="The Last Goodbye Tour Live - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f5270041983b7b838c2093f3042927d2.jpg" title="Echo Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a5c3187cd2e856a58bf5b31ac15092f.png" title="Playa La Manzanilla - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63ae49d15df3c1acd2a89ca2294cc039.jpg" title="Singing Sands - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7ade51bd6cd0175a05549e68a04bea54.jpg" title="The Last Goodbye (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e130b388ea12684a6ae966c5a9da7e52.jpg" title="Bridal Veil Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c90f4bd7d8218ab0f67de086e6b1063e.jpg" title="Jasper - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/fdcd8a3afa4a5584cc585c5ee6d06873.jpg" title="Allfather - Neon Odin"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/66a212ca52b0b2005837c8b8c549378b.jpg" title="Seulement L'amour - Dryve"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a191a2114b6d7ca2691cfdc678b896b.jpg" title="Mørketid - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8816946dc53e5400bda5c0bb1ee487a.jpg" title="Summer's Gone (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d7854d459270ee0f7494c5b0619b6706.jpg" title="Mirror Master - Young the Giant"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9e37f6c83d397a307b7fcf1460536781.jpg" title="Great Ocean Road - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0c4b4d65203882c7b78bb629f38cb3c2.jpg" title="Horror Show (The Instrumentals) - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ed5339e8710c8131e03fd0c81ad3c56f.jpg" title="Lake Wakatipu - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c8cc833e2085065d2b43cd0e5300076.jpg" title="Shuswap Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/874958bdf0bf4f9c3aa5e90f1b57426a.jpg" title="Waterton Lakes - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a4bc05c59aa286d875d031437df390f.jpg" title="The Beginning - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/842b56f7710a429efde801a5bc218fc6.jpg" title="Peak District - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/889c0c3371311a85f09e786b454af69d.jpg" title="Synthian (Deluxe Edition) - Nina"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/822c157beb5df04cd5ded872f92bdcc2.png" title="The Touch - yota"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/991a6471e0e3e9b68722dec8ea7673c0.jpg" title="After the Rain - Emilie Schiøtt"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/49f0383ffa35456ba42b45305084fc7f.jpg" title="The Gospel Truth (Bonus Track Version) - Ida Sand"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/20e56a3c3b32fcf6d263947312f8e30d.jpg" title="Projections - Rogue VHS"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d6e7200ad6360100997770fa3f3c08ae.jpg" title="Hugrheim - Eihwar"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2758821749e2dfc4519c33022609562.jpg" title="Carry My Heart - Indra Rios-Moore"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ffc951db119a47d8a046b0d574c1894b.jpg" title="Heartland - Indra Rios-Moore"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9c019286f3282154a84d5f149e2b938c.jpg" title="A6 - Lights"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b2e51674629feb5f41afe26c2a64b575.jpg" title=""Eine kleine Nachtmusik" - Mozart for Winter - Wolfgang Amadeus Mozart"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/58cf91087703903a5372513eba5e1ace.jpg" title="MOZART: Piano Concertos Nos. 23 and 24 - Wolfgang Amadeus Mozart"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f25ea79c455d2db06983f3b044cfd632.jpg" title="Í Ævir - Elinborg"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a438b61f486793660c1537c005ac5ab2.jpg" title="V.O.L.T - Emil Rottmayer"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/99947e68c0f44af76f1559af8734afd0.jpg" title="Gunship - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7ec7823d81129386d6132e05213a16ec.jpg" title="Do You Hear Me? - Ida Sand"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1cc2a347b477292757f5a6f9f1544e0b.jpg" title="My Soul Kitchen - Ida Sand"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ac9bb509e20ba59dd1e83f5833003eb3.jpg" title="Freedom Road - Indra Rios-Moore"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/749d7aec5df5e4456d21a59554ec99c1.jpg" title="Use Me - Vanessa Fernandez"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/dccadc589e8e7f9bebb277b63b840d26.jpg" title="From Afar - Víkingur Ólafsson"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9df88bfe6a60e90533a9ce876c3fccc5.jpg" title="Infinity - W O L F C L U B"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6b43f54f18c35a541c11eb71e3d6fe36.jpg" title="Mozart: Piano Sonatas K280, K281, K310 & K333 - Wolfgang Amadeus Mozart"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d1f8af1d6b8f6f5243886df8556f82e4.jpg" title="Memoria - A.L.I.S.O.N"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/66a56a70b0b5d8f19408b4a36b642c3b.jpg" title="Empty Streets - After Dark"> </p>

          
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

# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/f5270041983b7b838c2093f3042927d2.jpg" title="Echo Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6d8092b0c5c550eced96c7593ec9d151.jpg" title="Kaskade Christmas Deluxe - Kaskade"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c90f4bd7d8218ab0f67de086e6b1063e.jpg" title="Jasper - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d40551abbc08130b690acc64e51c6607.png" title="Christmas (Deluxe 10th Anniversary Edition) - Michael Bublé"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/63ae49d15df3c1acd2a89ca2294cc039.jpg" title="Singing Sands - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/33483a740afc298be82eb8e799750f4b.jpg" title="A Pentatonix Christmas Deluxe - Pentatonix"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ffc4a6e9d0ac31f4aa31e4812f925103.jpg" title="The Songs the Season Brings, Vols. 1-4 - Beta Radio"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3da8f5454f35a9cae73175113a23484f.jpg" title="Bing At Christmas - Bing Crosby"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/715bd82463f74ae2bf5aec55d3bfddcc.jpg" title="When My Heart Finds Christmas - Harry Connick, Jr."> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3ee4ff8a44b547d28f3020ff8d2d31d8.jpg" title="What A Night! A Christmas Album - Harry Connick, Jr."> <img src="https://lastfm.freetls.fastly.net/i/u/34s/72e0f8cd5fc2df808c6b478c4797880e.jpg" title="Snow Waltz - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/16e39fd39917aa2f93d8ad09530a07fc.jpg" title="DRIVE - Tiësto"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a5c3187cd2e856a58bf5b31ac15092f.png" title="Playa La Manzanilla - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/864eff2973cf26721a04df6507c1ab67.jpg" title="A Charlie Brown Christmas [2012 Remastered & Expanded Edition] - Vince Guaraldi Trio"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0ea1f680b8c9884266c56f37340b1b7c.jpg" title="I Dream Of Christmas (Extended) - Norah Jones"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1a191a2114b6d7ca2691cfdc678b896b.jpg" title="Mørketid - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/e130b388ea12684a6ae966c5a9da7e52.jpg" title="Bridal Veil Falls - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ed5339e8710c8131e03fd0c81ad3c56f.jpg" title="Lake Wakatipu - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d4ae381d45f9fc9ac7e687e33178a93b.jpg" title="In Return (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/08299b0209da9912f380404686840e58.jpg" title="A Legendary Christmas - John Legend"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/26dad4b17fd36ec94b6bb154eec17e8f.jpg" title="Warmer In The Winter (Deluxe Edition) - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/95716b6e75284516307f57088aa41cf5.jpg" title="Duality - Lindsey Stirling"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ca7dcc5389a5316c0be959ae146cedaf.jpg" title="Comfort In Chaos - John Summit"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a8816946dc53e5400bda5c0bb1ee487a.jpg" title="Summer's Gone (10 Year Anniversary Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9e37f6c83d397a307b7fcf1460536781.jpg" title="Great Ocean Road - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cc8e6c6cf1eaa64efd7f8f2d542b76cf.png" title="A Ben Rector Christmas - Ben Rector"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7c8cc833e2085065d2b43cd0e5300076.jpg" title="Shuswap Lake - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/874958bdf0bf4f9c3aa5e90f1b57426a.jpg" title="Waterton Lakes - Little Symphony"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7ade51bd6cd0175a05549e68a04bea54.jpg" title="The Last Goodbye (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3a732f7dd6ddc9f50e84c97875b6192c.jpg" title="A Moment Apart (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/50ca1f960fe2e4d1af069c3b8fcb25ff.jpg" title="Spotify Singles - Christmas - Jon Batiste"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/aef76153fac847de492126d416b1647e.png" title="The London Sessions - Tiësto"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/cfb32acc44fd2a22965e8ed12b4e0dda.jpg" title="FABLES, ACT I - Ekaterina Shelehova"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/99b44a4bf17642c7326e3480e5ce16f4.jpg" title="Human (feat. Echoes) - John Summit"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c6f04f91f0bdab652da998c243ee8077.jpg" title="Hollow (feat. Bonn) - MORTEN"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/352486d309624c360803f9f346c0133c.png" title="Miss You - Nu Aspect"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d194e534538e87d66bf09df9e8abe230.jpg" title="Overdrive (feat. Norma Jean Martine) - Ofenbach"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0744db3455a5c4d76615d19a9ab16658.png" title="Finally - Swedish House Mafia"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/97a1014867d48d5b01cc90d19d6273d2.jpg" title="Lioness - Swedish House Mafia"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c252c625f0ec6784ed170ed0a5862328.png" title="Paradise Again - Swedish House Mafia"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2de03bdd3a661dd8ad338ee07d1e6b3c.jpg" title="Ray of Solar - Swedish House Mafia"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/717e255b6fcc47e3845180d1cb249092.png" title="Tracks in the Snow - The Civil Wars"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d5308b9c9b2866411d8f3066aa358861.png" title="Bring Me to Life - Tiësto"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/651fec296a40ed1ff57cedda2ae18fa6.png" title="Drifting - Tiësto"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ac73c8a25448081f7513b5be5b50179e.jpg" title="VHS RAVE - Tiësto"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/2692ee69f4af046caf7b2b6f2912cd1b.jpg" title="Mwaki (Major Lazer Remix) - zerb"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/86c68338f464a97424b5b8e175542974.jpg" title="Thank You (Not So Bad) - Dimitri Vegas & Like Mike"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/55c35e22b50d521c4767d56f8033e958.jpg" title="You & Me (Rivo Remix) - Disclosure"> </p>

          
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

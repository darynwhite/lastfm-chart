# last.fm weekly chart

![banner](banner.png)

## 🤖 About this repo
This is a fork and rebuild of [melipass/lastfm-to-markdown](https://github.com/melipass/lastfm-to-markdown) focused on refactoring the Python for readability and maintainability. Also adding new features with time so this can build any weekly/monthly/etc. report that the Last.FM API offers.

## 🎵 Example output, automatically updated every day
<!-- lastfm -->
<p align="center"><img src="https://lastfm.freetls.fastly.net/i/u/34s/b16a343e68aefeaaf94b6324a07cb6e1.jpg" title="Slumberkins: Season 1, Vol. 1 (Apple Original Series Soundtrack) - Ingrid Michaelson"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3a732f7dd6ddc9f50e84c97875b6192c.jpg" title="A Moment Apart (Deluxe Edition) - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/3f4af1304c37e86a5329a169352d7820.png" title="Syndicate - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/85ee26d039d6495895f5e952d4df35d9.jpg" title="Summer's Gone - ODESZA"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d8c69121d829c66b65e6003a5d4415f8.jpg" title="Unicorn - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8c77e9f509c4dd3bca8d3ac6b5344ce5.png" title="Evolve - Imagine Dragons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/108217d96c01fa54d7e236bfd76895ac.png" title="The Line - Kalandra"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c8abf53ac459b88777f4e3d464250559.jpg" title="Our Time - Single - AFROJACK, Martin Garrix, David Guetta & Amél"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5526cfe62a8b32bc1cbcde8460e82784.jpg" title="Heroes - The Midnight"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8d1cbb90696dc73e46cea02feb36d3ba.jpg" title="Awake (Deluxe Version) - Tycho"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c344aff60cd752191f07e9b5c7fe2eb1.png" title="Electric Love (Oliver Remix) - Single - BØRNS"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/06030e2f059397b79fe2f4f37df70fb9.jpg" title="Breathe (20th Anniversary) - EP - Télépopmusik"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/950ca20d9253f8aad15a129884dadc97.jpg" title="Kala - Trevor Hall"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4d6a333808f4a1e7cd69d30ed457248e.jpg" title="A Day Without Rain - Enya"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/f9ed6857e7f4421790bc0948c758227b.jpg" title="Nickel Creek - Nickel Creek"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/eaed804aeb32b0510867d3fea540a4ee.jpg" title="Sigh No More - Mumford & Sons"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/612dcc8aeb13634b5fadee3f47f9abb0.jpg" title="Viva la Vida - Coldplay"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/56f4a3d4bbac40a8a49520f21d50b036.png" title="Feels Like Home - Norah Jones"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/6ccc66e1b7778e98304e87df8c0aedc7.jpg" title="Better Man - Single - Ryan Innes"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9b4a66927b8433e1f922fcd919965922.png" title="Girls and Boys - Ingrid Michaelson"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/a4820a28aaecbafcad028091a9597d78.png" title="Till the Sun Turns Black - Ray LaMontagne"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/ddb2b1df25524a798d2cf88ceb83ff32.png" title="Big Whiskey & The Groogrux King - Dave Matthews Band"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/1ee0db2cdbc7166836a17421be2197a8.jpg" title="Plans (Deluxe) - Death Cab for Cutie"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/9ec86c8bd6055b646d25e58457a971a3.jpg" title="Continuum - John Mayer"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/d241c204d07ae6a8881b80ee0fcd0e84.png" title="Come Away with Me - Norah Jones"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/5204b80b65b405e8bf1359475e941b3d.jpg" title="Trouble - Ray LaMontagne"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/0c47fb3b2f2b486b86ab09c5d4557445.png" title="Surfacing - Sarah McLachlan"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/b6c46db61212e9e9e57f3633cf588eae.png" title="Final Straw - Snow Patrol"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c15892b07145e2beb960c264c6ad9974.jpg" title="Give Up - The Postal Service"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/00d1be31d831a83047e4d4785066c040.png" title="Coco - Colbie Caillat"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/7f0781b7b4d96217e6cc0c65032a391b.jpg" title="Paint the Sky With Stars - The Best of Enya - Enya"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/c2402f6c2f3b47ab134051c80ed6f480.jpg" title="Dark All Day - Gunship"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/66732b3e2524905099fa087a9bce0f4d.png" title="Fumbling Towards Ecstasy - Sarah McLachlan"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/4a8ecdd4507fdf5ad3fc82e0a228a1d0.png" title="A Hundred Million Suns - Snow Patrol"> <img src="https://lastfm.freetls.fastly.net/i/u/34s/8e61d4bc73ef4aa1bab17883e5491553.png" title="Up to Now - Snow Patrol"> </p>

          
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

import requests
import os
import sys
import logging

# Setup logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def lastfm_request(payload) -> requests.Response:
    "Handle the Last.fm API request"
    logger.info(
        f"Making Last.fm API request with method: {payload.get('method', 'unknown')}"
    )
    logger.debug(f"Full payload: {payload}")

    headers = {"user-agent": os.getenv("LASTFM_USER")}
    if api_key := os.getenv("LASTFM_API_KEY"):
        payload["api_key"] = api_key
        logger.debug("API key found and added to payload")
    else:
        logger.error("LASTFM_API_KEY not set")
        raise ValueError("LASTFM_API_KEY not set")

    if api_user := os.getenv("LASTFM_USER"):
        payload["user"] = api_user
        logger.debug(f"Using Last.fm user: {api_user}")
    else:
        logger.error("LASTFM_USER not set")
        raise ValueError("LASTFM_USER not set")

    payload["format"] = "json"

    with requests.Session() as session:
        session.headers.update(headers)
        session.params.update(payload)
        logger.debug(f"Making GET request to: https://ws.audioscrobbler.com/2.0/")
        response = session.get("https://ws.audioscrobbler.com/2.0/")

        if response.status_code != 200:
            logger.error(f"Request failed with status code {response.status_code}")
            raise requests.RequestException(
                f"Request failed with status code {response.status_code}"
            )

        try:
            response.json()
            logger.debug("Response successfully parsed as JSON")
        except ValueError:
            logger.error("Response is not valid JSON")
            raise ValueError("Response is not valid JSON")

    logger.info("API request completed successfully")
    return response


def get_weekly_album_chart() -> dict:
    "Get the weekly album chart from Last.fm"
    logger.info("Fetching weekly album chart")
    payload = {"method": "user.getWeeklyAlbumChart"}
    albums = lastfm_request(payload).json()["weeklyalbumchart"]["album"]
    artist_and_album = {}
    max_albums = int(os.getenv("IMAGE_COUNT")) if os.getenv("IMAGE_COUNT") else 10
    logger.info(f"Fetching top {max_albums} albums")

    for album in albums:
        rank = album["@attr"]["rank"]
        if int(rank) > max_albums:
            continue
        artist_and_album[rank] = {
            "artist": album["artist"]["#text"],
            "album": album["name"],
        }
        logger.debug(
            f"Added album: {album['name']} by {album['artist']['#text']} (Rank: {rank})"
        )

    logger.info(f"Retrieved {len(artist_and_album)} albums")
    return artist_and_album


def get_album_covers(artist_and_album: dict) -> dict:
    "Get the album covers for the albums in the artist_and_album dictionary"
    logger.info("Fetching album covers")
    img_size = os.getenv("IMAGE_SIZE") if os.getenv("IMAGE_SIZE") else "medium"
    logger.debug(f"Using image size: {img_size}")

    for album in artist_and_album:
        current_album = artist_and_album[album]
        logger.debug(
            f"Fetching cover for {current_album['album']} by {current_album['artist']}"
        )

        payload = {
            "method": "album.getInfo",
            "artist": current_album["artist"],
            "album": current_album["album"],
        }

        request_response = lastfm_request(payload).json()
        for image in request_response["album"]["image"]:
            if image["size"] == img_size:
                link_to_image = image["#text"]
                break

        link_to_album = request_response["album"]["url"]
        if image != "":
            current_album["image"] = link_to_image
            current_album["link"] = link_to_album
            logger.debug(f"Found cover image: {link_to_image}")
        else:
            logger.warning(f"No cover image found for {current_album['album']}")

    logger.info("Finished fetching album covers")
    return artist_and_album


def update_readme(albums: dict) -> None:
    "Update the README.md file with the album covers"
    logger.info("Starting README.md update")

    if incl_link := os.getenv("INCLUDE_LINK"):
        if incl_link.lower() == "true":
            incl_link = True
        elif incl_link.lower() == "false":
            incl_link = False
        else:
            logger.error("Invalid INCLUDE_LINK value")
            raise ValueError("INCLUDE_LINK must be 'true' or 'false'")
    else:
        incl_link = False
    logger.debug(f"Include links: {incl_link}")

    with open("README.md", "r", encoding="utf-8") as file:
        readme = file.readlines()
    lastfm_line_index = readme.index("<!-- lastfm -->\n") + 1
    logger.debug(f"Found lastfm marker at line {lastfm_line_index}")

    lastfm_line = '<p align="center">'
    with requests.Session() as session:
        session.headers.update({"user-agent": os.getenv("LASTFM_USER")})
        session.params.update({"api_key": os.getenv("LASTFM_API_KEY")})

        for album in albums.values():
            logger.debug(f"Processing album: {album['album']}")
            if album["image"] and session.get(album["image"]).status_code == 200:
                if incl_link:
                    lastfm_line += f'<a href="{album['link']}"><img src="{album['image']}" title="{album['album']} - {album['artist']}"></a> '
                else:
                    lastfm_line += f'<img src="{album['image']}" title="{album['album']} - {album['artist']}"> '
                logger.debug(f"Added album to README: {album['album']}")
            else:
                logger.warning(
                    f"Skipping album due to missing or broken image: {album['album']}"
                )

    if readme[lastfm_line_index] == lastfm_line:
        logger.info("README.md is already up to date")
        sys.exit(0)
    else:
        lastfm_line = lastfm_line + "</p>\n"
        readme[lastfm_line_index] = lastfm_line
        logger.info("Updating README.md with new content")

    with open("README.md", "w", encoding="utf-8") as file:
        file.writelines(readme)
    logger.info("README.md update completed")


if __name__ == "__main__":
    logger.info("Starting Last.fm weekly chart update")

    if not os.path.exists("README.md"):
        logger.error("README.md file not found")
        raise FileNotFoundError("README.md file not found")

    if not os.getenv("LASTFM_API_KEY"):
        logger.error("LASTFM_API_KEY not set")
        raise ValueError("LASTFM_API_KEY not set")

    if not os.getenv("LASTFM_USER"):
        logger.error("LASTFM_USER not set")
        raise ValueError("LASTFM_USER not set")

    logger.debug("All required files and environment variables found")
    update_readme(get_album_covers(get_weekly_album_chart()))
    logger.info("Script completed successfully")

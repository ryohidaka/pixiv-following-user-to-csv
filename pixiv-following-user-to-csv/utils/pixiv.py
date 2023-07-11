import time
from utils.config import REFRESH_TOKEN, USER_ID
from pixivpy3 import AppPixivAPI


def init_api(self) -> AppPixivAPI:
    """
    Initialize the API.

    Returns:
        AppPixivAPI: The API client.
    """

    self.logger.info("[Start] Initialize the API client.")

    refresh_token = REFRESH_TOKEN

    api = AppPixivAPI()
    api.auth(refresh_token=refresh_token)
    time.sleep(2)

    self.logger.info("[End] Initialize the API client.")

    return api


def get_following_users(self):
    """
    Get the list of users who the target user is following.
    """
    api = self.api
    logger = self.logger
    logger.info("[Start] Get the list of users who the target user is following.")

    # Define a list of users.
    users = []

    # Get the list of users who the target user is following.
    res = self.api.user_following(USER_ID, restrict=self.restrict)
    time.sleep(5)

    while True:
        try:
            user_previews = res.user_previews

            for user_raw in user_previews:
                # Create a user object.
                user = user_raw.user
                latest_date = get_latest_date(user_raw.illusts)

                user_id = user.id

                user_data = {
                    "id": user_id,
                    "account": user.account,
                    "name": user.name,
                    "latest_date": latest_date,
                }

                users.append(user_data)

            next_url = res.next_url
            logger.info(f"Next URL: {next_url}")

            if next_url:
                next_qs = api.parse_qs(res.next_url)
                time.sleep(2)
                res = api.user_following(**next_qs)
                time.sleep(2)
            else:
                break

        except Exception as e:
            logger.error("Failed to get the user.:", str(e))
            break

    logger.info("[End] Get the list of users who the target user is following.")

    return users


def get_latest_date(illusts) -> str:
    """
    Get the latest post date of the user.

    Parameters
    ----------
    illusts: Any[]
          The list of user's illustrations.
    """

    # Check if there are illustrations.
    has_illusts = len(illusts) > 0

    if has_illusts:
        return illusts[0].create_date

    return None

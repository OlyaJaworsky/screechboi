def authorize(reddit, scopes=["identity", "privatemessages"]):
    """
    Creates a link for you to get an access code that can be used for the bot
    to access your account on your behalf.
    """

    print("Go to the following URL:")
    print(reddit.auth.url(scopes, "...", "permanent"))


def exchange_code(reddit, code):
    """
    Exchanges a temporary code received from "authorize" for a reusable refresh
    token.
    """

    print("Save the 'refresh_token' from the following:")
    print(reddit.auth.authorize(code))

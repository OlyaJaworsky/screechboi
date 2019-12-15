# Authorize creates a link for you to get an access code that can be used 
# for the bot to access your account on your behalf.
def authorize(reddit, scopes=["identity", "privatemessages"]):
    print("Go to the following URL:")
    print(reddit.auth.url(scopes, '...', 'permanent'))

def exchange_code(reddit, code):
    print("Save the 'refresh_token' from the following:")
    print(reddit.auth.authorize(code))
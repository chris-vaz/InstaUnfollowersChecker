import instaloader

def get_unfollowers(username, password):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    # Log in to Instagram
    L.login(username, password)

    # Get profile
    profile = instaloader.Profile.from_username(L.context, username)

    # Get the set of followees and followers
    followees = set([followee.username for followee in profile.get_followees()])
    followers = set([follower.username for follower in profile.get_followers()])

    # Calculate the difference
    not_following_back = followees - followers

    return not_following_back

if __name__ == "__main__":
    # Replace these with your Instagram credentials
    username = "Enter your Instagram Account here"
    password = "Enter your Instagram Password here"

    not_following_back = get_unfollowers(username, password)

    print("People you follow but who don't follow you back:")
    for user in not_following_back:
        print(user)

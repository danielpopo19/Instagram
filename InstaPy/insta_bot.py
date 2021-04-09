"""
This template is written by @Nuzzo235
What does this quickstart script aim to do?
- This script is targeting followers of similar accounts and influencers.
- This is my starting point for a conservative approach: Interact with the
audience of influencers in your niche with the help of 'Target-Lists' and
'randomization'.
NOTES:
- For the ease of use most of the relevant data is retrieved in the upper part.
"""

import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'D3liciousDining'
insta_password = '4567qweRR!'

# restriction data
dont_likes = ['#exactmatch', '[startswith', ']endswith', 'broadmatch']
ignore_users = ['user1', 'user2', 'user3']

""" Prevent commenting on and unfollowing your good friends (the images will 
still be liked)...
"""
friends = ['dpolinski', 'isabelledelcea', 'bye___alicia']

""" Prevent posts that contain...
"""
ignore_list = []

# TARGET data
""" Set similar accounts and influencers from your niche to target...
"""
targets = ['dcfoodporn', 'thenaughtyfork', 'buzzfeedtasty','food52']

""" Skip all business accounts, except from list given...
"""
target_business_categories = ['dcfoodporn', 'thenaughtyfork', 'buzzfeedtasty','food52']

# COMMENT data
comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'This is so delicious :yum: @{}',
        ':raised_hands: Yes!',
        'Im hungry!!  @{} :yum:']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  disable_image_load=False,
                  multi_logs=True)

# let's go! :>
with smart_run(session):
    # HEY HO LETS GO
    # general settings
    session.set_quota_supervisor(enabled=True,
                             sleep_after=["server_calls_h"],
                             sleepyhead=True,
                             stochastic_flow=True,
                             notify_me=True,
                             peak_likes_hourly=106, 
                             peak_likes_daily=585,
                             peak_follows_hourly=48,
                             peak_follows_daily=None,
                             peak_unfollows_hourly=35,
                             peak_unfollows_daily=403,
                             peak_server_calls_hourly=None,
                             peak_server_calls_daily=4700)

    session.set_dont_include(friends)                            # Defines which accounts should not be unfollowed
    session.set_mandatory_language(enabled=True, character_set=['LATIN'])
    session.set_dont_like(dont_likes)                            # Changes the possible restriction tags, if one of this words is in the description, the image won't be liked but user still might be unfollowed       
    session.set_ignore_if_contains(ignore_list)                  # Ignores the don't likes if the description contains one of the given words
    session.set_ignore_users(ignore_users)                       # Changes the possible restriction to users, if a user who posts is one of these, the image won't be liked
    session.set_simulation(enabled=True)                         # Sets aside simulation parameters
    session.set_relationship_bounds(enabled=True,                # Sets the potency ratio and limits to the provide an efficient activity between the targeted masses
                                    potency_ratio=-1.05,
                                    delimit_by_numbers=True,
                                    max_followers=1000,
                                    max_following=7000,
                                    min_followers=100,
                                    min_following=100,
                                    min_posts=10)

    session.set_skip_users(skip_private=False,                   # Dont_skip_business_categories = [] Setted by default in init
                           skip_no_profile_pic=True,
                           skip_business=True,
                           dont_skip_business_categories=[
                               target_business_categories])

    session.set_user_interact(amount=3, randomize=True, percentage=80,   #Define if posts of given user should be interacted
                              media='Photo')
    session.set_do_like(enabled=True, percentage=90)                     # 90% of viewed pages will be liked
    session.set_do_comment(enabled=True, percentage=15)                  # 15% of viewed pages will be commented
    session.set_comments(comments)                                       # load the comment list for photos only
    session.set_do_follow(enabled=True, percentage=20, times=1)          # follows ~ 10% of the users from the images, times=1 only follows a user once (if unfollowed again))
    session.set_dont_like(
        ['dick', 'squirt', 'gay', 'homo', '#fit', '#fitfam', '#fittips',
         '#abs', '#kids', '#children', '#child',
         '[nazi', 'promoter'
                  'jew', 'judaism', '[muslim', '[islam', 'bangladesh',
         '[hijab', '[niqab', '[farright', '[rightwing',
         '#conservative', 'death', 'racist'])
    session.set_action_delays(enabled=True,
                             like=3,
                             comment=5,
                             follow=4.17,
                             unfollow=28,
                             story=10)
    print("finished all general settings")
    # activities

    # FOLLOW+INTERACTION on TARGETED accounts
    """ Select users form a list of a predefined targets...
    """
    number = random.randint(1,4)
    random_targets = targets

    print("Number: " + str(number))

    for x in range(len(targets)):
        print(targets[x])

    if len(targets) <= number:
        print("random_targets = targets")
        random_targets = targets

    else:
        random_targets = random.sample(targets, number)

    for x in range(len(random_targets)):
        print(random_targets[x])

    """ Interact with the chosen targets...
    """
    session.follow_user_followers(random_targets,                         # Follow the `Followers` of given users 
                                  amount=random.randint(50, 100),         # finds the last people to have followed them and then follows each of them (FIGURE OUT)
                                  randomize=True, sleep_delay=600,
                                  interact=True)
    print("follow_user_follower finished************")
    # UNFOLLOW activity
    """ Unfollow nonfollowers after one day...
    """
    session.unfollow_users(amount=random.randint(75, 100),               # Unfollows (default) 10 users from your following list
                           nonFollowers=True,                            # Unfollow the users who do not follow you back
                           style="FIFO",
                           unfollow_after=24 * 60 * 60, sleep_delay=600)

    """ Unfollow all users followed by InstaPy after one week to keep the 
    following-level clean...
    """
    print("unfollow user finished************")
    session.unfollow_users(amount=random.randint(75, 100),
                           allFollowing=True,
                           style="FIFO",
                           unfollow_after=168 * 60 * 60, sleep_delay=600)

    print("unfollow user finished************")

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='food', engagement_mode='no_comments')

"""
Have fun while optimizing for your purposes, Nuzzo
"""
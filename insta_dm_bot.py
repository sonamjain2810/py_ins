from instabot import Bot

my_bot = Bot()

#login account

my_bot.login(username="rikhil.jain",password="")

#Method1

#DM the followers of the user

followers_ids = my_bot.get_user_followers("")

for each_follower in followers_ids:
    my_bot.follow(each_follower)
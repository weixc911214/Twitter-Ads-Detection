# Twitter-Ads-Detection


## Preliminary Results

For now, we develop two kinds of automation tools to test the input and output of the twitter.

### AccountManager: Mocking Twitter User Behaviors

For the Input part, we developped an **AccountManager** to mock the behaviors of normal Twitter users. 

AccountManager mantains a list of pre-created Twitter accounts. With the defined user baviors and keyword sets, each account mock the normal user behaviors like posting, retweeting and following other accounts. Each behavior records are stored into database for further research.

We specifiy different kind of behaviors like following:

1. Post tweets contains keywords or @ specific term(@another_user)
2. Post tweets with @ specific brands
3. search history contains keywords or for a specific term(#hashtag)
4. post tweets with specific location informations
5. Retweet, star or reply brand-related tweets
6. Following specific brand twitter account
7. Send messages from one user to another containing keywords
8. Click promotion tweets to give positive feedbacks

According to the part above, many user bahaviors rely on the diversity of keyword datasets.

### PromotionMonitor: Getting Twitter Promotion Informations

The ads on Twitter is based on different levels of promotions:

1. Promoted Tweets

    Promoted Tweets allows you to highlight a particular status update to get more exposure for it. You will have Promoted Tweets throughout Twitter included on your profile itself in expanded view…

    Or at the top of search results for particular keywords…


2. Promoted Trends

    Promoted Trends are topics and hashtags that are moved to the top of the Trending Topics list. You can see them when you visit your Twitter homepage and look under the Trends section.

    Just like regular trending topics, people can incorporate them into their tweets and view a page following anyone who has posted an update using the particular keyword or hashtag. At the top of the tweets, you will likely see a promoted tweet from the account that created the trend.

3. Promoted Accounts

    Promoted Accounts allows you to promote your account as one to follow. An example is when you log in to your Twitter account and go to your main dashboard. To the left of your Twitter stream, beneath your Twitter statistics, is a box showing suggested users to follow based on your interests. If an advertiser has related keywords in its profile and is targeting an audience in your location, you will see it as a promoted account in this section.

    Another place Promoted Accounts appear is in search results for particular keywords if you click on People.

What PromotionMonitor does is that, we do the snapshot of each Twitter accounts daily and extract the promotion parts of each users' timeline. The tweets, timestamp and other information are stored into database for now.

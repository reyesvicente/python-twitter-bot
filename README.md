# python-twitter-bot
A Twitter Bot that tweets jokes from the icanhazdadjoke 

*Cover photo by https://icons8.com/*
{% soundcloud https://soundcloud.com/mrmindful/mindful-vibes-episode-10-jazz-hop-mix %}

*The purpose of this program was to automate the jokes I have been posting on my facebook account thru twitter. Although I haven't figured out AWS Lambda yet, I believe I'll get there in no time.* 

This program is run thru IDLE, which, according to [Wikipedia](https://g.co/kgs/iQ9hDM), is bundled with the Mac OS X Python since 1.5.2b1.

We start learning with "[Getting started with the Twitter API](https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api)", then we progress to calling the [icanhazdadjoke api](https://icanhazdadjoke.com) throughout the article.

In this program, I learned 4 things: 

* How to apply & create the Twitter API keys used in this application

* How to use Twython to send tweets using Python

* How to call an API &

* How to search for the right questions on a search engine to get the right answer

#### First, we apply for a Twitter Developer account with the help of [this](https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api/3). Upon completing the application, we will receive an email confirmation from Twitter to confirm our email address. Then we wait for our application to be approved. We can check the status at [developer.twitter.com](https://developer.twitter.com).

#### After getting approved for the developer account, we login to [developer.twitter.com](https://developer.twitter.com) to get our application registered to get our API Keys.
![](https://thepracticaldev.s3.amazonaws.com/i/50a39k8s2a11qz2l82zt.png)

![](https://thepracticaldev.s3.amazonaws.com/i/8utkkl7igx2i16j7oo4v.png)

![](https://thepracticaldev.s3.amazonaws.com/i/fjiyzahgleta6a9xifu2.png)

![](https://thepracticaldev.s3.amazonaws.com/i/3wtexpx58ro4s0np4o7p.png)

![](https://thepracticaldev.s3.amazonaws.com/i/gywdbkispkhw02925slu.png)

##### Review the developer terms and click create.

![](https://thepracticaldev.s3.amazonaws.com/i/4kltiwvxhgfhqbng4u2m.png)

#### Click on keys and tokens to view your keys and access tokens then click create under Access token & access token secret.

![](https://thepracticaldev.s3.amazonaws.com/i/z0inajk61abjlnm6g22x.png)

![](https://thepracticaldev.s3.amazonaws.com/i/q8f5xd17798lnuk7qwgn.png)


### **Coding the program and sending our first tweet**

#### Create an auth.py file on IDLE and paste your keys inside then hit save

<pre>consumer_key = 'ENTER_YOUR_CONSUMER_KEY'
consumer_secret = 'ENTER_YOUR_CONSUMER_SECRET'
access_token = 'ENTER_YOUR_ACCESS_TOKEN'
access_token_secret = 'ENTER_YOUR_ACCESS_TOKEN'</pre>

#### Create another new file and import Twython from the twython module

<pre>from Twython import Twython</pre>

#### Also import the variables from auth.py

<pre>from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)</pre>

save this as twitter.py

#### Create a connection with the Twitter API using Twython 

<pre>twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)</pre>

#### We'll use the <pre>update_status()</pre> function of Twitter's API to send a tweet

<pre>message = "Hello world!"
twitter.update_status(status=message)
print('Tweeted: ' % message)</pre>

#### Now we run the module by using F5 or from tweet.py -> Run -> Run Module. 

View from the mobile : 
![](https://thepracticaldev.s3.amazonaws.com/i/59xvt797h0kc2jmi5u0m.jpg)

View from the CLI : 
![](https://thepracticaldev.s3.amazonaws.com/i/3sywi3aacy03uejeuknx.png)

View from the browser :
![](https://thepracticaldev.s3.amazonaws.com/i/zlk04q3jla5z79y0ph57.png)


### **Calling the icanhazdadjoke API**

Fortunately, *icanhazdadjoke* can be called without an authentication by the **GET** method. Read through their docs [here](https://icanhazdadjoke.com/api) if you want to learn more

<pre>url = 'https://icanhazdadjoke.com/'
headers = {'Accept': 'application/json'}
joke_msg = requests.get(url, headers=headers).json().get('joke')
print(joke_msg)</pre>

The response is : :raised_hands::raised_hands::raised_hands:
![](https://thepracticaldev.s3.amazonaws.com/i/oxa9xnkvlpdostt15pw7.png)

### Now, we play around the codes.

#### Designing the Code Structure

We want the output of the *icanhazdadjoke* tweeted on our twitter account so we use the **url** variable to call their API. I start with the output, going back to calling the API.

**We end up with this code :**

<pre>url = 'https://icanhazdadjoke.com/'
headers = {'Accept': 'application/json'}
joke_msg = requests.get(url, headers=headers).json().get('joke')
twitter.update_status(status=joke_msg)
print("Tweeted: " + joke_msg)</pre>

The output is : :scream::scream::scream:

CLI : 
![](https://thepracticaldev.s3.amazonaws.com/i/yj1bp6f5yzx0oms8zghz.png)

Browser : 
![](https://thepracticaldev.s3.amazonaws.com/i/qnb0cxt3ghrq25zhxxnw.png)

Mobile : 
![](https://thepracticaldev.s3.amazonaws.com/i/9abw67tyoquum7e2saw2.jpg)

:raised_hands::scream::raised_hands::scream::raised_hands:

**Next step here would be to figure out AWS Lambda to automate the tweets twice a day and forget about it.**

class PostCraiglistHousingOnSlack:

    def sendMessages(self, msg):
        self.smg = msg
        from slackclient import SlackClient
        SLACK_TOKEN = "xoxb-513638154290-513475702356-QOHxjz7toCmoeXRypUiQpBs4"
        SLACK_CHANNEL = "#learning"
        sc = SlackClient(SLACK_TOKEN)
        sc.api_call(
            "chat.postMessage", channel=SLACK_CHANNEL, text=msg,
            username='pybot', icon_emoji=':taxi:'
        )



    def getMessages(self):
        import time
        from slackclient import SlackClient
        token = "xoxb-513638154290-513475702356-QOHxjz7toCmoeXRypUiQpBs4"# found at https://api.slack.com/web#authentication
        sc = SlackClient(token)
        if sc.rtm_connect():
                while True:
                        read_response = sc.rtm_read()
                        if len(read_response) != 0 or read_response !=[]:
                            json_reonse = read_response
                            if 'text' in json_reonse[0]:
                                print("valid text")
                                print(json_reonse[0]['text'])
                                reponse = json_reonse[0]['text']

                                self.getCraigslistHousing(reponse)
                        time.sleep(1)


        else:
            print "Connection Failed, invalid token?"


    def getCraigslistHousing(self,city):
      self.city = city
      from craigslist import CraigslistHousing
      #print("before cl")
      if(len(city)<10):
        try:
            cl = CraigslistHousing(site=city , category='apa',
                                 filters={'max_price': 2000, 'min_price': 1000})
            results = cl.get_results(sort_by='newest', geotagged=True, limit=2)
            print("resultdasdsaad=", results)
            for result in results:
                print result
                self.sendMessages(result)
        except:
            self.sendMessages("Invalid Keyword")

findhouse= PostCraiglistHousingOnSlack()
findhouse.getMessages()



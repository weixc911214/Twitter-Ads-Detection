__author__ = 'wei'
import bs4


class PromotionExtractor():
    def __init__(self, html):
        input_file = open(html)
        self.soup = bs4.BeautifulSoup(input_file)

if __name__ == "__main__":
    pe = PromotionExtractor("../twitter.html")
    result = pe.soup.find_all(attrs={"data-item-type": "tweet"})
    for r in result:
        promotion_contents = r.find_all(attrs={"class": "js-promoted-badge"})
        if len(promotion_contents) > 0:
            content = r.find_all(attrs={"class": "content"})
            content = content[0]

            # get promotion tweets
            text = content.find(attrs={"class": "tweet-text"}).text

            # get promotion creator
            context = content.find_all(attrs={"class": "context"})
            promoted_source = ""
            if len(context) > 0:
                promoted_source = context[0].find(attrs={"class": "js-promoted-badge"}).text

            creator = content.find_all(attrs={"class": "promoted-account-in-timeline-name"})
            if len(creator) > 0:
                promoted_source = creator[0].find(attrs={"class": "fullname"}).text


            # get the promotion image, if they have
            media = content.find_all(attrs={"class": "js-media-container"})
            img_url = ""
            if len(media) == 2:
                img_contents = media[0].find_all(attrs={"alt": "Embedded image permalink"})
                if len(img_contents) > 0:
                    img_url = img_contents[0]['src']
            print "-----"
            print "tweet: " + text
            print "promotion creator: " + promoted_source
            print "promotion image: " + img_url









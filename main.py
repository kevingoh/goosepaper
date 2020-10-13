import sys
print(sys.version)

from goosepaper import (
    Goosepaper,
    RSSFeedStoryProvider,
    WikipediaCurrentEventsStoryProvider,
    MultiTwitterStoryProvider,
    WeatherStoryProvider,
    TwitterStoryProvider,
)

print(
    Goosepaper(
        [
            #WikipediaCurrentEventsStoryProvider(),
            #WeatherStoryProvider(woe="2358820"),
            #RSSFeedStoryProvider("https://news.yahoo.com/rss/world", limit=10),
            RSSFeedStoryProvider("https://rss.bloople.net/?url=https%3A%2F%2Fnews.yahoo.com%2Frss%2Fmostviewed&showtitle=false&type=js", limit=5),
            #MultiTwitterStoryProvider(
                #["reuters", "bbcWorld"], limit_per=5
            #),
            #TwitterStoryProvider("bbcWorld",limit=5),
        ]
    ).to_html()
)

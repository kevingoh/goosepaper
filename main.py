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
            WeatherStoryProvider(woe="551801"),
            RSSFeedStoryProvider("https://www.thestar.com.my/rss/News/", limit=20),
            RSSFeedStoryProvider("https://www.thestar.com.my/rss/Business", limit=20),
            
            #MultiTwitterStoryProvider(
            #    ["reuters", "bbcWorld", "axios", "BethanyAllenEbr", "NPR"], limit_per=5
            #),
            # Pending this issue: https://github.com/j6k4m8/goosepaper/issues/5
        ]
    ).to_html()
)

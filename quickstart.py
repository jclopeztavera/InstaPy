# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import ahimsa_settings
import os

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=os.environ.get('USER'),
                  password=os.environ.get('PWD'),
                  headless_browser=False)

with smart_run(session):
  """ Activity flow """
  # general settings
  session.set_dont_include(ahimsa_settings.DONT_INCLUDE)

  # activity
  session.like_by_tags(ahimsa_settings.TAGS, amount=10)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=35)
  session.set_comments(ahimsa_settings.COMMENTS)
  session.join_pods(topic=ahimsa_settings.TOPICS, engagement_mode='no_comments')

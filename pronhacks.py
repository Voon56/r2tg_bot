Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from __future__ import unicode_literals

import telegram
import praw
import logging
import html
import sys
import os
import json

from time import sleep
from datetime import datetimecredentials = {}

credentials["token"] = os.environ.get('TOKEN')
credentials["subreddit"] = os.environ.get('SUB')
credentials["channel"] = os.environ.get('CHANNEL')

token = credentials["5151928043:AAHFYBu2MVzT0TLHrZIQ8UdOjQl7B3wzpEI"]
channel = credentials["@fortgonly67"]
sub = "porn"
start_time = datetime.utcnow().timestamp()
SyntaxError: multiple statements found while compiling a single statement
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)

if credentials["token"] == "":
    raise RuntimeError('Bot token not found 🙁! Put bot token🔐 in credentials.json!')
if credentials["subreddit"] == "":
    raise RuntimeError('Subreddit name not found 🙁! Enter the subreddit name📃 in credentials.json!')
if credentials["channel"] == "":
    raise RuntimeError('Telegram Channel name not found 🙁! Enter the channel name📰 in credentials.json!')
def get_latest_submission_id(subreddit_obj):
    latest_submission = list(subreddit_obj.new(limit=1))[0]
    logger.debug(f"First submission id is {latest_submission.id} | Title is {latest_submission.title}")
    return latest_submission.id
def prepare_msg_from_submission(submission):
    logger.info(f"\tSubmission title: {submission.title} | "
                f"Submitted time: {utils.get_readable_datetime_from_timestamp(submission.created_utc)}")
    return f"{submission.title}\n{submission.shortlink}\n{submission.selftext}\n{MSG_DIVIDER}\n"


if __name__ == '__main__':
    last_submission_id = get_latest_submission_id(subreddit)
    logger.debug(f"Sleep has been set to {SLEEP_TIME_IN_SECS} seconds")

    while True:
        submissions = list(subreddit.new(limit=5, params={'before': f"t3_{last_submission_id}"}))
        for s in submissions:
            bot.sendMessage(chat_id=TELEGRAM_CHANNEL, parse_mode=telegram.ParseMode.HTML,
                            text=prepare_msg_from_submission(s))

        if submissions:
            last_submission_id = submissions[0].id

        sleep(SLEEP_TIME_IN_SECS)
r = praw.Reddit(user_agent="script by u/SumitPrasad607",
                client_id=os.environ.get('7YIMXe1AC2U11TqBU3GanQ'),
                client_secret=os.environ.get('nolYuirhAdT8sO5r-Rm01XydfFM_oA'),
                username=os.environ.get('SumitPrasad607'),
                password=os.environ.get('garena69'))
r.read_only = True
subreddit = r.subreddit(sub)

bot = telegram.Bot(token=token)
 bot.sendPhoto(chat_id=channel, photo=submission.url, caption=message)
                # bot.sendMessage(chat_id=channel, parse_mode=telegram.ParseMode.HTML, text=message)
                write_submissions(submission.id)
                sleep(60)
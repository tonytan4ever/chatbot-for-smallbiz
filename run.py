import logging

from slackbot import bot
import slackbot_settings


def main():
    logging.basicConfig(**slackbot_settings.LOGGING_CONF)
    logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(
        logging.WARNING
    )
    main_logger = logging.getLogger('chatbot_for_small_business.main')
    main_logger.info(slackbot_settings.STARTING_MESSAGE)
    finbot = bot.Bot()
    finbot.run()


if __name__ == "__main__":
    main()

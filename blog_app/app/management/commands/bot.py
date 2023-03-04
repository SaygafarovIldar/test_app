from django.core.management.base import BaseCommand

from app.bot import bot


class Command(BaseCommand):
    help = "Запускает работу бота"

    def handle(self, *args, **options):
        print("Bot is working")
        bot.infinity_polling()

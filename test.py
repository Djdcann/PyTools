from gmail import Gmail
import secrets

bot = Gmail(secrets.gmail_user, secrets.gmail_pass)
bot.send_email("djdcann@gmail.com", "kek", "Hey there")

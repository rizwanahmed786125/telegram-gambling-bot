import telebot
from telebot import types

# Replace with your bot's API token
API_TOKEN = '7872467504:AAFflIiWabGlfeYPRGvSpRyUD6fRp-JiaT4'

bot = telebot.TeleBot(API_TOKEN)

# User data storage (in-memory)
user_data = {}

# Start Command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    if user_id not in user_data:
        user_data[user_id] = {'balance': 100, 'referrals': 0, 'spins': 0, 'deposited': False}
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎁 Claim Bonus", "🎮 Play Games")
    markup.add("💰 Deposit", "🔗 Referral")
    markup.add("💸 Withdraw")
    bot.send_message(user_id, "Welcome to the Gambling Bot! Choose an option:", reply_markup=markup)

# Bonus Command
@bot.message_handler(func=lambda message: message.text == "🎁 Claim Bonus")
def claim_bonus(message):
    user_id = message.chat.id
    if user_data[user_id]['balance'] == 100:
        bot.reply_to(message, "You have already claimed your ₹100 bonus.")
    else:
        user_data[user_id]['balance'] += 100
        bot.reply_to(message, "₹100 has been added to your balance!")

# Referral Command
@bot.message_handler(func=lambda message: message.text == "🔗 Referral")
def referral_system(message):
    user_id = message.chat.id
    referral_link = f"https://t.me/yourbotusername?start={user_id}"
    bot.reply_to(message, f"Share this link with your friends:\n{referral_link}\n\nEarn spins for every referral!")

# Spin Wheel Function
def spin_wheel():
    return 2  # Always return ₹2 as default win

@bot.message_handler(func=lambda message: message.text == "🎮 Play Games")
def play_games(message):
    user_id = message.chat.id
    spins = user_data[user_id]['spins']
    if spins > 0:
        reward = spin_wheel()
        user_data[user_id]['balance'] += reward
        user_data[user_id]['spins'] -= 1
        bot.reply_to(message, f"You spun the wheel and won ₹{reward}! 🎉")
    else:
        bot.reply_to(message, "You have no spins left. Refer friends to earn more!")

# Deposit Command
@bot.message_handler(func=lambda message: message.text == "💰 Deposit")
def deposit_option(message):
    bot.reply_to(message, "Send your deposit to this UPI ID:\n`haseenabanu15@ybl`\nAfter payment, send a screenshot for manual confirmation.")

# Withdraw Command
@bot.message_handler(func=lambda message: message.text == "💸 Withdraw")
def withdraw_option(message):
    user_id = message.chat.id
    if user_data[user_id]['balance'] >= 150:
        if user_data[user_id]['deposited']:
            bot.reply_to(message, "Send your withdrawal request to the admin for manual processing.")
        else:
            bot.reply_to(message, "You must deposit at least once to activate withdrawals.")
    else:
        bot.reply_to(message, "You need a minimum balance of ₹150 to withdraw.")

# Handle Text Messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "Choose an option from the menu.")

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()
  

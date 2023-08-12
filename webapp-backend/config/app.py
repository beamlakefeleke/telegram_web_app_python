from configparser import ConfigParser

def telegram_key():
    parser = ConfigParser()
    parser.read('C:/Users/user/Documents/telegram bot/telegram-webapp-bot-main/webapp-backend/config/config.ini')
    api_key = parser.get('telegram', 'key')
    return api_key
    

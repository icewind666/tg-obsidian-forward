import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot token issued by @botfather (Telegram)
token = os.getenv('TELEGRAM_BOT_TOKEN')
if not token:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set")

# Path to the folder where new notes should be created
#inbox_path = r'/usr/src/app/FromOutside'
#inbox_path = r'/Users/steelrat/icewind666-obsidian/FromOutside'

# Path to the folder where received pictures should be stored
photo_path = os.getenv('PHOTO_PATH', r'/usr/src/app/img')
if not photo_path:
    raise ValueError("PHOTO_PATH is not set")

# Ollama API key
ollama_api_key = os.getenv('OLLAMA_API_KEY', 'default_key')

# Get sensitive credentials from environment variables
# Use default values if environment variables are not set
token = os.getenv('TELEGRAM_BOT_TOKEN', 'default_token')

# URL of the Ollama server
#ollama_url = 'host.docker.internal:11434'
ollama_url = os.getenv('OLLAMA_URL', 'host.docker.internal:11434')

# Model to use for generating a title and summary of the note
ollama_model = os.getenv('OLLAMA_MODEL', 'qwen3:14b')

# Path to the Obsidian vault
inbox_path = os.getenv('INBOX_PATH', r'/Users/steelrat/icewind666-obsidian/')

# If True, messages (including picture captions) will retain formatting (bold, italic, links, etc.)
# If False, messages will be saved as plain text. This also removes inline links.
format_messages = True

#if True, callout block containing link information such as description and/or image will be created
# for messages containing single url
#if False, or more than one url in the message, no callout will be created
create_link_info = True

# If True, voice messages will be recognized to text.
# This requires Whisper ( https://github.com/openai/whisper ), FFMPEG, Python and PyTorch to be installed
# on the machine where the script is running.
# If False, voice messages will not be recognized nor stored.
recognize_voice = False

# Whisper speech recognition software's model options and their relative speed and size of DB:
# tiny (x32, 78MB), base(x16, 145MB), small(x6, 484MB), medium(x2, 1.5GB), large(x1, 3.1GB).
# These are general models. English-only models also exist. Check https://github.com/openai/whisper .
whisper_model = 'medium'

# The following set of options define file name of the note where Telegram posts appear.
# Resulting file name consists of concatenated prefix, date, and postfix.
# With the default config values, full note name would be like Telegram-2023-01-02_Notes.md.
# To omit either prefix or postfix (or both), comment out corresponding option with # or edit it to be empty.
# To omit the date part and always put new messages in a single static file, comment out note_date option
# or edit it to be empty.
note_prefix = 'Telegram-'
note_date = True
note_postfix = '_Notes'

# The following parameter sets logging level:
# 0 - Disable any logging. The only traces of the program are notes and files in the vault.
# 1 - Basic logging of the main actions and errors in the `bot.log` file in the script folder.
# 2 - Extended logging: the same as basic + recording of incoming messages to
# `messages-YYYY-MM-DD.txt` file in the script folder in order to help debugging the script.
log_level = 2

# If True, then all line breaks are removed from the note, and any note literally becomes one-line note.
# If False, then the note is stored including all line breaks.
one_line_note = False

# If one of the specified substrings is found in the message text (case insensitive),
# the message will be converted to a Markdown task like the following:
# - [ ] Complete one important task
# To turn this off, specify task_keywords = {}
task_keywords = {'задач', 'сделать', 'todo', 'complete'}

# If one of the keywords is found in the message text, the specified tag will be added to the message
# To turn this off, specify negative_keywords = {}
negative_keywords = {'негатив', 'печал'}
negative_tag = '#негатив'

# The ID of the chat the bot should read. Messages from other chats will be ignored.
# When the bot receives the /start command, it replies with the ID of the chat.
# This setting is not in effect yet.
# my_chat_id = -xxxxxxxxx


# Prompt for generating a title for the note
ollama_title_prompt="""
Создай название заметки (необязательно на русском языке), название должно быть не более 50 
символов,без знаков препинания. Это название будет использовано как часть имени файла, поэтому
можно использовать только символы валидные для имен файлов. Не добавляй в конце расширение. 
Название должно отражать суть содержания заметки.
Твой результат должен содержать только само название (оно используется парсерами далее) без суффиксов и 
описаний этого названия, только результат. Название заметки должно быть осмысленным словом (или фразой, несколькими словами через подчеркивание) передающим
 смысловое содержание текста заметки, его основную мысль.
Нельзя предварять результат префиксами типа "Вот текст"
 или "Можно использовать..." - результат должен содержать ТОЛЬКО самое название заметки!
Если текст заметки короткий - используй его в качестве 
названия. Запрещено использовать кавычки в результате. Название не должно содержать непереведенные английские слова - если заметка на английском языке делай название 
на английском, если заметка на русском языке (большая часть текста) - название должно быть на русском языке
Текст заметки:"
"""

# Prompt for generating a summary of the note
ollama_summary_prompt="""
Создай краткое содержание текста (для заметки),обязательно на русском языке, 
оно должно быть не более 2000 символов. Нельзя предварять результат префиксами типа "Вот текст"
 или "Создаю краткое содержание" - результат должен содержать ТОЛЬКО самое краткое содержание текста.
Если текст заметки короткий - используй его в качестве названия. Краткое содержание не должно содержать непереведенные английские слова - если заметка на английском 
языке делай все содержание переводом на русском языке. Краткое содержание должно быть ТОЛЬКО на русском языке и содержать осмысленный текст.
Краткое содержание не должно быть однострочным - оно должно отражать основную мысль текста заметки.
Текст:"
"""

# Path to the file with the structure of the Obsidian vault
ollama_folders_file='paths.txt'

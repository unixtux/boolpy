#!/bin/env python3
'''
Constants attributes of the SUBCLASSES.
'''

# MessageOrigin (4)
DEFAULT_MESSAGE_ORIGIN_USER = 'user'
DEFAULT_MESSAGE_ORIGIN_HIDDEN_USER = 'hidden_user'
DEFAULT_MESSAGE_ORIGIN_CHAT = 'chat'
DEFAULT_MESSAGE_ORIGIN_CHANNEL = 'channel'

# ChatBoostSource (3)
DEFAULT_CHAT_BOOST_SOURCE_PREMIUM = 'premium'
DEFAULT_CHAT_BOOST_SOURCE_GIFT_CODE = 'gift_code'
DEFAULT_CHAT_BOOST_SOURCE_GIVEAWAY = 'giveaway'

# ReactionType (3)
DEFAULT_REACTION_TYPE_EMOJI = 'emoji'
DEFAULT_REACTION_TYPE_CUSTOM_EMOJI = 'custom_emoji'
DEFAULT_REACTION_TYPE_PAID = 'paid'

# ChatMember (6)
DEFAULT_CHAT_MEMBER_OWNER = 'creator'
DEFAULT_CHAT_MEMBER_ADMINISTRATOR = 'administrator'
DEFAULT_CHAT_MEMBER_MEMBER = 'member'
DEFAULT_CHAT_MEMBER_RESTRICTED = 'restricted'
DEFAULT_CHAT_MEMBER_LEFT = 'left'
DEFAULT_CHAT_MEMBER_BANNED = 'kicked'

# BotCommandScope (7)
DEFAULT_BOT_COMMAND_SCOPE_DEFAULT = 'default'
DEFAULT_BOT_COMMAND_SCOPE_ALL_PRIVATE_CHATS = 'all_private_chats'
DEFAULT_BOT_COMMAND_SCOPE_ALL_GROUP_CHATS = 'all_group_chats'
DEFAULT_BOT_COMMAND_SCOPE_ALL_CHAT_ADMINISTRATORS = 'all_chat_administrators'
DEFAULT_BOT_COMMAND_SCOPE_CHAT = 'chat'
DEFAULT_BOT_COMMAND_SCOPE_CHAT_ADMINISTRATORS = 'chat_administrators'
DEFAULT_BOT_COMMAND_SCOPE_CHAT_MEMBER = 'chat_member'

# MenuButton (3)
DEFAULT_MENU_BUTTON_COMMANDS = 'commands'
DEFAULT_MENU_BUTTON_WEB_APP = 'web_app'
DEFAULT_MENU_BUTTON_DEFAULT = 'default'

# InlineQueryResult (20)
DEFAULT_INLINE_QUERY_RESULT_ARTICLE = 'article'
DEFAULT_INLINE_QUERY_RESULT_PHOTO = 'photo'
DEFAULT_INLINE_QUERY_RESULT_GIF = 'gif'
DEFAULT_INLINE_QUERY_RESULT_MPEG4_GIF = 'mpeg4_gif'
DEFAULT_INLINE_QUERY_RESULT_VIDEO = 'video'
DEFAULT_INLINE_QUERY_RESULT_AUDIO = 'audio'
DEFAULT_INLINE_QUERY_RESULT_VOICE = 'voice'
DEFAULT_INLINE_QUERY_RESULT_DOCUMENT = 'document'
DEFAULT_INLINE_QUERY_RESULT_LOCATION = 'location'
DEFAULT_INLINE_QUERY_RESULT_VENUE = 'venue'
DEFAULT_INLINE_QUERY_RESULT_CONTACT = 'contact'
DEFAULT_INLINE_QUERY_RESULT_GAME = 'game'
DEFAULT_INLINE_QUERY_RESULT_CACHED_PHOTO = 'photo'
DEFAULT_INLINE_QUERY_RESULT_CACHED_GIF = 'gif'
DEFAULT_INLINE_QUERY_RESULT_CACHED_MPEG4_GIF = 'mpeg4_gif'
DEFAULT_INLINE_QUERY_RESULT_CACHED_STICKER = 'sticker'
DEFAULT_INLINE_QUERY_RESULT_CACHED_DOCUMENT = 'document'
DEFAULT_INLINE_QUERY_RESULT_CACHED_VIDEO = 'video'
DEFAULT_INLINE_QUERY_RESULT_CACHED_VOICE = 'voice'
DEFAULT_INLINE_QUERY_RESULT_CACHED_AUDIO = 'audio'

# PassportElementError (9)
DEFAULT_PASSPORT_ELEMENT_ERROR_DATA_FIELD = 'data'
DEFAULT_PASSPORT_ELEMENT_ERROR_FRONT_SIDE = 'front_side'
DEFAULT_PASSPORT_ELEMENT_ERROR_REVERSE_SIDE = 'reverse_side'
DEFAULT_PASSPORT_ELEMENT_ERROR_SELFIE = 'selfie'
DEFAULT_PASSPORT_ELEMENT_ERROR_FILE = 'file'
DEFAULT_PASSPORT_ELEMENT_ERROR_FILES = 'files'
DEFAULT_PASSPORT_ELEMENT_ERROR_TRANSLATION_FILE = 'translation_file'
DEFAULT_PASSPORT_ELEMENT_ERROR_TRANSLATION_FILES = 'translation_files'
DEFAULT_PASSPORT_ELEMENT_ERROR_UNSPECIFIED = 'unspecified'

# InputMedia (5)
DEFAULT_INPUT_MEDIA_PHOTO = 'photo'
DEFAULT_INPUT_MEDIA_VIDEO = 'video'
DEFAULT_INPUT_MEDIA_ANIMATION = 'animation'
DEFAULT_INPUT_MEDIA_AUDIO = 'audio'
DEFAULT_INPUT_MEDIA_DOCUMENT = 'document'

# BackgroundType (4)
DEFAULT_BACKGROUND_TYPE_FILL = 'fill'
DEFAULT_BACKGROUND_TYPE_WALLPAPER = 'wallpaper'
DEFAULT_BACKGROUND_TYPE_PATTERN = 'pattern'
DEFAULT_BACKGROUND_TYPE_CHAT_THEME = 'chat_theme'

# BackgroundFill (3)
DEFAULT_BACKGROUND_FILL_SOLID = 'solid'
DEFAULT_BACKGROUND_FILL_GRADIENT = 'gradient'
DEFAULT_BACKGROUND_FILL_FREEFORM_GRADIENT = 'freeform_gradient'

# TransactionPartner (3)
DEFAULT_TRANSACTION_PARTNER_FRAGMENT = 'fragment'
DEFAULT_TRANSACTION_PARTNER_USER = 'user'
DEFAULT_TRANSACTION_PARTNER_OTHER = 'other'

# RevenueWithdrawalState (3)
DEFAULT_REVENUE_WITHDRAWAL_STATE_PENDING = 'pending'
DEFAULT_REVENUE_WITHDRAWAL_STATE_SUCCEEDED = 'succeeded'
DEFAULT_REVENUE_WITHDRAWAL_STATE_FAILED = 'failed'

# PaidMedia (3)

DEFAULT_PAID_MEDIA_PREVIEW = 'preview'
DEFAULT_PAID_MEDIA_PHOTO = 'photo'
DEFAULT_PAID_MEDIA_VIDEO = 'video'

# InputPaidMedia (2)
DEFAULT_INPUT_PAID_MEDIA_PHOTO = 'photo'
DEFAULT_INPUT_PAID_MEDIA_VIDEO = 'video'

# TransactionPartnerTelegramAds (?)
DEFAULT_TRANSACTION_PARTNER_TELEGRAM_ADS = 'telegram_ads'

# TransactionPartnerTelegramApi (?)
DEFAULT_TRANSACTION_PARTNER_TELEGRAM_API = 'telegram_api'
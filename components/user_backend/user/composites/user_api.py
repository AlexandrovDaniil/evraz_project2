from user.adapters import user_api, database
from user.application import services
from classic.sql_storage import TransactionContext
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Settings:
    db = database.Settings()
    user_api = user_api.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL, echo=True)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)
    Session = sessionmaker(bind=engine)
    users_repo = database.repositories.UsersRepo(context=context)
    # chats_repo = database.repositories.ChatsRepo(context=context)
    # chat_members_repo = database.repositories.ChatsMembersRepo(context=context)
    # chat_messages_repo = database.repositories.ChatsMessagesRepo(context=context)


class Application:
    is_dev_mode = Settings.user_api.IS_DEV_MODE
    users = services.Users(user_repo=DB.users_repo)
    # chats = services.Chats(chat_repo=DB.chats_repo, user_repo=DB.users_repo, chat_members_repo=DB.chat_members_repo,
    #                        chat_messages_repo=DB.chat_messages_repo)


class Aspects:
    services.join_points.join(DB.context)
    user_api.join_points.join(DB.context)


app = user_api.create_app(
    is_dev_mode=Application.is_dev_mode,
    users=Application.users,

)

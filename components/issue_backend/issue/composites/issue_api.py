from threading import Thread

from issue.adapters import issue_api, database, message_bus
from issue.application import services
from classic.sql_storage import TransactionContext
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from kombu import Connection
from classic.messaging_kombu import KombuPublisher


class Settings:
    db = database.Settings()
    issue_api = issue_api.Settings()
    message_bus = message_bus.Settings()


class DB:
    engine = create_engine(Settings.db.DB_URL, echo=True)
    database.metadata.create_all(engine)

    context = TransactionContext(bind=engine)
    Session = sessionmaker(bind=engine)
    issues_repo = database.repositories.IssuesRepo(context=context)
    # chats_repo = database.repositories.ChatsRepo(context=context)
    # chat_members_repo = database.repositories.ChatsMembersRepo(context=context)
    # chat_messages_repo = database.repositories.ChatsMessagesRepo(context=context)


class Application:
    is_dev_mode = Settings.issue_api.IS_DEV_MODE
    issues = services.Issues(issue_repo=DB.issues_repo,
                             # publisher=MessageBus.publisher,
                             )


class MessageBus:
    connection = Connection(Settings.message_bus.BROKER_URL)
    consumer = message_bus.create_consumer(connection, Application.issues)

    @staticmethod
    def declare_scheme():
        message_bus.broker_scheme.declare(MessageBus.connection)


class Aspects:
    services.join_points.join(DB.context)
    issue_api.join_points.join(DB.context)


MessageBus.declare_scheme()
consumer = Thread(target=MessageBus.consumer.run, daemon=True)
consumer.start()

app = issue_api.create_app(
    is_dev_mode=Application.is_dev_mode,
    issues=Application.issues,

)

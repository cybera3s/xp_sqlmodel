from sqlmodel import Session

from db import engine, create_db_and_tables
from models.blog import Post



def seed_db() -> None:
    post1 = Post(
        title="Python",
        content="python is great",
    )
    post2 = Post(
        title="Sqlmodel",
        content="it is a great ORM",
    )
    post3 = Post(
        title="CodeXP",
        content="it can help you",
    )

    with Session(engine) as session:
        session.add(post1)
        session.add(post2)
        session.add(post3)
        session.commit()


def main() -> None:
    create_db_and_tables()
    seed_db()



if __name__ == "__main__":
    main()

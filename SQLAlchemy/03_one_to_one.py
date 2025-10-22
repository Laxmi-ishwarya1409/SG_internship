# ONE TO ONE
from sqlalchemy import Integer, String, Column, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base,relationship,sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True)
    name = Column(String)

    profile = relationship("Profile",back_populates="user",uselist = False)

    def __repr__(self):
        return f"Username : {self.name} Bio : {self.profile.bio}"


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer,primary_key=True)
    bio = Column(String)

    user_id = Column(Integer,ForeignKey("users.id"),unique=True)

    user = relationship("User",back_populates="profile")

    def __repr__(self):
        return f"Username : {self.user.name} Bio : {self.bio}"


engine = create_engine("sqlite:///user_profile.db",echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session=Session()


user1 = User(name="Laxmi Ishwarya")
profile1 = Profile(bio="Student",user=user1)

session.add_all([user1,profile1])
session.commit()

user = session.query(User).filter_by(name="Laxmi Ishwarya").first()
print(f"{user.name} bio: {user.profile.bio}")

all_users = session.query(User).all()
for i in all_users:
    print(f"{i.name}, {i.profile.bio}")

# model.py
from sqlalchemy import Boolean, Column, Integer, String, create_engine
from app.database.config import Base, BaseMixin


# 用户信息
class UserInfo(Base):
    __tablename__ = "userinfo"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # autoincrement自增长 index索引
    username = Column(String, unique=True, nullable=True, index=True, comment="用户名")  # nullable不能为空
    name = Column(String(10), unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    age = Column(Integer, nullable=True, )
    sex = Column(Integer, nullable=True, )
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return self.username


class User(Base, BaseMixin):
    __tablename__ = "user"

    Name = Column(String(36), nullable=False)
    Phone = Column(String(36), nullable=False, unique=False)

    def __repr__(self):
        return self.Name + ":" + self.Phone

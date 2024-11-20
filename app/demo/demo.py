from app.database.config import get_session
from app.database.model import User

# with get_session() as session:
#     result = session.execute('select * from user')
#     result = result.fetchall()
#     print(result)
#


# # 查询User
# with get_session() as session:
#     print(session.query(User).all())



# ## 增加一个User 表中的信息
# with get_session() as session:
#     session.add(User(Name='寻悟空', Phone='18827603916'))



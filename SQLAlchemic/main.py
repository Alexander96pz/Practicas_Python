from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound
from config.bd import engine
from models.user import User,Base
Session = sessionmaker(engine)
session = Session()
# METODOS QUERY: https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_using_query.htm
def consultasMultiples():
    datausers=session.query(User).filter(
        User.id > 1
    ).filter(
        User.name == "Alex"
    )
    # NOTA: query(Class) return un objeto || query(arg) return en tupla
    for u in datausers:
        print(u.id)
def consultasUnicas():
    # metodo 1 first()
    datauser = session.query(User).filter(
        User.id == 4
    ).first()
    if datauser:
        print(datauser.name)
    else:
        print("no existe")
    # metodo 2 one()
    # try:
    #     datauser = session.query(User).filter(
    #         User.id == 100
    #     ).one()
    #     print(datauser.name)
    # except NoResultFound:
    #     print("No se encuentra el usuario")
def updateRegistro():
    session.query(User).filter(User.id==1).update(
        {
            User.name:"Carlos",
            User.apellido:"Jimenez"
        }
    )
    session.commit()
def deleteRegistro():
    session.query(User).filter(User.id==2).delete()
    session.commit()


if __name__ == '__main__':
    # Crea el modelos
    Base.metadata.create_all(engine)
    # user1=User(name="Alex",apellido="Pizarro")
    # user2=User(name="Leonel",apellido="Velez")

    # # add to DB
    # session.add(user1)
    # session.add(user2)
    # # save changes
    # session.commit()
    # consult Multiples
    consultasMultiples()
    # # PARA CONSULTAS UNICAS https://www.youtube.com/watch?v=yeN_3jdyCho
    # consultasUnicas()
    # updateRegistro()
    # deleteRegistro()


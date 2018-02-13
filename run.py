from coins import db, models


if __name__ == "__main__":
    models.Base.metadata.create_all(db.engine)
    session = db.get_session()
    m = models.Metal(name='test_met_1')
    session.add(m)
    session.commit()
    print(m.id)


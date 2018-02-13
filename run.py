from coins import core, db, models


if __name__ == "__main__":
    print('Updating prices...')
    session = db.Session()
    core.update_metal_prices(session)
    metals = session.query(models.Metal).all()
    print('Latest prices:')
    for metal in metals:
        print('{}: {}'.format(metal.name, metal.last_price.value))

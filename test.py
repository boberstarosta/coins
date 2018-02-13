from coins import db
from coins.models import Metal
from coins.core import update_metal_prices


update_metal_prices()

session = db.get_session()

silver = session.query(Metal).filter_by(symbol='XAGPLN').first()
print(silver)
print(silver.last_price)

gold = session.query(Metal).filter_by(symbol='XAUPLN').first()
print(gold)
print(gold.last_price)

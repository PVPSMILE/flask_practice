from shop.settings import db

class Product(db.Model):

    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(50), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    count = db.Column(db.Integer, nullable = False)
    discount = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Integer, nullable = False)

    final_price = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"id: {self.id}; name: {self.name};"
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bank(db.Model):
    __tablename__ = 'banks'
    
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(49), nullable=False)
    
    branches = db.relationship('Branch', backref='bank', lazy=True)

    def __repr__(self):
        return f'<Bank {self.name}>'

class Branch(db.Model):
    __tablename__ = 'branches'
    
    ifsc = db.Column(db.String(11), primary_key=True)
    bank_id = db.Column(db.BigInteger, db.ForeignKey('banks.id'), nullable=False)
    branch = db.Column(db.String(74), nullable=False)
    address = db.Column(db.String(195))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    state = db.Column(db.String(26))
    
    def __repr__(self):
        return f'<Branch {self.branch}>'

class BankBranch(db.Model):
    __tablename__ = 'bank_branches'
    
    ifsc = db.Column(db.String(11), primary_key=True)
    bank_id = db.Column(db.BigInteger, nullable=False)
    branch = db.Column(db.String(74))
    address = db.Column(db.String(195))
    city = db.Column(db.String(50))
    district = db.Column(db.String(50))
    state = db.Column(db.String(26))
    bank_name = db.Column(db.String(49))
    
    def __repr__(self):
        return f'<BankBranch {self.branch} - {self.bank_name}>'

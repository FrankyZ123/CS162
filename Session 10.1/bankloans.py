import sqlalchemy 
from sqlalchemy import create_engine, Column, Text, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker 

engine = create_engine('sqlite:///bankloans.db')
engine.connect()

Base = declarative_base() 

class Clients(Base):
	__tablename__ = 'clients'
	clientnumber = Column(Integer, primary_key=True, index=True)
	firstname = Column(Text, index=True)
	surname = Column(Text, index=True)
	email = Column(Text)
	phone = Column(Integer)

class Loans(Base):
	__tablename__ = 'loans'
	accountnumber = Column(Integer, primary_key=True, index=True)
	clientnumber = Column(Integer, ForeignKey('clients.clientnumber'), index=True)
	startdate = Column(Text)
	startmonth = Column(Text)
	term = Column(Integer)
	remaining_term = Column(Integer)
	principaldebt = Column(Integer)
	accountlimit = Column(Integer)
	balance = Column(Integer)
	status = Column(Integer)

Base.metadata.create_all(bind=engine) 

Session = sessionmaker(bind=engine)
session = Session()

clients = [
	{
		'clientnumber' : 1, 
		'firstname' : 'Robert', 
		'lastname' : 'Warren', 
		'email' : 'RobertDWarren@teleworm.us', 
		'phone' : '(251) 546-9442'
	},
	{
		'clientnumber' : 2, 
		'firstname' : 'Vincent', 
		'lastname' : 'Brown', 
		'email' : 'VincentHBrown@rhyta.com', 
		'phone' : '(125) 546-4478'
	},
	{
		'clientnumber' : 3, 
		'firstname' : 'Janet', 
		'lastname' : 'Prettyman', 
		'email' : 'JanetTPrettyman@teleworm.us', 
		'phone' : '(949) 569-4371'
	},
	{
		'clientnumber' : 4, 
		'firstname' : 'Martina', 
		'lastname' : 'Kershner', 
		'email' : 'MartinaMKershner@rhyta.com', 
		'phone' : '(630) 446-8851'
	},
	{
		'clientnumber' : 5, 
		'firstname' : 'Tony', 
		'lastname' : 'Schroeder', 
		'email' : 'TonySSchroeder@teleworm.us', 
		'phone' : '(226) 906-2721'
	},
	{
		'clientnumber' : 6, 
		'firstname' : 'Harold', 
		'lastname' : 'Grimes', 
		'email' : 'HaroldVGrimes@dayrep.com', 
		'phone' : '(671) 925-1352'
	}
]
for client in clients:
	client_ = Clients(
		clientnumber=client['clientnumber'], 
		firstname=client['firstname'], 
		surname=client['lastname'],
		email=client['email'],
		phone=client['phone']
	)
	session.add(client_)
	session.commit()
	
loans = [
	{
		'accountnumber' : 1,
		'clientnumber' : 1,
		'startdate' : '2017-11-01 10:00:00',
		'startmonth' : '201712',
		'term' : 36,
		'remaining_term' : 35,
		'principaldebt' : 10000.00,
		'accountlimit' : 15000.00,
		'balance' : 9800.00,
		'status' : 'NORMAL'
	},
	{
		'accountnumber' : 2,
		'clientnumber' : 2,
		'startdate' : '2018-01-01 10:00:00',
		'startmonth' : '201802',
		'term' : 24,
		'remaining_term' : 24,
		'principaldebt' : 1000.00,
		'accountlimit' : 1500.00,
		'balance' : 1000.00,
		'status' : 'NORMAL'
	},
	{
		'accountnumber' : 3,
		'clientnumber' : 1,
		'startdate' : '2016-11-01 10:00:00',
		'startmonth' : '201612',
		'term' : 12,
		'remaining_term' : -3,
		'principaldebt' : 2000.00,
		'accountlimit' : 15000.00,
		'balance' : 4985.12,
		'status' : 'ARREARS'
	},
	{
		'accountnumber' : 4,
		'clientnumber' : 3,
		'startdate' : '2018-01-01 10:00:00',
		'startmonth' : '201802',
		'term' : 24,
		'remaining_term' : 24,
		'principaldebt' : 3500.00,
		'accountlimit' : 5000.00,
		'balance' : 1300.00,
		'status' : 'NORMAL'
	},
	{
		'accountnumber' : 5,
		'clientnumber' : 4,
		'startdate' : '2017-11-01 10:00:00',
		'startmonth' : '201712',
		'term' : 12,
		'remaining_term' : 35,
		'principaldebt' : 10000.00,
		'accountlimit' : 15000.00,
		'balance' : 0.00,
		'status' : 'PAID OFF'
	},
	{
		'accountnumber' : 6,
		'clientnumber' : 5,
		'startdate' : '2018-01-01 10:00:00',
		'startmonth' : '201802',
		'term' : 48,
		'remaining_term' : 24,
		'principaldebt' : 1000.00,
		'accountlimit' : 1500.00,
		'balance' : 0.00,
		'status' : 'PAID OFF'
	},
	{
		'accountnumber' : 7,
		'clientnumber' : 6,
		'startdate' : '2015-11-01 10:00:00',
		'startmonth' : '201512',
		'term' : 12,
		'remaining_term' : -20,
		'principaldebt' : 10000.00,
		'accountlimit' : 15000.00,
		'balance' : 9800.00,
		'status' : 'ARREARS'
	},
	{
		'accountnumber' : 8,
		'clientnumber' : 4,
		'startdate' : '2018-01-01 10:00:00',
		'startmonth' : '201802',
		'term' : 12,
		'remaining_term' : 1,
		'principaldebt' : 2400.00,
		'accountlimit' : 3600.00,
		'balance' : 130.00,
		'status' : 'NORMAL'
	},
]
for loan in loans:
	loan_ = Loans(
		accountnumber=loan['accountnumber'],
		clientnumber=loan['clientnumber'],
		startdate=loan['startdate'],
		startmonth=loan['startmonth'],
		term=loan['term'],
		remaining_term=loan['remaining_term'],
		principaldebt=loan['principaldebt'],
		accountlimit=loan['accountlimit'],
		balance=loan['balance'],
		status=loan['status']
	)
	session.add(loan_)
	session.commit()

#Select Statement
print(session.query(Clients).all())

#Update Statement
for loan in session.query(Loans).all():
	loan.balance +=1
session.commit()
'''
"""You should see something like: 

<User(id=1, name=What's His Name, insurance_id=1)>
"""

print(session.query(Insurance).filter_by(claim_id = 1).all())

"""
Here, you should see something like: 
<Insurance(id=1, claim_id=1>
"""
'''
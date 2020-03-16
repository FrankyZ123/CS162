import sqlalchemy 
from sqlalchemy import create_engine, Column, Text, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker 

engine = create_engine('sqlite:///retail.db')
engine.connect() 
Base = declarative_base()

class Product(Base):
	__tablename__ = 'product'
	productid = Column(Integer, primary_key = True)
	title = Column(Text)
	description = Column(Text)
	price = Column(Integer)
	cost = Column(Integer)

class Orders(Base):
	__tablename__ = 'orders'
	orderid = Column(Integer, primary_key = True)
	customerid = Column(Integer, ForeignKey('product.productid'))
	dateordered = Column(Text)
	monthordered = Column(Text)

class OrderItems(Base):
	__tablename__ = 'orderitems'
	orderid = Column(Integer, ForeignKey('orders.orderid'), primary_key = True)
	productid = Column(Integer, ForeignKey('product.productid'), primary_key = True)
	quantity = Column(Integer)

class Warehouse(Base):
	__tablename__ = 'warehouse'
	warehouseid = Column(Integer, primary_key = True)
	name = Column(Text)
	addressline1 = Column(Text)
	addressline2 = Column(Text)
	addressline3 = Column(Text)

class Inventory(Base):
	__tablename__ = 'inventory'
	warehouseid = Column(Integer, ForeignKey('warehouse.warehouseid'), primary_key = True)
	productid = Column(Integer, ForeignKey('product.productid'), primary_key = True)
	quantity = Column(Integer)

class Supplier(Base):
	__tablename__ = 'supplier'
	supplierid = Column(Integer, primary_key = True)
	name = Column(Text)
	addressline1 = Column(Text)
	addressline2 = Column(Text)
	addressline3 = Column(Text)
	phonenumber = Column(Text)
	email = Column(Text)

class SupplierProduct(Base):
	__tablename__ = 'supplierproduct'
	supplierid = Column(Integer, ForeignKey('supplier.supplierid'), primary_key = True)
	productid = Column(Integer, ForeignKey('product.productid'), primary_key = True)
	daysleadtime = Column(Integer)
	cost = Column(Integer)

class SupplierOrder(Base):
	__tablename__ = 'supplierorder'
	supplierorderid = Column(Integer, primary_key = True)
	supplierid = Column(Integer, ForeignKey('supplier.supplierid'))
	productid = Column(Integer, ForeignKey('product.productid'))
	warehouseid = Column(Integer, ForeignKey('warehouse.warehouseid'))
	quantity = Column(Integer)
	status = Column(Text)
	dateordered = Column(Text)
	datedue = Column(Text)

class Customer(Base):
	__tablename__ = 'customer'
	customerid = Column(Integer, primary_key = True)
	firstname = Column(Text)
	surname = Column(Text)
	addressline1 = Column(Text)
	addressline2 = Column(Text)
	addressline3 = Column(Text)
	phonenumber = Column(Text)
	email = Column(Text)

Base.metadata.create_all(bind=engine) 

Session = sessionmaker(bind=engine)
session = Session()

products = [
	{
		'productid' : 3001,
		'title' : "Widget",
		'description' : "Widge all your worries away!",
		'price' : 99.95,
		'cost' : 23.05
	},
	{
		'productid' : 3002,
		'title' : "Wodget",
		'description' : "Wodge all your worries away!",
		'price' : 199.95,
		'cost' : 123.05
	}
]
for product in products:
	product_ = Product(
		productid=product['productid'],
		title=product['title'],
		description=product['description'],
		price=product['price'],
		cost=product['cost']
	)
	session.add(product_)
	session.commit()

orders = [
	{
		'orderid' : 1000,
		'customerid' : 3001,
		'dateordered' : '2025-01-01 10:00:00',
		'monthordered' : '202501'
	}
]
for order in orders:
	order_ = Orders(
		orderid=order['orderid'],
		customerid=order['customerid'],
		dateordered=order['dateordered'],
		monthordered=order['monthordered']
	)
	session.add(order_)
	session.commit()

orderitems = [
	{
		'orderid' : 1000,
		'productid' : 3001,
		'quantity' : 1
	},
	{
		'orderid' : 1000,
		'productid' : 3002,
		'quantity' : 2
	}
]
for orderitem in orderitems:
	orderitem_ = OrderItems(
		orderid=orderitem['orderid'],
		productid=orderitem['productid'],
		quantity=orderitem['quantity']
	)
	session.add(orderitem_)
	session.commit()

warehouses = [
	{
		'warehouseid' : 4001,
		'name' : 'ABC Warehouse',
		'addressline1' : '1374 Elkview Drive',
		'addressline2' : 'Fort Lauderdale',
		'addressline3' : 'FL 33301'
	},
	{
		'warehouseid' : 4002,
		'name' : 'XYZ Warehouse',
		'addressline1' : '1576 Walnut Street',
		'addressline2' : 'Jackson',
		'addressline3' : 'MS 39211'
	},
]
for warehouse in warehouses:
	warehouse_ = Warehouse(
		warehouseid=warehouse['warehouseid'],
		name=warehouse['name'],
		addressline1=warehouse['addressline1'],
		addressline2=warehouse['addressline2'],
		addressline3=warehouse['addressline3']
	)
	session.add(warehouse_)
	session.commit()

inventorys = [
	{
		'warehouseid' : 4001,
		'productid' : 3001,
		'quantity' : 3
	},
	{
		'warehouseid' : 4001,
		'productid' : 3002,
		'quantity' : 1
	},
	{
		'warehouseid' : 4002,
		'productid' : 3001,
		'quantity' : 1
	},
	{
		'warehouseid' : 4002,
		'productid' : 3002,
		'quantity' : 4
	}
]
for inventory in inventorys:
	inventory_ = Inventory(
		warehouseid=inventory['warehouseid'],
		productid=inventory['productid'],
		quantity=inventory['quantity']
	)
	session.add(inventory_)
	session.commit()

suppliers = [
	{
		'supplierid' : 5001,
		'name' : 'Widge Suppliers Ltd',
		'addressline1' : '3316 Whitetail Lane',
		'addressline2' : 'Irving',
		'addressline3' : 'TX 75039',
		'phonenumber' : '479-357-6159',
		'email' : 'TimothyCSilva@widge.com'
	},
	{
		'supplierid' : 5002,
		'name' : 'Wodge Suppliers PLC',
		'addressline1' : '390 Clarksburg Park Road',
		'addressline2' : 'Scottsdale',
		'addressline3' : 'AZ 85256',
		'phonenumber' : '252-441-7555',
		'email' : 'JohnAWilley@wodge.co.uk'
	}
]
for supplier in suppliers:
	supplier_ = Supplier(
		supplierid=supplier['supplierid'],
		name=supplier['name'],
		addressline1=supplier['addressline1'],
		addressline2=supplier['addressline2'],
		addressline3=supplier['addressline3'],
		phonenumber=supplier['phonenumber'],
		email=supplier['email']
	)
	session.add(supplier_)
	session.commit()

supplierproducts = [
	{
		'supplierid' : 5001,
		'productid' : 3001,
		'daysleadtime' : 3,
		'cost' : 23.05
	},
	{
		'supplierid' : 5001,
		'productid' : 3002,
		'daysleadtime' : 20,
		'cost' : 999.99
	},
	{
		'supplierid' : 5002,
		'productid' : 3001,
		'daysleadtime' : 20,
		'cost' : 9999.99
	},
	{
		'supplierid' : 5002,
		'productid' : 3002,
		'daysleadtime' : 5,
		'cost' : 123.05
	}
]
for supplierproduct in supplierproducts:
	supplierproduct_ = SupplierProduct(
		supplierid=supplierproduct['supplierid'],
		productid=supplierproduct['productid'],
		daysleadtime=supplierproduct['daysleadtime'],
		cost=supplierproduct['cost']
	)
	session.add(supplierproduct_)
	session.commit()

supplierorders = [
	{
		'supplierorderid' : 6001,
		'supplierid' : 5001,
		'productid' : 3001,
		'warehouseid' : 4001,
		'quantity' : 99,
		'status' : 'ORDERED',
		'dateordered' : '2025-01-15',
		'datedue' : '2025-01-21'
	},
	{
		'supplierorderid' : 6002,
		'supplierid' : 5001,
		'productid' : 3001,
		'warehouseid' : 4001,
		'quantity' : 99,
		'status' : 'DELIVERED',
		'dateordered' : '2025-01-16',
		'datedue' : '2025-01-23'
	}
]
for supplierorder in supplierorders:
	supplierorder_ = SupplierOrder(
		supplierorderid=supplierorder['supplierorderid'],
		supplierid=supplierorder['supplierid'],
		productid=supplierorder['productid'],
		warehouseid=supplierorder['warehouseid'],
		quantity=supplierorder['quantity'],
		status=supplierorder['status'],
		dateordered=supplierorder['dateordered'],
		datedue=supplierorder['datedue']
	)
	session.add(supplierorder_)
	session.commit()

customers = [
	{
		'customerid' : 2000,
		'firstname' : 'Gertrud',
		'surname' : 'Karr',
		'addressline1' : '1709 Woodridge Lane',
		'addressline2' : 'Memphis',
		'addressline3' : 'TN 38110',
		'phonenumber' : '559-309-6624',
		'email' : 'gkarr@dayrep.com'
	},
	{
		'customerid' : 2001,
		'firstname' : 'Clara',
		'surname' : 'Tang',
		'addressline1' : '500 Retreat Avenue',
		'addressline2' : 'York',
		'addressline3' : 'ME 03909',
		'phonenumber' : '312-367-6954',
		'email' : 'clara_tang@armyspy.com'
	}
]
for customer in customers:
	customer_ = Customer(
		customerid=customer['customerid'],
		firstname=customer['firstname'],
		surname=customer['surname'],
		addressline1=customer['addressline1'],
		addressline2=customer['addressline2'],
		addressline3=customer['addressline3'],
		phonenumber=customer['phonenumber'],
		email=customer['email']
	)
	session.add(customer_)
	session.commit()
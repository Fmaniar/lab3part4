import pytest
from invoice import Invoice

@pytest.fixture()
def products():
    products = {"Pen": {"qnt": 10, "unit_price": 3.75, "discount": 5},
                "Notebook": {"qnt": 5, "unit_price": 7.5, "discount": 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice
    
def test_CanFindInvoiceClass():
    invoice = Invoice()

def test_canCalcTotalImpurePrice(invoice,products):
    invoice.totalImpurePrice(products)
    assert invoice.totalImpurePrice(products) == 75

def test_canCalcTotalDiscount(invoice,products):
    invoice.totalDiscount(products)
    assert invoice.totalDiscount(products) == 5.62

def test_canCalcTotalPurePrice(invoice,products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 69.38

#test 1
def test_canAddProduct(invoice,products):
    product = "stapler"
    unitPrice = 12.00
    qnt = 1
    discount = 1
    result = Invoice().addProduct(qnt,unitPrice,discount)
    products[product] = result
    assert len(products) == 3
#test2
def test_canGetName(invoice,products):
    existingName = "Pen"
    name = invoice.getName(products,0)
    assert existingName == name
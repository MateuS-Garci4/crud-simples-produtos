from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel

def get_products(db: Session):
    """
    Funcao que retorna todos os produtos
    """

    return db.query(ProductModel).all()


def get_product(db: Session, product_id: int):
    """
    Funcao que retorna apenas o produto selecionado
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def create_product(db: Session, product: ProductCreate):
    # transformar minha view para ORM
    db_product = ProductModel(**product.model_dump())

    db.add(db_product)      # adicionar na tabela

    db.commit()             # commitar

    db.refresh(db_product)  # refresh no banco

    return db_product       # retornar pro usuario o produto criado


def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product is None:
        return None
    db.delete(db_product)
    db.commit()
    return db_product


def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name

    if product.description is not None:
        db_product.description = product.description

    if product.price is not None:
        db_product.price = product.price

    if product.categoria is not None:
        db_product.categoria = product.categoria

    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    db.commit()
    db.refresh(db_product)

    return db_product
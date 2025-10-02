from fastapi import FastAPI
from model import Products


app = FastAPI(
    title="fastapi-demo",
    description="A simple FastAPI demo application"
)

products = [
    Products(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
    Products(id=2, name="Smartphone", description="A latest model smartphone", price=699.99, quantity=25),
    Products(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=15),
    Products(id=4, name="Monitor", description="4K UHD Monitor", price=399.99, quantity=8),
    Products(id=5, name="Keyboard", description="Mechanical keyboard", price=89.99, quantity=30)
]

@app.get("/")
async def read_root():
    return {"message": "Welcome to fastapi-demo!"}

@app.get("/products")
async def get_all_products():
    return products

@app.get("/product/{id}")
async def get_product_by(id: int):
    for product in products:
        print(product)
        if product.id == id:
            return product
    return {"message": "Product not found"}

@app.post("/product")
async def create_product(product: Products):
    products.append(product)
    return product

@app.put("/product")
async def update_product(id: int, updated_product: Products):
    for index, product in enumerate(products):
        if product.id == id:
            products[index] = updated_product
            return updated_product
    return {"message": "Product not found"}

@app.delete("/product")
async def delete_product(id: int):
    for index, product in enumerate(products):
        if product.id == id:
            del products[index]
            return {"message": "Product deleted successfully"}
    return {"message": "Product not found"}


# def main():
#     print("Hello from fastapi-demo!")


# if __name__ == "__main__":
#     main()

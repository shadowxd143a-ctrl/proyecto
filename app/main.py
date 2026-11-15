# Punto de entrada para Vercel (ver vercel.json). Las rutas viven en los blueprints de app/.
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()

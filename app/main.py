from app import create_app

app = create_app()

@app.route('/')
def index():
    return {"status": "DropX Logística API funcionando correctamente"}, 200

if __name__ == "__main__":
    app.run()
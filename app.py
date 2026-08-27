import os
from flask import Flask
from frontend.products import frontend_bp
from frontend.cart import cart_bp
from admin import admin_bp
from models.users import db

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'vaii_secure_store_session_secret_key_2026')

# Database Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'vaii.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'static', 'uploads', 'users')

db.init_app(app)

with app.app_context():
    db.create_all()

# Register Blueprints
app.register_blueprint(frontend_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(admin_bp)

# Backwards-compatible endpoint aliases for existing client templates
app.add_url_rule('/', 'index', view_func=app.view_functions['frontend.index'])
app.add_url_rule('/products', 'products', view_func=app.view_functions['frontend.products'])
app.add_url_rule('/product/<product_name>', 'product_detail', view_func=app.view_functions['frontend.product_detail'])
app.add_url_rule('/cart', 'cart', view_func=app.view_functions['cart_bp.cart'])
app.add_url_rule('/add_to_cart', 'add_to_cart', view_func=app.view_functions['cart_bp.add_to_cart'], methods=['GET', 'POST'])
app.add_url_rule('/cart/remove', 'cart_remove', view_func=app.view_functions['cart_bp.cart_remove'])
app.add_url_rule('/checkout', 'checkout', view_func=app.view_functions['cart_bp.checkout'], methods=['GET', 'POST'])
app.add_url_rule('/login', 'login', view_func=app.view_functions['frontend.login'], methods=['GET', 'POST'])
app.add_url_rule('/register', 'register', view_func=app.view_functions['frontend.register'], methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', view_func=app.view_functions['frontend.logout'], methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True)

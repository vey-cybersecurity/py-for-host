from flask import Blueprint, render_template, request, redirect, url_for, make_response, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models.users import db, User
from products import (
    PRODUCTS, 
    get_all_products, 
    get_product_title, 
    get_product_category, 
    get_product_id
)
from frontend.cart import get_cart_data, cart_bp

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/')
def index():
    products_list = get_all_products()
    cart_items, _ = get_cart_data()
    return render_template('index.html', products=products_list, cart_items=cart_items)

@frontend_bp.route('/products')
def products():
    category = request.args.get('category')
    search_query = request.args.get('q', '').strip().lower()
    
    products_list = get_all_products()
    if category:
        products_list = get_product_category(category)
    if search_query:
        products_list = [p for p in products_list if search_query in p['title'].lower() or search_query in p['description'].lower()]
        
    cart_items, _ = get_cart_data()
    return render_template('products.html', products=products_list, cart_items=cart_items, current_category=category)

@frontend_bp.route('/product/<product_name>')
def product_detail(product_name):
    product = get_product_title(product_name)
    if product is None:
        return "Product not found", 404
        
    related_products = get_product_category(product['category'])
    # Exclude current product from related products
    related_products = [p for p in related_products if str(p['id']) != str(product['id'])]
    cart_items, _ = get_cart_data()
    return render_template('product_detail.html', product=product, related_products=related_products, cart_items=cart_items)

@frontend_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        
        if not email or not password:
            flash('Please provide both email and password.', 'error')
            cart_items, _ = get_cart_data()
            return render_template('login.html', cart_items=cart_items, email=email)
            
        user = User.query.filter_by(email=email).first()
        
        # Verify user password (handles both hash and legacy fallback)
        is_valid_password = False
        if user:
            if user.password.startswith(('scrypt:', 'pbkdf2:', 'argon2:')):
                is_valid_password = check_password_hash(user.password, password)
            else:
                is_valid_password = (user.password == password)
                if is_valid_password:
                    user.password = generate_password_hash(password)
                    db.session.commit()
                    
        if user and is_valid_password:
            if user.status and user.status.lower() == 'inactive':
                flash('Your account is inactive. Please contact administrator.', 'error')
                cart_items, _ = get_cart_data()
                return render_template('login.html', cart_items=cart_items)
                
            # Set session data
            session['user_id'] = user.id
            session['user_name'] = user.fullname
            session['user_email'] = user.email
            session['user_role'] = user.role
            
            flash(f'Welcome back, {user.fullname}!', 'success')
            
            # If admin role, redirect to admin dashboard; else storefront
            if user.role in ['Super Admin', 'Admin', 'Product Manager']:
                return redirect(url_for('admin.dashboard'))
            return redirect(url_for('frontend.index'))
            
        flash('Invalid email or password. Please try again.', 'error')
        cart_items, _ = get_cart_data()
        return render_template('login.html', cart_items=cart_items, email=email)
        
    cart_items, _ = get_cart_data()
    return render_template('login.html', cart_items=cart_items)

@frontend_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form.get('fullname', '').strip() or request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        
        if not fullname or not email or not password:
            flash('All fields (Full Name, Email, and Password) are required!', 'error')
            cart_items, _ = get_cart_data()
            return render_template('register.html', cart_items=cart_items, fullname=fullname, email=email)
            
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('This email is already registered. Please sign in.', 'error')
            cart_items, _ = get_cart_data()
            return render_template('register.html', cart_items=cart_items, fullname=fullname, email=email)
            
        hashed_password = generate_password_hash(password)
        avatar = f"https://api.dicebear.com/7.x/avataaars/svg?seed={fullname.replace(' ', '')}"
        
        new_user = User(
            fullname=fullname,
            email=email,
            password=hashed_password,
            role='User',
            status='Active',
            profile_image=avatar
        )
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please sign in with your credentials.', 'success')
        return redirect(url_for('frontend.login'))
        
    cart_items, _ = get_cart_data()
    return render_template('register.html', cart_items=cart_items)

@frontend_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    session.pop('user_email', None)
    session.pop('user_role', None)
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('frontend.login'))
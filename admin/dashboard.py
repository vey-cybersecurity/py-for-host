from flask import Blueprint, render_template
from products import get_dashboard_stats, get_all_products, get_all_categories, get_all_users

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
@admin_bp.route('/dashboard')
def dashboard():
    stats = get_dashboard_stats()
    products = get_all_products()
    categories = get_all_categories()
    users = get_all_users()
    
    # Top 5 most expensive/featured products
    top_products = sorted(products, key=lambda x: x.get('price', 0), reverse=True)[:5]
    
    return render_template(
        'admin/dashboard.html',
        stats=stats,
        products=products,
        categories=categories,
        users=users,
        top_products=top_products,
        active_page='dashboard'
    )
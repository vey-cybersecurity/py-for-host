from flask import render_template, request, redirect, url_for, flash
from admin.dashboard import admin_bp
from products import (
    get_all_products,
    get_product_id,
    create_product,
    update_product,
    delete_product,
    get_all_categories
)

@admin_bp.route('/products')
def products_list():
    query = request.args.get('q', '').strip().lower()
    selected_category = request.args.get('category', '').strip()
    
    all_prods = get_all_products()
    filtered_prods = all_prods
    
    if selected_category:
        filtered_prods = [p for p in filtered_prods if p['category'].strip().lower() == selected_category.lower()]
        
    if query:
        filtered_prods = [
            p for p in filtered_prods 
            if query in p['title'].lower() or query in p['description'].lower() or query in p['category'].lower()
        ]
        
    categories = get_all_categories()
    
    return render_template(
        'admin/products.html',
        products=filtered_prods,
        categories=categories,
        total_count=len(all_prods),
        selected_category=selected_category,
        search_query=query,
        active_page='products'
    )

@admin_bp.route('/products/create', methods=['POST'])
def product_create():
    title = request.form.get('title', '').strip()
    price = request.form.get('price', 0)
    category = request.form.get('category', '').strip()
    description = request.form.get('description', '').strip()
    image = request.form.get('image', '').strip()
    rate = request.form.get('rate', 5.0)
    
    if not title or not category:
        flash('Product title and category are required!', 'error')
        return redirect(url_for('admin.products_list'))
        
    try:
        price = float(price)
    except ValueError:
        price = 0.0
        
    create_product(title, price, description, category, image, rate=rate)
    flash(f'Product "{title}" successfully created!', 'success')
    return redirect(url_for('admin.products_list'))

@admin_bp.route('/products/<int:product_id>/edit', methods=['POST'])
def product_edit(product_id):
    title = request.form.get('title', '').strip()
    price = request.form.get('price', 0)
    category = request.form.get('category', '').strip()
    description = request.form.get('description', '').strip()
    image = request.form.get('image', '').strip()
    
    if not title or not category:
        flash('Product title and category cannot be empty!', 'error')
        return redirect(url_for('admin.products_list'))
        
    try:
        price = float(price)
    except ValueError:
        price = 0.0
        
    updated = update_product(product_id, title, price, description, category, image)
    if updated:
        flash(f'Product "{title}" updated successfully!', 'success')
    else:
        flash('Product not found or update failed.', 'error')
        
    return redirect(url_for('admin.products_list'))

@admin_bp.route('/products/<int:product_id>/delete', methods=['POST'])
def product_delete(product_id):
    success = delete_product(product_id)
    if success:
        flash('Product deleted successfully.', 'success')
    else:
        flash('Failed to delete product.', 'error')
    return redirect(url_for('admin.products_list'))

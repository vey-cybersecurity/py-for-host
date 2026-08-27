from flask import render_template, request, redirect, url_for, flash
from admin.dashboard import admin_bp
from products import (
    get_all_categories,
    create_category,
    update_category,
    delete_category
)

@admin_bp.route('/categories')
def categories_list():
    query = request.args.get('q', '').strip().lower()
    categories = get_all_categories()
    
    if query:
        categories = [
            c for c in categories 
            if query in c['name'].lower() or query in c['description'].lower()
        ]
        
    return render_template(
        'admin/categories.html',
        categories=categories,
        search_query=query,
        active_page='categories'
    )

@admin_bp.route('/categories/create', methods=['POST'])
def category_create():
    name = request.form.get('name', '').strip()
    description = request.form.get('description', '').strip()
    icon = request.form.get('icon', 'fa-solid fa-tag').strip()
    
    if not name:
        flash('Category name is required!', 'error')
        return redirect(url_for('admin.categories_list'))
        
    create_category(name, description, icon)
    flash(f'Category "{name}" created successfully!', 'success')
    return redirect(url_for('admin.categories_list'))

@admin_bp.route('/categories/<int:cat_id>/edit', methods=['POST'])
def category_edit(cat_id):
    name = request.form.get('name', '').strip()
    description = request.form.get('description', '').strip()
    icon = request.form.get('icon', 'fa-solid fa-tag').strip()
    
    if not name:
        flash('Category name cannot be empty!', 'error')
        return redirect(url_for('admin.categories_list'))
        
    updated = update_category(cat_id, name, description, icon)
    if updated:
        flash(f'Category "{name}" updated successfully!', 'success')
    else:
        flash('Category not found or update failed.', 'error')
        
    return redirect(url_for('admin.categories_list'))

@admin_bp.route('/categories/<int:cat_id>/delete', methods=['POST'])
def category_delete(cat_id):
    success = delete_category(cat_id)
    if success:
        flash('Category deleted successfully.', 'success')
    else:
        flash('Failed to delete category.', 'error')
    return redirect(url_for('admin.categories_list'))

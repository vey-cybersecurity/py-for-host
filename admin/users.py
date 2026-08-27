import os
import uuid
from flask import render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from sqlalchemy import text
from werkzeug.security import generate_password_hash
from admin.dashboard import admin_bp
from models.users import db, User

def save_profile_image(file):
    if file and file.filename:
        # Create a unique filename
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        
        # Ensure upload folder exists
        upload_folder = current_app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
            
        filepath = os.path.join(upload_folder, unique_filename)
        file.save(filepath)
        
        # Return the relative path to serve from static
        return f"/static/uploads/users/{unique_filename}"
    return None

@admin_bp.route('/users')
def users_list():
    query_str = request.args.get('q', '').strip().lower()
    selected_role = request.args.get('role', '').strip()
    selected_status = request.args.get('status', '').strip()
    
    # Base raw SQL query
    sql = "SELECT id, fullname, email, role, status, profile_image, created_at, orders_count FROM user WHERE 1=1"
    params = {}
    
    if selected_role:
        sql += " AND LOWER(role) = :role"
        params['role'] = selected_role.lower()
        
    if selected_status:
        sql += " AND LOWER(status) = :status"
        params['status'] = selected_status.lower()
        
    if query_str:
        sql += " AND (LOWER(fullname) LIKE :query OR LOWER(email) LIKE :query OR LOWER(role) LIKE :query)"
        params['query'] = f"%{query_str}%"
        
    sql += " ORDER BY id DESC"
    
    # Execute raw SQL
    result = db.session.execute(text(sql), params)
    users = result.mappings().all()
    
    # Get total count for display
    total_count = db.session.execute(text("SELECT COUNT(id) as count FROM user")).scalar()
    
    return render_template(
        'admin/users.html',
        users=users,
        total_count=total_count,
        selected_role=selected_role,
        selected_status=selected_status,
        search_query=query_str,
        active_page='users'
    )

@admin_bp.route('/users/create', methods=['POST'])
def user_create():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    role = request.form.get('role', 'Customer').strip()
    status = request.form.get('status', 'Active').strip()
    raw_password = request.form.get('password', '').strip() or 'password123'
    
    if not name or not email:
        flash('Name and email are required!', 'error')
        return redirect(url_for('admin.users_list'))
        
    # Check if user exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        flash('Email is already registered!', 'error')
        return redirect(url_for('admin.users_list'))

    # Handle file upload
    profile_image_path = None
    if 'profile_image' in request.files:
        file = request.files['profile_image']
        profile_image_path = save_profile_image(file)
        
    if not profile_image_path:
        profile_image_path = f"https://api.dicebear.com/7.x/avataaars/svg?seed={name.replace(' ', '')}"
        
    # Hash password before saving to db
    hashed_password = generate_password_hash(raw_password)

    # ORM Create
    new_user = User(
        fullname=name,
        email=email,
        password=hashed_password,
        role=role,
        status=status,
        profile_image=profile_image_path
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    flash(f'User "{name}" created successfully with role "{role}"!', 'success')
    return redirect(url_for('admin.users_list'))

@admin_bp.route('/users/<int:user_id>/edit', methods=['POST'])
def user_edit(user_id):
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    role = request.form.get('role', 'Customer').strip()
    status = request.form.get('status', 'Active').strip()
    new_password = request.form.get('password', '').strip()
    
    if not name or not email:
        flash('Name and email cannot be empty!', 'error')
        return redirect(url_for('admin.users_list'))
        
    # ORM Update
    user = User.query.get(user_id)
    if user:
        # Check email uniqueness (if changed)
        if user.email != email:
            existing = User.query.filter_by(email=email).first()
            if existing:
                flash('Email is already taken!', 'error')
                return redirect(url_for('admin.users_list'))
                
        user.fullname = name
        user.email = email
        user.role = role
        user.status = status
        
        # Update password if provided
        if new_password:
            user.password = generate_password_hash(new_password)
            
        # Handle file upload
        if 'profile_image' in request.files:
            file = request.files['profile_image']
            if file and file.filename:
                # We could delete the old image here if we wanted to be perfectly clean
                profile_image_path = save_profile_image(file)
                if profile_image_path:
                    user.profile_image = profile_image_path
                    
        db.session.commit()
        flash(f'User "{name}" updated successfully!', 'success')
    else:
        flash('User not found or update failed.', 'error')
        
    return redirect(url_for('admin.users_list'))

@admin_bp.route('/users/<int:user_id>/delete', methods=['POST'])
def user_delete(user_id):
    # ORM Delete
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        flash('User removed successfully.', 'success')
    else:
        flash('Failed to delete user.', 'error')
    return redirect(url_for('admin.users_list'))

@admin_bp.route('/users/<int:user_id>/toggle-status', methods=['POST'])
def user_toggle_status(user_id):
    # ORM Update
    user = User.query.get(user_id)
    if user:
        user.status = "Inactive" if user.status == "Active" else "Active"
        db.session.commit()
        flash(f"Status for {user.fullname} set to {user.status}.", 'success')
    else:
        flash('User not found.', 'error')
    return redirect(url_for('admin.users_list'))

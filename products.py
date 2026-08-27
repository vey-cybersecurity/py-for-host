from datetime import datetime

PRODUCTS = [
  {
    "id": 1,
    "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
    "price": 109.95,
    "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
    "rating": {
      "rate": 3.9,
      "count": 120
    }
  },
  {
    "id": 2,
    "title": "Mens Casual Premium Slim Fit T-Shirts ",
    "price": 22.3,
    "description": "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_t.png",
    "rating": {
      "rate": 4.1,
      "count": 259
    }
  },
  {
    "id": 3,
    "title": "Mens Cotton Jacket",
    "price": 55.99,
    "description": "great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm hearted love to Father, husband or son in this thanksgiving or Christmas Day.",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_t.png",
    "rating": {
      "rate": 4.7,
      "count": 500
    }
  },
  {
    "id": 4,
    "title": "Mens Casual Slim Fit",
    "price": 15.99,
    "description": "The color could be slightly different between on the screen and in practice. / Please note that body builds vary by person, therefore, detailed size information should be reviewed below on the product description.",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_t.png",
    "rating": {
      "rate": 2.1,
      "count": 430
    }
  },
  {
    "id": 5,
    "title": "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
    "price": 695.0,
    "description": "From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.",
    "category": "jewelery",
    "image": "https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_t.png",
    "rating": {
      "rate": 4.6,
      "count": 400
    }
  },
  {
    "id": 6,
    "title": "Solid Gold Petite Micropave ",
    "price": 168.0,
    "description": "Satisfaction Guaranteed. Return or exchange any order within 30 days.Designed and sold by Hafeez Center in the United States. Satisfaction Guaranteed. Return or exchange any order within 30 days.",
    "category": "jewelery",
    "image": "https://fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_t.png",
    "rating": {
      "rate": 3.9,
      "count": 70
    }
  },
  {
    "id": 7,
    "title": "White Gold Plated Princess",
    "price": 9.99,
    "description": "Classic Created Wedding Engagement Solitaire Diamond Promise Ring for Her. Gifts to spoil your love more for Engagement, Wedding, Anniversary, Valentine's Day...",
    "category": "jewelery",
    "image": "https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_t.png",
    "rating": {
      "rate": 3.0,
      "count": 400
    }
  },
  {
    "id": 8,
    "title": "Pierced Owl Rose Gold Plated Stainless Steel Double",
    "price": 10.99,
    "description": "Rose Gold Plated Double Flared Tunnel Plug Earrings. Made of 316L Stainless Steel",
    "category": "jewelery",
    "image": "https://fakestoreapi.com/img/51UDEzMJVpL._AC_UL640_QL65_ML3_t.png",
    "rating": {
      "rate": 1.9,
      "count": 100
    }
  },
  {
    "id": 9,
    "title": "WD 2TB Elements Portable External Hard Drive - USB 3.0 ",
    "price": 64.0,
    "description": "USB 3.0 and USB 2.0 Compatibility Fast data transfers Improve PC Performance High Capacity; Compatibility Formatted NTFS for Windows 10, Windows 8.1, Windows 7; Reformatting may be required for other operating systems; Compatibility may vary depending on user's hardware configuration and operating system",
    "category": "electronics",
    "image": "https://fakestoreapi.com/img/61IBBVJvSDL._AC_SY879_t.png",
    "rating": {
      "rate": 3.3,
      "count": 203
    }
  },
  {
    "id": 10,
    "title": "SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s",
    "price": 109.0,
    "description": "Easy upgrade for faster boot up, shutdown, application load and response (As compared to 5400 RPM SATA 2.5” hard drive; Based on published specifications and internal benchmarking tests using PCMark vantage scores) Boosts burst write performance, making it ideal for typical PC workloads The perfect balance of performance and reliability Read/write speeds of up to 535MB/s/450MB/s (Based on internal testing; Performance may vary depending upon drive capacity, host device, OS and application.)",
    "category": "electronics",
    "image": "https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_t.png",
    "rating": {
      "rate": 2.9,
      "count": 470
    }
  },
  {
    "id": 11,
    "title": "Silicon Power 256GB SSD 3D NAND A55 SLC Cache Performance Boost SATA III 2.5",
    "price": 109.0,
    "description": "3D NAND flash are applied to deliver high transfer speeds Remarkable transfer speeds that enable faster bootup and improved overall system performance. The advanced SLC Cache Technology allows performance boost and longer lifespan 7mm slim design suitable for Ultrabooks and Ultra-slim notebooks. Supports TRIM command, Garbage Collection technology, RAID, and ECC (Error Checking & Correction) to provide the optimized performance and enhanced reliability.",
    "category": "electronics",
    "image": "https://fakestoreapi.com/img/71kWymZ+c+L._AC_SX679_t.png",
    "rating": {
      "rate": 4.8,
      "count": 319
    }
  },
  {
    "id": 12,
    "title": "WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive",
    "price": 114.0,
    "description": "Expand your PS4 gaming experience, Play anywhere Fast and easy, setup Sleek design with high capacity, 3-year manufacturer's limited warranty",
    "category": "electronics",
    "image": "https://fakestoreapi.com/img/61mtL65D4cL._AC_SX679_t.png",
    "rating": {
      "rate": 4.8,
      "count": 400
    }
  },
  {
    "id": 13,
    "title": "Acer SB220Q bi 21.5 inches Full HD (1920 x 1080) IPS Ultra-Thin",
    "price": 599.0,
    "description": "21. 5 inches Full HD (1920 x 1080) widescreen IPS display And Radeon free Sync technology. No compatibility for VESA Mount Refresh Rate: 75Hz - Using HDMI port Zero-frame design | ultra-thin | 4ms response time | IPS panel Aspect ratio - 16: 9. Color Supported - 16. 7 million colors. Brightness - 250 nit Tilt angle -5 degree to 15 degree. Horizontal viewing angle-178 degree. Vertical viewing angle-178 degree 75 hertz",
    "category": "electronics",
    "image": "https://fakestoreapi.com/img/81QpkIctqPL._AC_SX679_t.png",
    "rating": {
      "rate": 2.9,
      "count": 250
    }
  },
  {
    "id": 14,
    "title": "Samsung 49-Inch CHG90 144Hz Curved Gaming Monitor (LC49HG90DMNXZA) – Super Ultrawide Screen QLED ",
    "price": 999.99,
    "description": "49 INCH SUPER ULTRAWIDE 32:9 CURVED GAMING MONITOR with dual 27 inch screen side by side QUANTUM DOT (QLED) TECHNOLOGY, HDR support and factory calibration provides stunningly realistic and accurate color and contrast 144HZ HIGH REFRESH RATE and 1ms ultra fast response time work to eliminate motion blur, ghosting, and reduce input lag",
    "category": "electronics",
    "image": "https://fakestoreapi.com/img/81Zt42ioCgL._AC_SX679_t.png",
    "rating": {
      "rate": 2.2,
      "count": 140
    }
  },
  {
    "id": 15,
    "title": "BIYLACLESEN Women's 3-in-1 Snowboard Jacket Winter Coats",
    "price": 56.99,
    "description": "Note:The Jackets is US standard size, Please choose size as your usual wear Material: 100% Polyester; Detachable Liner Fabric: Warm Fleece. Detachable Functional Liner: Skin Friendly, Lightweigt and Warm.Stand Collar Liner jacket, keep you warm in cold weather. Zippered Pockets: 2 Zippered Hand Pockets, 2 Zippered Pockets on Chest (enough to keep cards or keys)and 1 Hidden Pocket Inside.Zippered Hand Pockets and Hidden Pocket keep your things secure. Humanized Design: Adjustable and Detachable Hood and Adjustable cuff to prevent the wind and water,for a comfortable fit. 3 in 1 Detachable Design provide more convenience, you can separate the coat and inner as needed, or wear it together. It is suitable for different season and help you adapt to different climates",
    "category": "women's clothing",
    "image": "https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_t.png",
    "rating": {
      "rate": 2.6,
      "count": 235
    }
  },
  {
    "id": 16,
    "title": "Lock and Love Women's Removable Hooded Faux Leather Moto Biker Jacket",
    "price": 29.95,
    "description": "100% POLYURETHANE(shell) 100% POLYESTER(lining) 75% POLYESTER 25% COTTON (SWEATER), Faux leather material for style and comfort / 2 pockets of front, 2-For-One Hooded denim style faux leather jacket, Button detail on waist / Detail stitching at sides, HAND WASH ONLY / DO NOT BLEACH / LINE DRY / DO NOT IRON",
    "category": "women's clothing",
    "image": "https://fakestoreapi.com/img/81XH0e8fefL._AC_UY879_t.png",
    "rating": {
      "rate": 2.9,
      "count": 340
    }
  },
  {
    "id": 17,
    "title": "Rain Jacket Women Windbreaker Striped Climbing Raincoats",
    "price": 39.99,
    "description": "Lightweight perfet for trip or casual wear---Long sleeve with hooded, adjustable drawstring waist design. Button and zipper front closure raincoat, fully stripes Lined and The Raincoat has 2 side pockets are a good size to hold all kinds of things, it covers the hips, and the hood is generous but doesn't overdo it.Attached Cotton Lined Hood with Adjustable Drawstrings give it a real styled look.",
    "category": "women's clothing",
    "image": "https://fakestoreapi.com/img/71HblAHs5xL._AC_UY879_-2t.png",
    "rating": {
      "rate": 3.8,
      "count": 679
    }
  },
  {
    "id": 18,
    "title": "MBJ Women's Solid Short Sleeve Boat Neck V ",
    "price": 9.85,
    "description": "95% RAYON 5% SPANDEX, Made in USA or Imported, Do Not Bleach, Lightweight fabric with great stretch for comfort, Ribbed on sleeves and neckline / Double stitching on bottom hem",
    "category": "women's clothing",
    "image": "https://fakestoreapi.com/img/71z3kpMAYsL._AC_UY879_t.png",
    "rating": {
      "rate": 4.7,
      "count": 130
    }
  },
  {
    "id": 19,
    "title": "Opna Women's Short Sleeve Moisture",
    "price": 7.95,
    "description": "100% Polyester, Machine wash, 100% cationic polyester interlock, Machine Wash & Pre Shrunk for a Great Fit, Lightweight, roomy and highly breathable with moisture wicking fabric which helps to keep moisture away, Soft Lightweight Fabric with comfortable V-neck collar and a slimmer fit, delivers a sleek, more feminine silhouette and Added Comfort",
    "category": "women's clothing",
    "image": "https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_t.png",
    "rating": {
      "rate": 4.5,
      "count": 146
    }
  },
  {
    "id": 20,
    "title": "DANVOUY Womens T Shirt Casual Cotton Short",
    "price": 12.99,
    "description": "95%Cotton,5%Spandex, Features: Casual, Short Sleeve, Letter Print,V-Neck,Fashion Tees, The fabric is soft and has some stretch., Occasion: Casual/Office/Beach/School/Home/Street. Season: Spring,Summer,Autumn,Winter.",
    "category": "women's clothing",
    "image": "https://fakestoreapi.com/img/61pHAEJ4NML._AC_UX679_t.png",
    "rating": {
      "rate": 3.6,
      "count": 145
    }
  }
]

# Categories Store
CATEGORIES = [
    {
        "id": 1,
        "name": "men's clothing",
        "slug": "mens-clothing",
        "icon": "fa-solid fa-shirt",
        "description": "Premium apparel and casual essentials tailored for men."
    },
    {
        "id": 2,
        "name": "women's clothing",
        "slug": "womens-clothing",
        "icon": "fa-solid fa-vest-patches",
        "description": "Contemporary and classic fashion choices for women."
    },
    {
        "id": 3,
        "name": "jewelery",
        "slug": "jewelery",
        "icon": "fa-solid fa-gem",
        "description": "Luxury bracelets, rings, and handcrafted accessories."
    },
    {
        "id": 4,
        "name": "electronics",
        "slug": "electronics",
        "icon": "fa-solid fa-laptop",
        "description": "Next-generation gadgets, storage drives, and high-res displays."
    }
]

# Users Store
USERS = [
    {
        "id": 1,
        "name": "Alex Morgan",
        "email": "admin@vaii.store",
        "role": "Super Admin",
        "status": "Active",
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150&auto=format&fit=crop&q=80",
        "joined_date": "2024-01-15",
        "orders_count": 18
    },
    {
        "id": 2,
        "name": "David Chen",
        "email": "david.chen@vaii.store",
        "role": "Product Manager",
        "status": "Active",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&auto=format&fit=crop&q=80",
        "joined_date": "2024-02-10",
        "orders_count": 5
    },
    {
        "id": 3,
        "name": "Sophia Bennett",
        "email": "sophia.b@gmail.com",
        "role": "Customer",
        "status": "Active",
        "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=150&auto=format&fit=crop&q=80",
        "joined_date": "2024-03-01",
        "orders_count": 12
    },
    {
        "id": 4,
        "name": "Marcus Wright",
        "email": "marcus.w@yahoo.com",
        "role": "Customer",
        "status": "Active",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&auto=format&fit=crop&q=80",
        "joined_date": "2024-03-22",
        "orders_count": 4
    },
    {
        "id": 5,
        "name": "Emma Watson",
        "email": "emma.tech@outlook.com",
        "role": "Customer",
        "status": "Inactive",
        "avatar": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&auto=format&fit=crop&q=80",
        "joined_date": "2024-04-05",
        "orders_count": 1
    }
]

# Recent Orders for Dashboard
RECENT_ORDERS = [
    {
        "id": "ORD-9482",
        "customer": "Sophia Bennett",
        "email": "sophia.b@gmail.com",
        "total": 349.95,
        "status": "Delivered",
        "date": "Today, 14:23",
        "items_count": 3
    },
    {
        "id": "ORD-9481",
        "customer": "Marcus Wright",
        "email": "marcus.w@yahoo.com",
        "total": 109.95,
        "status": "Processing",
        "date": "Today, 11:05",
        "items_count": 1
    },
    {
        "id": "ORD-9480",
        "customer": "Liam Johnson",
        "email": "liam.j@gmail.com",
        "total": 1248.99,
        "status": "Shipped",
        "date": "Yesterday",
        "items_count": 4
    },
    {
        "id": "ORD-9479",
        "customer": "Olivia Taylor",
        "email": "olivia.t@live.com",
        "total": 85.90,
        "status": "Delivered",
        "date": "2 days ago",
        "items_count": 2
    },
    {
        "id": "ORD-9478",
        "customer": "Noah Williams",
        "email": "noah.w@icloud.com",
        "total": 599.00,
        "status": "Cancelled",
        "date": "3 days ago",
        "items_count": 1
    }
]

# ----------------- Product Helpers ----------------- #

def get_all_products():
    return PRODUCTS

def get_product_title(title):
    for product in PRODUCTS:
        if (product['title']).strip() == str(title).strip():
            return product
    return None

def get_product_category(category):
    result = []
    for product in PRODUCTS:
        if (product['category']).strip() == str(category).strip():
            result.append(product)
    return result

def get_product_id(product_id):
    for product in PRODUCTS:
        if str(product['id']) == str(product_id):
            return product
    return None

def create_product(title, price, description, category, image="", rate=5.0, count=1):
    new_id = max([p['id'] for p in PRODUCTS], default=0) + 1
    if not image or not image.strip():
        image = "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop&q=80"
    
    new_product = {
        "id": new_id,
        "title": title.strip(),
        "price": float(price),
        "description": description.strip(),
        "category": category.strip(),
        "image": image.strip(),
        "rating": {
            "rate": float(rate),
            "count": int(count)
        }
    }
    PRODUCTS.insert(0, new_product)
    return new_product

def update_product(product_id, title, price, description, category, image=""):
    product = get_product_id(product_id)
    if product:
        product['title'] = title.strip()
        product['price'] = float(price)
        product['description'] = description.strip()
        product['category'] = category.strip()
        if image and image.strip():
            product['image'] = image.strip()
        return product
    return None

def delete_product(product_id):
    global PRODUCTS
    product = get_product_id(product_id)
    if product:
        PRODUCTS = [p for p in PRODUCTS if str(p['id']) != str(product_id)]
        return True
    return False


# ----------------- Category Helpers ----------------- #

def get_all_categories():
    categories_data = []
    for cat in CATEGORIES:
        product_count = len([p for p in PRODUCTS if p['category'].strip().lower() == cat['name'].strip().lower()])
        categories_data.append({
            **cat,
            "product_count": product_count
        })
    return categories_data

def get_category_by_id(cat_id):
    for cat in CATEGORIES:
        if str(cat['id']) == str(cat_id):
            return cat
    return None

def get_category_by_name(name):
    for cat in CATEGORIES:
        if cat['name'].strip().lower() == str(name).strip().lower():
            return cat
    return None

def create_category(name, description="", icon="fa-solid fa-tag"):
    new_id = max([c['id'] for c in CATEGORIES], default=0) + 1
    slug = name.strip().lower().replace(" ", "-").replace("'", "")
    new_category = {
        "id": new_id,
        "name": name.strip(),
        "slug": slug,
        "icon": icon.strip() if icon else "fa-solid fa-tag",
        "description": description.strip()
    }
    CATEGORIES.append(new_category)
    return new_category

def update_category(cat_id, name, description="", icon=""):
    category = get_category_by_id(cat_id)
    if category:
        old_name = category['name']
        category['name'] = name.strip()
        category['slug'] = name.strip().lower().replace(" ", "-").replace("'", "")
        category['description'] = description.strip()
        if icon and icon.strip():
            category['icon'] = icon.strip()
        # update products using old category name
        for p in PRODUCTS:
            if p['category'].strip().lower() == old_name.strip().lower():
                p['category'] = category['name']
        return category
    return None

def delete_category(cat_id):
    global CATEGORIES
    category = get_category_by_id(cat_id)
    if category:
        CATEGORIES = [c for c in CATEGORIES if str(c['id']) != str(cat_id)]
        return True
    return False


# ----------------- User Helpers ----------------- #

def get_all_users():
    return USERS

def get_user_by_id(user_id):
    for u in USERS:
        if str(u['id']) == str(user_id):
            return u
    return None

def create_user(name, email, role="Customer", status="Active", avatar=""):
    new_id = max([u['id'] for u in USERS], default=0) + 1
    if not avatar or not avatar.strip():
        avatar = f"https://api.dicebear.com/7.x/avataaars/svg?seed={name.replace(' ', '')}"
    new_user = {
        "id": new_id,
        "name": name.strip(),
        "email": email.strip(),
        "role": role,
        "status": status,
        "avatar": avatar,
        "joined_date": datetime.now().strftime("%Y-%m-%d"),
        "orders_count": 0
    }
    USERS.insert(0, new_user)
    return new_user

def update_user(user_id, name, email, role="Customer", status="Active", avatar=""):
    user = get_user_by_id(user_id)
    if user:
        user['name'] = name.strip()
        user['email'] = email.strip()
        user['role'] = role
        user['status'] = status
        if avatar and avatar.strip():
            user['avatar'] = avatar.strip()
        return user
    return None

def delete_user(user_id):
    global USERS
    user = get_user_by_id(user_id)
    if user:
        USERS = [u for u in USERS if str(u['id']) != str(user_id)]
        return True
    return False

def toggle_user_status(user_id):
    user = get_user_by_id(user_id)
    if user:
        user['status'] = "Inactive" if user['status'] == "Active" else "Active"
        return user
    return None


# ----------------- Dashboard Stats ----------------- #

def get_dashboard_stats():
    total_products = len(PRODUCTS)
    total_categories = len(CATEGORIES)
    total_users = len(USERS)
    total_revenue = sum([p['price'] * 3.5 for p in PRODUCTS]) + 14250.00
    
    # Category sales distribution
    category_counts = {}
    for p in PRODUCTS:
        cat = p['category']
        category_counts[cat] = category_counts.get(cat, 0) + 1
        
    return {
        "total_revenue": round(total_revenue, 2),
        "total_products": total_products,
        "total_categories": total_categories,
        "total_users": total_users,
        "total_orders": 128,
        "recent_orders": RECENT_ORDERS,
        "category_counts": category_counts
    }

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from config import Config
from database.db import init_db, db
from database.models import Post
from agents.writer import generate_post
from agents.image_agent import process_image_request
from agents.linkedin_agent import publish_content
from agents.chat_agent import process_chat_instruction

app = Flask(__name__)
app.config.from_object(Config)
init_db(app)

# Basic authentication verification
def is_logged_in():
    return session.get('logged_in') == True

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Hardcoded for personal use. Aap isay badal saktay hain.
        if username == 'admin' and password == 'admin123':
            session['logged_in'] = True
            return redirect(url_for('index'))
        return "Invalid Credentials", 401
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    if not is_logged_in():
        return redirect(url_for('login'))
        
    post = Post.query.order_by(Post.id.desc()).first()
    return render_template('index.html', post=post)

@app.route('/api/generate', methods=['POST'])
def generate():
    if not is_logged_in(): return jsonify({'success': False, 'error': 'Unauthorized'}), 401
    
    data = request.json
    topic = data.get('topic', 'Computer Vision technical updates')
    
    content = generate_post(topic)
    img_url = process_image_request(topic)
    
    new_post = Post(topic=topic, content=content, image_url=img_url)
    db.session.add(new_post)
    db.session.commit()
    
    return jsonify({'success': True})

@app.route('/api/action', methods=['POST'])
def action():
    if not is_logged_in(): return jsonify({'success': False}), 401
    
    data = request.json
    post_id = data.get('id')
    action_type = data.get('action')
    
    post = Post.query.get(post_id)
    if post:
        post.status = action_type
        if action_type == 'approve':
            success = publish_content(post.content, post.image_url)
            if success:
                post.status = 'posted'
        db.session.commit()
        return jsonify({'success': True, 'status': post.status})
    return jsonify({'success': False})

@app.route('/api/chat', methods=['POST'])
def chat():
    if not is_logged_in(): return jsonify({'success': False}), 401
    
    data = request.json
    instruction = data.get('instruction')
    current_draft = data.get('current_draft')
    
    new_draft = process_chat_instruction(current_draft, instruction)
    
    # Update latest post in DB
    post = Post.query.order_by(Post.id.desc()).first()
    if post:
        post.content = new_draft
        db.session.commit()
        
    return jsonify({'success': True, 'new_draft': new_draft})

@app.route('/privacy-policy.html')
def privacy():
    return render_template('privacy-policy.html')

@app.route('/terms.html')
def terms():
    return render_template('terms.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response
from flask_login import login_required, current_user
from . import main
from .. import db
from ..models import Permission, Role, User, Post, Comment,Contact
from ..decorators import admin_required, permission_required
from .forms import ContactForm
from ..email import send_email



@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == "POST":
        contact = Contact(name=form.name.data,email=form.email.data,
                subject=form.subject.data,message=form.message.data)
        db.session.add(contact)
        db.session.commit()
        send_email(contact.email, 'Thank you for contacting us',
                   'mail/contact',contact=contact)
        flash('Thanks for reaching out.')
    return render_template('contact.html',form=form)

@main.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    return render_template('portfolio.html')



@main.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@main.route('/blog', methods=['GET', 'POST'])
def blog():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['CREATIVE_POSTS_PER_PAGE'],
        error_out=False)
    posts = pagination.items    
    return render_template('blog.html', posts=posts,
            pagination=pagination)


@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', posts=[post])



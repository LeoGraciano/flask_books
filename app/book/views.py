from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user

from app import db
from app.forms import BookForm, UserBookForm
from app.models import Book

from . import book


@book.route('/book')
def book_list():
    context = {
        'form': BookForm()
    }
    return render_template('book/list.html', **context)


@book.route('/book/add', methods=['POST', 'GET'])
def book_add():
    form = BookForm()

    if form.validate_on_submit():
        book = Book()
        book.name = form.name.data
        db.session.add(book)
        db.session.commit()

        flash('Livro cadastrado com sucesso.', 'success')

        return redirect(url_for('.book_add'))

    context = {
        'form': form
    }

    return render_template('book/add.html', **context)


@book.route('/user/<int:id>/book/add', methods=['POST', 'GET'])
def user_add_book(id):
    template_name = 'book/user_add_book.html'
    form = UserBookForm()

    if form.validate_on_submit():
        book = Book.query.get(form.book.data)
        current_user.books.append(book)

        db.session.add(current_user)
        db.session.commit()

        flash('Livro cadastrado com sucesso.', 'success')

        return redirect(url_for('account.detail_user', id=current_user.id))

    context = {
        'form': form
    }

    return render_template(template_name, **context)

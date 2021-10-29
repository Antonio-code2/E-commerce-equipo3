from os import error
from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError
from flask_sqlalchemy import SQLAlchemy

from app import db

class productos(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Usuarios.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    precio = db.Column(db.String, nullable=False)
    title_slug = db.Column(db.String(256), unique=True, nullable=False)
    descripcion = db.Column(db.Text)
    image_name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<productos {self.title}>'

    def save(self):
        if not self.id_producto:
            db.session.add(self)
        if not self.title_slug:
            self.title_slug = slugify(self.title)

        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1
                self.title_slug = f'{self.title_slug}-{count}'

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return productos.query.get(id)

        

    @staticmethod
    def get_by_slug(slug):
        return productos.query.filter_by(title_slug=slug).first()

    #@staticmethod
    #def get_all():
    #   return productos.query.all() 

    # @staticmethod
    # def all_paginated(page=1, per_page=20):
    #     return productos.query.order_by(productos.created.asc()).\
    #     paginate(page=page, per_page=per_page, error_out=False)

        
        
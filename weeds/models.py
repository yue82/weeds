# -*- coding: utf-8 -*-
from weeds import db


class LearnRecord(db.Model):
    __tablename__ = 'learnrecord'
    date = db.Column(db.Date, primary_key=True)
    tlen = db.Column(db.Integer)

    def __repr__(self):
        return '<LearnRecord date={date} tlen={tlen!r}>'.format(
            date=self.date, tlen=self.tlen)

def init():
    db.create_all()

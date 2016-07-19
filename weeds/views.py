# -*- coding: utf-8 -*-
from flask import request, redirect, url_for, render_template, flash
from weeds import app, db
from weeds.models import LearnRecord
from datetime import date

@app.route('/')
def show_weeds():
    records = LearnRecord.query.order_by(LearnRecord.date.asc()).all()
    return render_template('show_weeds.html', records=records)


@app.route('/add', methods=['POST'])
def add_record():
    y = int(request.form['year'])
    m = int(request.form['month'])
    d = int(request.form['day'])
    record = LearnRecord(
        date = date(y, m, d),
        tlen = int(request.form['tlen']))
    db.session.add(record)
    db.session.commit()
    flash('New learning record was successfully posted')
    return redirect(url_for('show_weeds'))

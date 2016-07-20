# -*- coding: utf-8 -*-
from flask import request, redirect, url_for, render_template, flash
from weeds import app, db
from weeds.models import LearnRecord
from datetime import date, timedelta
import random

@app.route('/')
def show_weeds():
    records = LearnRecord.query.order_by(LearnRecord.date.asc()).all()
    return render_template('show_weeds.html', records=records)


@app.route('/reset')
def reset_weeds():
    today = date.today()
    day = today - timedelta(15*7)
    while day != today:
        if not LearnRecord.query.get(day):
            t = random.randint(0, 24)
            if t == 0:
                r, g, b = 220, 220, 220
            else:
                r, g, b = 0, int(t/24.0*128)+128, 0
            record = LearnRecord(date=day, tlen=t, r=r, g=g, b=b)
            db.session.add(record)
            db.session.commit()
        day += timedelta(1)
    flash('learning record was successfully reseted')
    return redirect(url_for('show_weeds'))


@app.route('/add', methods=['POST'])
def add_record():
    y = int(request.form['year'])
    m = int(request.form['month'])
    d = int(request.form['day'])
    tlen = int(request.form['tlen'])
    if tlen == 0:
        r, g, b = 220, 220, 220
    else:
        r, g, b = 0, int(t/24.0*128)+128, 0
    print r, g, b
    record = LearnRecord(
        date = date(y, m, d),
        tlen=tlen, r=r, g=g, b=b)
    db.session.add(record)
    db.session.commit()
    flash('New learning record was successfully posted')
    return redirect(url_for('show_weeds'))

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 12:02:51 2020

@author: hp
"""

from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file

app = Flask(__name__)

import rds_db as db
intervals = [(0,1000,"Northern Territory","Brisbane"),(1001,1999,"New South Wales","Sydney"),(2000,2999,"New South Wales","Sydney"),(3000,3999,"Victoria","Melbourne"),(4000,4999,"Queensland","Sydney"),(5000,5999,"South Australia","Melbourne"),(6000,6999,"Western Australia","Melbourne"),(7000,7999,"Tasmania","Melbourne"),(8000,8999,"Victoria","Melbourne"),(9000,9999,"Queensland","Brisbane")]
@app.route('/', methods=['GET', 'POST'])
def assignment():
	if request.method == 'GET':
		return render_template('task.html')
	elif request.method == 'POST':
        try:
            pincode = request.form['postal_code']
            for interval in intervals:
                left, right, city, office= interval
                if left<=int(pincode)<=right:
                    return "For customers in "+city+", closest office is in "+office
        except Exception as e:
            return "Please enter the correct pincode"
        db.insert_details(pincode,city,office)
        details = db.get_details()
        print(details)
        for detail in details:
            var = detail
        return render_template('index.html',var=var)



if __name__ == "__main__":
    
    app.run(debug=True)

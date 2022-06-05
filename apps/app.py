from flask import Flask, render_template, session, request, redirect, url_for
from model.models import Users, Cars, ApplicationTos


app = Flask(__name__)
app.secret_key = 'super secret key'


@app.route('/', methods=['GET', "POST"])
def index():
    global user

    data = Cars.select()

    # Форма входа 
    if request.method == "POST" and request.form.get('username') and request.form.get('password'):
        login = request.form.get('username')
        password = request.form.get('password')
        for row in Users.select().where(Users.login == login):
            if row.password == password:
                session['login'] = row.login

    # Форма добавления 
    if request.method == "POST":
        name = request.form.get('mark')
        model_car = request.form.get('model')
        year_car = request.form.get('year')
        volume_engine = request.form.get('volume')
        # Добавление записи
        try:
            car = Cars()
            car.name = name
            car.model_car = model_car
            car.year_car = year_car
            car.volume_engine = float(volume_engine)
            car.save()
        except TypeError:
            pass

    # Форма обновления 
    if request.method == "POST" and request.form.get('update_mark'):
        print('update')
        car_id = request.form.get('car_id')
        update_name = request.form.get('update_mark')
        update_model_car = request.form.get('update_model')
        update_year_car = request.form.get('update_year')
        update_volume_engine = request.form.get('update_volume')
        # Обновление макри
        update_car = Cars.update(name=update_name).where(Cars.car_id==int(car_id))
        update_car.execute()
        # Обновление модели
        update_car = Cars.update(model_car=update_model_car).where(Cars.car_id==int(car_id))
        update_car.execute()
        # Обновление года
        update_car = Cars.update(year_car=update_year_car).where(Cars.car_id==int(car_id))
        update_car.execute()
        # Обновление объёма двигателя
        update_car = Cars.update(volume_engine=float(update_volume_engine)).where(Cars.car_id==int(car_id))
        update_car.execute()

    return render_template('index.html', data=data)


@app.route('/delete/<int:id>', methods=['GET', "POST"])
def delete(id):
    query = Cars.delete().where(Cars.car_id == id)
    query.execute()
    return redirect(url_for('index'))


app.run()

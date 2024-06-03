from datetime import datetime, timedelta
from flask import Flask, jsonify
import random
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def nu_generate(minValue, maxValue):
    return random.randint(minValue, maxValue)


def moon_generate(minValue, maxValue):
    moon = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım",
            "Aralık"]
    data = {}
    for i in moon:
        data[i] = nu_generate(minValue, maxValue)
    return data


def day_generate(minValue, maxValue):
    day = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]
    data = {}
    for i in day:
        data[i] = nu_generate(minValue, maxValue)
    return data


def department_generate():
    department = ["Çağrı Karşılayıcı", "Sağlık", "Emniyet", "Jandarma", "İtfaiye", "Orman", "AFAD"]
    data = {}
    for i in department:
        data1 = nu_generate(10000, 90000)
        data2 = nu_generate(1000, 90000)
        data3 = nu_generate(0, 100)
        data[i] = [data1, data2, data3, data3]
    return data


def generate_random_date():
    start = '01.01.2024'
    end = '01.01.2026'

    start_time = time.mktime(time.strptime(start, '%d.%m.%Y'))
    end_time = time.mktime(time.strptime(end, '%d.%m.%Y'))
    random_time = start_time + random.random() * (end_time - start_time)
    random_date = datetime.fromtimestamp(random_time)
    # end_date = random_date + timedelta(days=days_to_add)
    # return random_date.strftime('%d.%m.%Y'), end_date.strftime('%d.%m.%Y')
    return random_date


def generate_random_time():
    random_date = generate_random_date()
    random_hour = random.randint(8, 16)
    random_minute = random.randint(0, 59)
    random_date = random_date.replace(hour=random_hour, minute=random_minute, second=0)
    return random_date


def generate_random_datetime():
    random_date = generate_random_date()

    random_duration_minutes = random.randint(15, 180)
    return random_date + timedelta(minutes=random_duration_minutes)

    # return new_date.strftime('%d.%m.%Y %H:%M')


def staff_generate():
    staff_data = []
    for _ in range(1, 14):
        day_off_info = []
        worked_staff_name = 'Staff ' + str(random.randint(100, 299))
        work_start = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(time.time()))
        work_finish = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(time.time()))
        day_off_info.append((work_start, work_finish))
        data = {
            "staff_name": worked_staff_name,
            "working_time": day_off_info,
            "work_rate": nu_generate(0, 100)
        }
        staff_data.append(data)
    return staff_data


def generate_dashboard_dummy_statistic():
    data = {
        "carts_data": {
            "listen_total": nu_generate(500, 35000),
            "total_rate_compared": nu_generate(-100, 100),
            "listen_duration": nu_generate(20, 3000),
            "duration_rate_compared": nu_generate(-100, 100),
            "call_total": nu_generate(10000, 900000),
            "call_rate_compared": nu_generate(-100, 100),
            "working_staff": nu_generate(1, 14),
            "day_off_staff": nu_generate(0, 5),
            "listen_days": day_generate(20, 3000),
            "call_months": moon_generate(50000, 900000),
            "call_listen_rate": moon_generate(0, 100),
        },
        "daily_department_data": department_generate(),
        "daily_staff_data": staff_generate(),
    }
    yield data


def generate_staff_dummy_statistic():
    staff_data = staff_generate()

    for staff in staff_data:
        start_date = generate_random_date()
        duration_days_off = nu_generate(0, 12)
        finish_date = start_date + timedelta(days=duration_days_off)

        start_leave = generate_random_datetime()
        duration_leave = nu_generate(15, 180)
        finish_leave = start_leave + timedelta(minutes=duration_leave)

        data = {
            "staff_name": staff["staff_name"],
            "phone": "05" + str(nu_generate(300000000, 499999999)),
            "address": random.choices(["Keçiören", "Çankaya", "Yenimahalle", "Altındağ", "Mamak"]),
            "title": random.choices(["Memur", "Görevlendirme", "İşçi"]),
            "moon_statistics": {
                "work_day": moon_generate(0, 22),
                "listening_call_quantity": moon_generate(200, 9000),
                "listening_call_duration": moon_generate(50, 5000),
                "performance_quantity": moon_generate(0, 100),
                "performance_duration": moon_generate(0, 100),
            },
            "leave_info": {
                "annual_leave": {
                    "day_off_start": start_date,
                    "day_off_finish": finish_date,
                    "day_off_duration": duration_days_off,
                },
                "short_term_leave": {
                    "start_leave": start_date,
                    "duration_leave": duration_leave,
                    "finish_leave": finish_leave
                }
            }
        }
        yield data


def generate_called_list():
    staff_name = 'Staff ' + str(random.randint(100, 299))
    called_nu = "0" + str(random.randint(5300000000, 5499999999))
    call_time = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(time.time()))
    duration = nu_generate(0, 100)
    return (staff_name, called_nu, call_time, duration)


def generate_dummy_called_list():
    data =[]
    for i in range(1, 1000):
        record = {
            'id': i,
            'staff_name': generate_called_list()[0],
            'called_nu': generate_called_list()[1],
            'call_time': generate_called_list()[2],
            'duration': generate_called_list()[3]
        }
        data.append(record)
    return data


@app.route("/dummy-dashboard-statistics", methods=['GET'])
def get_dummy_dashboard_statistics():
    dummy_data = list(generate_dashboard_dummy_statistic())
    return jsonify(dummy_data)


@app.route("/dummy-staff-statistics", methods=['GET'])
def get_dummy_staff_statistics():
    dummy_data = list(generate_staff_dummy_statistic())
    return jsonify(dummy_data)


@app.route("/dummy-called-list", methods=['GET'])
def get_dummy_called_list():
    dummy_data = list(generate_dummy_called_list())
    return jsonify(dummy_data)


if __name__ == '__main__':

    while True:
        app.run(debug=True, host='0.0.0.0')
        time.sleep(1)

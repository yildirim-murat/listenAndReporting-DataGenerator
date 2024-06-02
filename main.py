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
        data2 = nu_generate(10, 1000)
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


@app.route("/dummy-dashboard-statistics", methods=['GET'])
def get_dummy_dashboard_statistics():
    dummy_data = list(generate_dashboard_dummy_statistic())
    return jsonify(dummy_data)


@app.route("/dummy-staff-statistics", methods=['GET'])
def get_dummy_staff_statistics():
    dummy_data = list(generate_staff_dummy_statistic())
    return jsonify(dummy_data)


#
#
# def generate_dummy_staff_statistic():
#     staff_name = "Staff One"
#
#     data = {
#         "staff_information": {
#             "name": staff_name,
#             "phone": "05" + nu_generate(300000000, 499999999),
#             "address": random.choices["Keçiören", "Çankaya", "Yenimahalle", "Altındağ", "Mamak"],
#             "title": random.choices["Memur", "Görevlendirme", "İşçi"],
#         },
#         "work_information": {
#             "moon": {
#                 "Ocak": nu_generate(0, 22),
#             }
#         }
#
#     }
#     yield data
#
#
# @app.route("/dummy-staff-statistic", methods=['GET'])
# def get_dummy_staff_statistic():
#     dummy_staff_statistic = list(generate_dummy_staff_statistic())
#     return jsonify(dummy_staff_statistic)
#
#
# def generate_dummy_data():
#     for _ in range(2000):
#         ucid = ''.join(random.choices('0123456789', k=20))
#         arayan_numara = '05' + ''.join(random.choices('0123456789', k=9))
#         aranan_numara = '03' + ''.join(random.choices('0123456789', k=9))
#         random_nu = ''.join(random.choices('0123456789', k=1))
#         baslangic_zamani = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(time.time()) + int(random_nu)))
#         random_nu = ''.join(random.choices('0123456789', k=3))
#         bitis_zamani = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(time.time()) + int(random_nu)))
#         vdn = ''.join(random.choices('0123456789', k=7))
#         operator = random.choice(["TURKCELL", "VODAFONE", "TURKTELEKOM"])
#         gelen_arama_tipi = random.choice(["Diger", "Simkartli"])
#         sonlandirma_nedeni = random.choice(["Vaka İhbari", "-"])
#         arama_tipi = random.choice(["Gelen Arama", "Giden Arama"])
#         vaka_numarasi = random.choice([str(random.randint(10000000, 99999999)), "-"])
#         dosya_adi = ''.join(random.choices('0123456789', k=8))
#         agent = 'Staff ' + str(random.randint(100, 299))
#         audio_url = random.choice(["https://soundbible.com/mp3/airplane-landing_daniel_simion.mp3",
#                                    "https://soundbible.com/mp3/cartoon-birds-2_daniel-simion.mp3",
#                                    "https://soundbible.com/mp3/bells-tibetan-daniel_simon.mp3",
#                                    "https://soundbible.com/mp3/soundbible-person-whistling-at-girl-daniel_simon.mp3",
#                                    "https://soundbible.com/mp3/analog-watch-alarm_daniel-simion.mp3",
#                                    "https://soundbible.com/mp3/baby-music-box_daniel-simion.mp3"])
#
#         data = {
#             "ucid": ucid,
#             "caller_nu": arayan_numara,
#             "dialled_nu": aranan_numara,
#             "start_time": baslangic_zamani,
#             "finish_time": bitis_zamani,
#             "vdn": vdn,
#             "operator_name": operator,
#             "incoming_call_type": gelen_arama_tipi,
#             "termination_reason": sonlandirma_nedeni,
#             "call_type": arama_tipi,
#             "event_nu": vaka_numarasi,
#             "file_name": dosya_adi,
#             "agent": agent,
#             "audio_url": audio_url
#         }
#         yield data
#
#
# @app.route('/dummy-data', methods=['GET'])
# def get_dummy_data():
#     dummy_data = list(generate_dummy_data())
#     return jsonify(dummy_data)


if __name__ == '__main__':

    while True:
        app.run(debug=True, host='0.0.0.0')
        time.sleep(1)

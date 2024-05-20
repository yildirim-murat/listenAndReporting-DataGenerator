import sys

from flask import Flask, jsonify
import random
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# CORS(app, resources={r"/dummy-data": {"origins": "http://localhost:3000"}})
def generate_dummy_staff_statistic():
    staff_name = "Staff One"
    call_listen_av_1=random.randint(1,1000)
    call_listen_av_2=random.randint(1,1000)
    call_listen_av_3=random.randint(1,1000)
    call_listen_av_4=random.randint(1,1000)
    call_listen_av_5=random.randint(1,1000)
    call_listen_av_6=random.randint(1,1000)
    call_listen_av_7=random.randint(1,1000)
    call_listen_av_8=random.randint(1,1000)
    call_listen_av_9=random.randint(1,1000)
    call_listen_av_10=random.randint(1,1000)
    call_listen_av_11=random.randint(1,1000)
    call_listen_av_12=random.randint(1,1000)
    call_listen_1=random.randint(1,1000)
    call_listen_2=random.randint(1,1000)
    call_listen_3=random.randint(1,1000)
    call_listen_4=random.randint(1,1000)
    call_listen_5=random.randint(1,1000)
    call_listen_6=random.randint(1,1000)
    call_listen_7=random.randint(1,1000)
    call_listen_8=random.randint(1,1000)
    call_listen_9=random.randint(1,1000)
    call_listen_10=random.randint(1,1000)
    call_listen_11=random.randint(1,1000)
    call_listen_12=random.randint(1,1000)
    call_listen_duration_1=random.randint(1,5000)
    call_listen_duration_2=random.randint(1,5000)
    call_listen_duration_3=random.randint(1,5000)
    call_listen_duration_4=random.randint(1,5000)
    call_listen_duration_5=random.randint(1,5000)
    call_listen_duration_6=random.randint(1,5000)
    call_listen_duration_7=random.randint(1,5000)
    call_listen_duration_8=random.randint(1,5000)
    call_listen_duration_9=random.randint(1,5000)
    call_listen_duration_10=random.randint(1,5000)
    call_listen_duration_11=random.randint(1,5000)
    call_listen_duration_12=random.randint(1,5000)

    data = {
       "staff_name": staff_name,
        "call_listen_av_1": call_listen_av_1,
        "call_listen_av_2": call_listen_av_2,
        "call_listen_av_3": call_listen_av_3,
        "call_listen_av_4": call_listen_av_4,
        "call_listen_av_5": call_listen_av_5,
        "call_listen_av_6": call_listen_av_6,
        "call_listen_av_7": call_listen_av_7,
        "call_listen_av_8": call_listen_av_8,
        "call_listen_av_9": call_listen_av_9,
        "call_listen_av_10": call_listen_av_10,
        "call_listen_av_11": call_listen_av_11,
        "call_listen_av_12": call_listen_av_12,
        "call_listen_1": call_listen_1,
        "call_listen_2": call_listen_2,
        "call_listen_3": call_listen_3,
        "call_listen_4": call_listen_4,
        "call_listen_5": call_listen_5,
        "call_listen_6": call_listen_6,
        "call_listen_7": call_listen_7,
        "call_listen_8": call_listen_8,
        "call_listen_9": call_listen_9,
        "call_listen_10": call_listen_10,
        "call_listen_11": call_listen_11,
        "call_listen_12": call_listen_12,
        "call_listen_duration_1": call_listen_duration_1,
        "call_listen_duration_2": call_listen_duration_2,
        "call_listen_duration_3": call_listen_duration_3,
        "call_listen_duration_4": call_listen_duration_4,
        "call_listen_duration_5": call_listen_duration_5,
        "call_listen_duration_6": call_listen_duration_6,
        "call_listen_duration_7": call_listen_duration_7,
        "call_listen_duration_8": call_listen_duration_8,
        "call_listen_duration_9": call_listen_duration_9,
        "call_listen_duration_10": call_listen_duration_10,
        "call_listen_duration_11": call_listen_duration_11,
        "call_listen_duration_12": call_listen_duration_12,
    }
    yield data


def generate_dummy_statistic():
    max_staff = 14
    staff_array = []
    worked_info = []
    day_off_info = []

    for _ in range(max_staff):
        staff_name = 'Staff ' + str(random.randint(100, 299))
        staff_rate = random.randint(0, 100)
        staff_start = f"{random.randint(8, 14)}:{random.randint(0, 59):02}"
        staff_finish = f"{random.randint(14, 17)}:{random.randint(0, 59):02}"
        staff_array.append((staff_name, staff_start, staff_finish, staff_rate))

    day_off_staff = random.randint(0, max_staff)
    call_karsilayici = random.randint(1000, 100000)
    call_saglik = random.randint(1, 5000)
    call_emniyet = random.randint(1, 5000)
    call_itfaiye = random.randint(1, 5000)
    call_jandarma = random.randint(1, 5000)
    call_orman = random.randint(1, 5000)
    call_afad = random.randint(1, 5000)
    call_rate = random.randint(-100, 100)
    listen_karsilayici = random.randint(1, 5000)
    listen_saglik = random.randint(1, call_saglik)
    listen_emniyet = random.randint(1, call_emniyet)
    listen_jandarma = random.randint(1, call_jandarma)
    listen_itfaiye = random.randint(1, call_itfaiye)
    listen_orman = random.randint(1, call_orman)
    listen_afad = random.randint(1, call_afad)
    listen_rate = random.randint(-100, 100)
    listen_duration = random.randint(1, 2000)
    listen_duration_rate = random.randint(-100, 100)
    listen_1 = random.randint(1, 1500)
    listen_2 = random.randint(1, 1500)
    listen_3 = random.randint(1, 1500)
    listen_4 = random.randint(1, 1500)
    listen_5 = random.randint(1, 1500)
    call_1 = random.randint(1000, 900000)
    call_2 = random.randint(1000, 900000)
    call_3 = random.randint(1000, 900000)
    call_4 = random.randint(1000, 900000)
    call_5 = random.randint(1000, 900000)
    call_6 = random.randint(1000, 900000)
    call_7 = random.randint(1000, 900000)
    call_8 = random.randint(1000, 900000)
    call_9 = random.randint(1000, 900000)
    call_10 = random.randint(1000, 900000)
    call_11 = random.randint(1000, 900000)
    call_12 = random.randint(1000, 900000)
    call_rate_1 = random.randint(-100, 100)
    call_rate_2 = random.randint(-100, 100)
    call_rate_3 = random.randint(-100, 100)
    call_rate_4 = random.randint(-100, 100)
    call_rate_5 = random.randint(-100, 100)
    call_rate_6 = random.randint(-100, 100)
    call_rate_7 = random.randint(-100, 100)
    call_rate_8 = random.randint(-100, 100)
    call_rate_9 = random.randint(-100, 100)
    call_rate_10 = random.randint(-100, 100)
    call_rate_11 = random.randint(-100, 100)
    call_rate_12 = random.randint(-100, 100)
    worked_staff_name = 'Staff ' + str(random.randint(100, 299))
    worked_staff_phone = '05' + str(random.randint(300000000, 399999999))
    worked_staff_address = random.choice(["Yenimahalle", "Keçiören", "Çankaya"])
    worked_staff_title = random.choice(["VHKI", "Görevlendirme", "İşçi"])
    for _ in range(5):
        worked_moon = random.choice(["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"])
        worked_day = random.randint(0, 22)
        worked_listen_quantity = random.randint(100, 1600)
        worked_listen_duration = random.randint(400, 4000)
        worked_listen_quantity_rate = random.randint(-100, 100)
        worked_listen_duration_rate = random.randint(-100, 100)
        worked_info.append((worked_moon, worked_day, worked_listen_quantity, worked_listen_duration,
                            worked_listen_quantity_rate, worked_listen_duration_rate))

    for _ in range(15):
        day_off_type = random.choice(["Yıllık İzin", "Saatlik İzin"])
        day_off_start = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(time.time()))
        day_off_finish = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(time.time()))
        day_off_info.append((day_off_type, day_off_start, day_off_finish))

    data = {
        "max_staff": max_staff,
        "day_off_staff": day_off_staff,
        "staff_name": staff_array,
        "call_karsilayici": call_karsilayici,
        "call_saglik": call_saglik,
        "call_emniyet": call_emniyet,
        "call_jandarma": call_jandarma,
        "call_itfaiye": call_itfaiye,
        "call_orman": call_orman,
        "call_afad": call_afad,
        "call_total": call_karsilayici + call_saglik + call_emniyet + call_jandarma + call_itfaiye + call_orman + call_afad,
        "call_rate": call_rate,
        "listen_karsilayici": listen_karsilayici,
        "listen_saglik": listen_saglik,
        "listen_emniyet": listen_emniyet,
        "listen_jandarma": listen_jandarma,
        "listen_itfaiye": listen_itfaiye,
        "listen_orman": listen_orman,
        "listen_afad": listen_afad,
        "listen_total": listen_karsilayici + listen_saglik + listen_emniyet + listen_jandarma + listen_itfaiye + listen_orman + listen_afad,
        "listen_rate": listen_rate,
        "listen_duration": listen_duration,
        "listen_duration_rate": listen_duration_rate,
        "listen_1": listen_1,
        "listen_2": listen_2,
        "listen_3": listen_3,
        "listen_4": listen_4,
        "listen_5": listen_5,
        "call_1": call_1,
        "call_2": call_2,
        "call_3": call_3,
        "call_4": call_4,
        "call_5": call_5,
        "call_6": call_6,
        "call_7": call_7,
        "call_8": call_8,
        "call_9": call_9,
        "call_10": call_10,
        "call_11": call_11,
        "call_12": call_12,
        "call_rate_1": call_rate_1,
        "call_rate_2": call_rate_2,
        "call_rate_3": call_rate_3,
        "call_rate_4": call_rate_4,
        "call_rate_5": call_rate_5,
        "call_rate_6": call_rate_6,
        "call_rate_7": call_rate_7,
        "call_rate_8": call_rate_8,
        "call_rate_9": call_rate_9,
        "call_rate_10": call_rate_10,
        "call_rate_11": call_rate_11,
        "call_rate_12": call_rate_12,
        "worked_info": worked_info,
        "day_off_info": day_off_info,
        "worked_staff_name": worked_staff_name,
        "worked_staff_phone": worked_staff_phone,
        "worked_staff_address": worked_staff_address,
        "worked_staff_title": worked_staff_title,
    }
    yield data


def generate_dummy_data():
    for _ in range(2000):
        ucid = ''.join(random.choices('0123456789', k=20))
        arayan_numara = '05' + ''.join(random.choices('0123456789', k=9))
        aranan_numara = '03' + ''.join(random.choices('0123456789', k=9))
        random_nu = ''.join(random.choices('0123456789', k=1))
        baslangic_zamani = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(time.time()) + int(random_nu)))
        random_nu = ''.join(random.choices('0123456789', k=3))
        bitis_zamani = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(int(time.time()) + int(random_nu)))
        vdn = ''.join(random.choices('0123456789', k=7))
        operator = random.choice(["TURKCELL", "VODAFONE", "TURKTELEKOM"])
        gelen_arama_tipi = random.choice(["Diger", "Simkartli"])
        sonlandirma_nedeni = random.choice(["Vaka İhbari", "-"])
        arama_tipi = random.choice(["Gelen Arama", "Giden Arama"])
        vaka_numarasi = random.choice([str(random.randint(10000000, 99999999)), "-"])
        dosya_adi = ''.join(random.choices('0123456789', k=8))
        agent = 'Staff ' + str(random.randint(100, 299))
        audio_url = random.choice(["https://soundbible.com/mp3/airplane-landing_daniel_simion.mp3",
                                   "https://soundbible.com/mp3/cartoon-birds-2_daniel-simion.mp3",
                                   "https://soundbible.com/mp3/bells-tibetan-daniel_simon.mp3",
                                   "https://soundbible.com/mp3/soundbible-person-whistling-at-girl-daniel_simon.mp3",
                                   "https://soundbible.com/mp3/analog-watch-alarm_daniel-simion.mp3",
                                   "https://soundbible.com/mp3/baby-music-box_daniel-simion.mp3"])

        data = {
            "ucid": ucid,
            "caller_nu": arayan_numara,
            "dialled_nu": aranan_numara,
            "start_time": baslangic_zamani,
            "finish_time": bitis_zamani,
            "vdn": vdn,
            "operator_name": operator,
            "incoming_call_type": gelen_arama_tipi,
            "termination_reason": sonlandirma_nedeni,
            "call_type": arama_tipi,
            "event_nu": vaka_numarasi,
            "file_name": dosya_adi,
            "agent": agent,
            "audio_url": audio_url
        }
        yield data


@app.route('/dummy-data', methods=['GET'])
def get_dummy_data():
    dummy_data = list(generate_dummy_data())
    return jsonify(dummy_data)


@app.route("/dummy-statistics", methods=['GET'])
def get_dummy_statistics():
    dummy_data = list(generate_dummy_statistic())
    return jsonify(dummy_data)


@app.route("/dummy-staff-statistic", methods=['GET'])
def get_dummy_staff_statistic():
    dummy_staff_statistic = list(generate_dummy_staff_statistic())
    return jsonify(dummy_staff_statistic)


if __name__ == '__main__':

    while True:
        app.run(debug=True, host='0.0.0.0')
        time.sleep(1)

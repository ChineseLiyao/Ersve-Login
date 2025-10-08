from flask import Flask, render_template, session, request , make_response
from flask_session import Session

# app定义
app = Flask(__name__)
# 设置session
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'super secret key'

# 设置session
Session(app)

# 定义主页路由
@app.route('/')
def index():
    if session.get('yijingyouzhanghu') == None:
        session['yijingyouzhanghu'] = "hh"
        return render_template('hy.html')
    else:
        return render_template('index.html')

@app.route('/rw')
def rw():
    return render_template('rw.html')
    
# 定义主路由
@app.route('/Login')
def login():
    response_headers = {
        'Cententd-Header': 'ABABAABAAABABBAAAAAAABBAB ABABAABAAABABBAAAAAAABBAB AABAABAAAABAAABBAABBAABAA ABABAABBABAABBAABAAAABBAA AAAAAAAABBABABBABAAAABBAA ABBBAAAAAABAAABBAAAB',
        'Conversation-Header': 'I=J&U=V'
    }
    return render_template('IndexLogin.html'),200,response_headers

@app.route('/LoginAccept', methods=['POST'])
def accept():
        if request.form.get("pass") == "72fk6fap" and request.form.get("user") == "resu":
            session["Login"] = "user"
            return render_template("userOLED.html")
        elif request.form.get("pass") == "LIYAO LIYAO ERSUE LOGIN ADMIN PASS" and request.form.get("user") == "Liyao":
            session["Login"] = "admin"
            return render_template("Win.html")
        elif request.form.get("pass") == None:
            return render_template("Login.html")
        else:
            return render_template("PassNo.html")


@app.route('/setting.bak')
def Setting_backup():
    return render_template('setting.html')

@app.route('/Renterbak')
def Renter_backup():
    return render_template('Renter.html')

# 登录路由示例
# @app.route('/accept')
# def sessionchaxun():
#     return render_template('Login.html')

# @app.route('/shouquan', methods=['POST'])
# def accept():
#         if request.form.get("password") == "lrx123456":
#             session["XMGLY"] = "YES"
#             return render_template("ysq.html")
#         elif request.form.get("password") == None:
#             return render_template("Login.html")
#         else:
#             return render_template("Not.html")

if __name__ == '__main__':
    app.run(host='::',port=32323)


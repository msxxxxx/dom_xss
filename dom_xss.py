from flask import Flask, render_template, request, redirect, url_for, make_response, abort

app = Flask(__name__)


@app.route("/")
def red():
    return redirect('/login')


@app.route("/login")
def dom_xss():
    return render_template("dom_page.html")


@app.route("/search")
def search():
    if request.cookies.get("role") == "guest":
        return render_template("search.html")
    elif request.cookies.get("role") == "flag123_456":
        return render_template("admin.html")
    else:
        abort(403)


@app.route("/admin")
def dom_adm():
    if request.cookies.get("role") != "flag123_456":
        abort(403)  # нет куки или role != admin
    return render_template("admin.html")  # 200
    #if request.cookies.get("role") != "admin":
    #    resp = make_response(redirect(url_for("dom_adm")))
    #    resp.set_cookie("role", "admin", httponly=True, samesite="Lax")
    #    return resp
    #return render_template("admin.html")
    #resp = make_response(render_template("admin.html"))
    #resp.set_cookie("role", "admin", httponly=True, samesite="Lax")
    #return resp
    #return render_template("admin.html")

@app.route("/guest")
def dom_guest():
    if request.cookies.get("role") != "guest":
        resp = make_response(redirect(url_for("dom_guest")))
        resp.set_cookie("role", "guest")
        return resp
    return redirect('/search')
    #return render_template("search.html")
    #resp = make_response(render_template("guest.html"))
    #resp.set_cookie("role", "guest", httponly=True, samesite="Lax")
    #return resp
    #return render_template("guest.html")


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5002)

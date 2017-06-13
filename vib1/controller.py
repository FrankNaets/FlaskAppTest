from model import InputForm
from flask import Flask, render_template, request
from compute import compute

app = Flask(__name__)

@app.route('/vib1', methods=['GET','POST'])
def index():
	form = InputForm(request.form)
	if request.method == 'POST' and form.validate():
		result_t, result_u = compute(form.A.data, form.b.data, form.w.data, form.T.data)
		#result_t = result_t_f
		#result_u = result_u_f
		#result_t = ["%.2f" % number for number in result_t_f]
		#result_u = ["%.2f" % number for number in result_u_f]
		n = len(result_t)
		#result = result_t_f+result_u_f
	else:
		n = 0
		result_t = None
		result_u = None
	return render_template('view.html', form=form, result_t=result_t, result_u=result_u, n = n)

if __name__ == '__main__':
	app.run(debug=True)

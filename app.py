from flask import Flask, render_template,request,redirect
import pafy
app = Flask(__name__)
URL=""
urls=[]
resolutions=[]
extentions=[]
filesize=[]
final={}
error1="	"
global video
global streams
@app.route("/")
def main():
	return render_template("index.html")
@app.route("/show")
def show_extract():
	return render_template("show_extract.html",final=final ,title = title )
@app.route("/error")
def error():
	return render_template("error.html",error = error1, url = "/")

@app.route("/extract_info",methods=['POST'])
def extract():
	global URL
	URL=request.form['inputURL']
	global video
	try:
		video = pafy.new(URL)
	except Exception as e:
		global error1
		error1 = e
		return redirect('/error')
	
	global streams
	streams=video.streams
	global title
	title = video.title
	global final
	i=0
	for s in streams:
		temp=[]
		temp.append(s.url)
		temp.append(s.resolution)
		temp.append(s.extension)
		temp.append(((s.get_filesize())/1024)/1024)
		final[i] = temp
		i=i+1
	return redirect('/show') 

if __name__ =="__main__":
	
	app.run()

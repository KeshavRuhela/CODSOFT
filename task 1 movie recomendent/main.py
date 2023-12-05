from flask import Flask, render_template,request
import pickle
import pandas as pd
# https://api.themoviedb.org/3/movie/343611?api_key=adc27d079302486236588ffe576d4baf
# api_url = 'https://api.themoviedb.org/3/movie/'+343611+'?api_key=adc27d079302486236588ffe576d4baf'  # Replace this with the actual API URL
movies = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies)  # it create a new table again
similarity = pickle.load(open('similarity.pkl','rb'))
def recommend_process(movie):
    recommend =[]
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda x:x[1])  #enumerate use for not loosing indexes
    for i in distances[1:6]:
        print ("ID : " + str(i[0]))
        recommend.append(movies.iloc[i[0]].title)
    return recommend

app = Flask(__name__)
app.debug = True

@app.route("/")
def main_name():
    return render_template('index.html', movies = movies)

@app.route("/process_data", methods=["POST"])
def process():
    # print(data)
    data1 = request.json.get('data')
    return recommend_process(data1)

if __name__ == "__main__":
    app.run(debug=True)

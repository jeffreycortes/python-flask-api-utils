import io
import urllib
import base64
from src.data.constantes import *
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import urllib
from flask import render_template
from sklearn.decomposition import PCA

class Word2vecAppService:
    def model_text(self, wordItem):
        if(len(wordItem) > 0):
            model = Word2Vec(wordItem, min_count=1)
            words = list(model.wv.vocab)
            print(words)
            #print(model['positivo'])
            model.save(PATH_DATA + 'model_sider_app.bin')
            plot = self.generate_plot(model)
            resp = {"model": words, "plot": plot}
            return resp
        else:
            print('error: words is empty', file=sys.stderr)

    def generate_plot(self, model):
        # fit a 2d PCA model to the vectors
        X = model[model.wv.vocab]
        pca = PCA(n_components=2)
        result = pca.fit_transform(X)
        # create a scatter plot of the projection
        plt.scatter(result[:, 0], result[:, 1])
        words = list(model.wv.vocab)
        for i, word in enumerate(words):
        	plt.annotate(word, xy=(result[i, 0], result[i, 1]))
        plt.xlabel('x')
        plt.xlabel('y')
        plt.title('Mi primera Gráfica en Python 2')
        plt.legend(loc=4)
        #pyplot.show()

        img = io.BytesIO()  # create the buffer
        plt.savefig(img, format='png')  # save figure to the buffer
        img.seek(0)  # rewind your buffer
        plot_data = urllib.parse.quote(base64.b64encode(img.read()).decode()) # base64 encode & URL-escape
        return plot_data #render_template('plot.html', plot_url=plot_data)

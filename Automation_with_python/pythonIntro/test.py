import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()

#print(file_contents)


#def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]
with open("ebook.txt",'r') as f:
    lines = f.readlines()
    #words = lines.split()
    print(lines)
    # LEARNER CODE START HERE
    # word_dict = {}
    # for char in file_contents:
    # print("char is",char)
    # if char.isalpha() and char not in punctuations and char not in uninteresting_words:
    # print("Correct char is",char)
    # if char not in word_dict:
    #    word_dict[char] = 1
    # else:
    #    word_dict[char] += 1
    # print("Word_dict is", word_dict)
    # return word_dict

# calculate_frequencies(file_contents)
# wordcloud
# cloud = wordcloud.WordCloud()
# cloud.generate_from_frequencies()
# return cloud.to_array()

# Display your wordcloud image

#myimage = calculate_frequencies(file_contents)
#plt.imshow(myimage, interpolation = 'nearest')
#plt.axis('off')
#plt.show()
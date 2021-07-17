from wordcloud import WordCloud
import matplotlib.pyplot as plt
import wikipedia
import PySimpleGUI as sg                  

sg.theme('dark grey 9')
layout = [[sg.Text("Word Cloud Generator")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Generate'),  sg.Button('Quit')]]

# Create the window
window = sg.Window('Word Cloud Generator', layout)

while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break    
    elif event == "Generate":

        KeyWord = values['-INPUT-']

        page_result= wikipedia.page(KeyWord)
        Text = page_result.content

        result = WordCloud(width = 800, height = 800,
                    background_color ='white',
                    #stopwords = stopwords,
                    min_font_size = 10).generate(Text)

        plt.imshow(result,interpolation='bilinear')
        plt.axis('off')
        plt.show()

window.close()

def pie_graph():
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('') 
    plt.title("")
    plt.show()

def bar_graph():
    plt.bar(categories, values, color='skyblue', edgecolor='black')
    plt.xlabel('')
    plt.ylabel('')
    plt.title('')

def line_graph():
    plt.line()
    plt.xlabel('')
    plt.ylabel('')
    plt.title('')

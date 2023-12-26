cities = ['Mogadishu', 'bay dabo', 'Hargesa', 'Kismayo']
for city in cities:
    print(city.title().replace(" ","_"))
print("Done!")


print("================================")

# creating Html tags 
items = ['first string', 'second string']
html_str = "<ul>\n" 

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>\n"

print(html_str)
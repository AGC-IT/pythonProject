import json
import webbrowser


with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)


with open('JsonRead.html', 'r') as template_file:
    html_template = template_file.read()


placeholder = '{{json_data}}'


html_content = html_template.replace(placeholder, json.dumps(json_data))


with open('JsonRead.html', 'w') as f:

    f.write(html_content)


webbrowser.open_new_tab('JsonRead.html')

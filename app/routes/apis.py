import markdown
from extensions import application_root_directory
#default will render the readme file
@apis.route('/')
def index():
    #application_root_directory= os.path.abspath(os.path.dirname(__file__))
    with open(application_root_directory+"/README.md", 'r') as home_page:
        # read content of the file
        content=home_page.read()
        #convert markdown into html and return it
        return markdown.markdown(content)
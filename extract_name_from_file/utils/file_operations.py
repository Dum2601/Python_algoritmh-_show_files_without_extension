import os

class Files:
    def __init__(self):

        # Put the dir path below in var ''
        self.directory_path = r''

    def list_files(self):

        if os.path.exists(self.directory_path):

            self.inside_dir = os.listdir(self.directory_path)
            return self.inside_dir
        
        else:

            return 'O diretório não foi encontrado'

    def format_files(self):

        def show_files():

            self.files_in_dir = []            
            self.files_name = self.list_files()

            for name in self.files_name:

                self.files_in_dir.append(name)
            
            return self.files_in_dir
        
        def hide_extension_file():
           
            raw_names = show_files()
            formated = []

            for name in raw_names:
                name_without_ext = os.path.splitext(name)[0] 
                formated.append(name_without_ext)

            return formated

        try:

            return hide_extension_file()  
        
        except Exception as err:

            print('Erro encontrado na função de formatação.\n',
                f'Erro informado: {err}')
            
    @property
    def show_files(self):
        self.format_files = self.format_files()
        return self.format_files






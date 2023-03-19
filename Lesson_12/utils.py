def read_txt(file_path):
    # try:
    with open(file_path, 'r', encoding='utf-8') as file_open:
        contents = file_open.readlines()
    # except FileNotFoundError:
    #     print('File not found')
    #     file_open.close()
    return contents

def write_txt(file_path, contents, mode):
    # try:
    with open(file_path, mode, encoding='utf-8') as file_rw:
        current_content = file_rw.readlines()
        # print(current_content)
        file_rw.writelines(contents)
        return True
    # except:
    #     print('File not written')
    #     return False


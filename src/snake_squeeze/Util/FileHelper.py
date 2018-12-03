class FileHelper(object):

    # Reads the file to the given file path and returns all lines in string array
    @staticmethod
    def read_file(file_path):
        result = []

        if file_path.exists() is False:
            return result

        try:
            with open(str(file_path)) as fp:
                for line in iter(fp.readline, ''):
                    result.append(line)
        finally:
            fp.close()
        return result

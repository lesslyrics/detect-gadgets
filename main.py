import glob
import os

PATH_TO_FOLDER = ""
PATH_TO_INSPECTOR = ""


def locate_jars():
    jars = glob.glob(PATH_TO_FOLDER + '/**/*.jar', recursive=True)

    for jar_path in jars:
        file = open('jars_generated.txt', 'a')
        print(f"{jar_path}", file=file)
        file.close()


def detect_gadgets(jar_path):
    command = f'java -jar {PATH_TO_INSPECTOR} {jar_path}'
    os.system(command)


if __name__ == '__main__':

    locate_jars()

    jars_file = open("jars_generated.txt", "r")  # put paths to your jars in this file
    jars_list = jars_file.read().split("\n")
    jars_file.close()

    print(jars_list)
    for jar in jars_list:
        with open("jars_analyzed.txt", "a") as text_file:  # logs all the jars analysed
            text_file.write(jar + "\n")  # jars with gadgets will be logged in result.txt
        detect_gadgets(jar)

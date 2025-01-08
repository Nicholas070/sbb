def writer():
    #파일을 연다.
    with open("a.text","r") as file:
        text = file.read()
        print(f"{text=}")

    with open("a.text","w+") as file:
        #파일에 값을 적는다
        text = text + input("write something : ")
        file.write(text)


writer()
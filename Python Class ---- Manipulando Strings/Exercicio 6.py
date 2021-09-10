date_nasc = str(input('Digite a data de nasciemento: [00/00/0000] ')).split('/')
meses = ["Unknown",
          "January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]

mes = date_nasc[1]
print("Você nasceu em {} de {} de {}".format(date_nasc[0],meses[int(mes)],date_nasc[2]))


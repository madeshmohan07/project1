def write_log():
    file = open("app.log", "w")
    file.write("Application started successfully\n")
    file.close()
    print("Log file created")


write_log()

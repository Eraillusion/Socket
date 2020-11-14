import socket
# socket server program
import string
# string

HOST = 'appdev.lyle.smu.edu'        # localhost means your machine acts as server for local clients
PORT = 5730                       # CHANGE TO YOUR port

# --------------------
# Modify this function to return msg + name,id,& coding name
def processMsg(tank,x,y,speed,dire,dx,dy,tankb,speedb,direb):
        return "tank=" + tank + " x=" + x + " y=" + y + " speed=" + speed + " dir=" + dire + " dx=" + dx + " dy=" + dy + '\n' + tankb + "," + speedb + "," + direb

# -----------------------------------

#create socket object for Internet V4 and use streams to get/send data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#set up the socket on our PORT
s.bind((HOST, PORT))

#display a message to show we are alive
print ("Server waiting for a client on port " + str(PORT) )

keepListening = True

while (keepListening ):
        # listen( ) is synchronous - waits until client shows up
        # the parameter (backlog) sets the number of incoming that will be queued if busy
        s.listen(2)

        #when we get here a client has connected -
        # get the connection socket and address
        conn, addr = s.accept()

        print ('Client coming in from: ', addr    )

        #data comes in as bytes - here we receive 1024 bytes
        data = conn.recv(1024)

        #convert bytes to a string using decode so we can string concatenate
        serverData = data.decode()

        serverData.split(',')

        #do something with the incoming msg
        tank = serverData.split(',')[0]
        if tank in "TNK*1":
                tank = "t1"
        x = serverData.split(',')[1]
        y = serverData.split(',')[2]
        speed = serverData.split(',')[3]
        dire = serverData.split(',')[4]
        dx = serverData.split(',')[6]
        dy = serverData.split(',')[7]


        # Part B
        if int(dx) == int(x) and int(dy) > int(y):
                dire = "4"
        if int(dx) > int(x) and int(dy) > int(y):
                dire = "3"
        if int(dx) == int(x) and int(dy) < int(y):
                dire = "0"
        if int(dx) > int(x) and int(dy) < int(y):
                dire = "1"
        if int(dx) > int(x) and int(dy) == int(y):
                dire = "2"
        if int(dx) < int(x) and int(dy) == int(y):
                dire = "6"
        if int(dx) < int(x) and int(dy) < int(y):
                dire = "7"
        if int(dx) < int(x) and int(dy) > int(y):
                dire = "5"
        if int(dx) == int(x) and int(dy) == int(y):
                dire = "0"

        msg = processMsg(tank, x, y, speed, serverData.split(',')[4], dx, dy, tank, speed, dire)

        #use encode() to convert string back to bytes for transport back to client
        conn.sendall(msg.encode())

        keepListening = (serverData != 'bye')

#close down the connection and the server
conn.close()

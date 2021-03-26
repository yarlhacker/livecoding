from turtle import Turtle, done
s = ["blue", "red", "yellow", "purple", "green", "orange", "black", "pink"]
t = Turtle()
for i in range(5):
    t.color(s[i])
    t.fd(200)
    t.left(-144)
done()


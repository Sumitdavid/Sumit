def greet(fx: None) -> None:
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")

    return mfx()


@greet
def hello():
    print("Hello World")


@greet
def add(a: 1, b: 2):
    print(a + b)

# # hello()
# add(1,2)

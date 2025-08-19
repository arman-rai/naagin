with open("Notes.md", "a") as f:
    f.write("This is a context check ")

# custom context

class my_context:
    def __enter__(self):
        print("entering context....")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("exiting context....")

with my_context():
    print("in")
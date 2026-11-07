from flask import Flask, request, redirect, url_for
import random





high_or_low = Flask(__name__)
rnumber = random.randint(0, 9)
@high_or_low.route("/", methods=["GET", "POST"])

def home():

    if request.method == "POST":

        number = request.form.get("number", type=int)


        if number is None:

            return """
            <form method="POST">
                <div style="text-align: center;">
                
                <img src="/static/cho.png" alt="chogath" width="800" length = "800">
                
                
                
                </div>
            </form>
            
        
        """
        elif number == rnumber:
            return """
            <div style="text-align: center;">
                
                <img src="/static/toy.png" alt="cho" width="800" length = "800">
                
                
                
                </div>
            """
        elif number > rnumber:
            return """
            <div style="text-align: center;">
            <img src="/static/high.png" alt="highcho" width="800" length = "800">
            </div>
            """
        elif number < rnumber:
            return """
            <div style="text-align: center;">
            <img src="/static/low.png" alt="low_cho" width="800" length = "800">
            </div>
            """
        else :
            print(f"Secret number: {rnumber}")
            print(f"Your guess: {number}")


    return """
        <form method="POST">
            <div style="text-align: center;">
            <input 
            type="text" name="number"
            
            
            style="width: 300px; height: 40px;"
            
            >
            <button type="submit">Submit</button>
            </div>
        </form>
    """


if __name__ == "__main__":
    high_or_low.run(debug=True)


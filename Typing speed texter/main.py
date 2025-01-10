import tkinter as tk
import time


root = tk.Tk()
root['bg'] = 'violet'
root.title("Typing Speed Calculator")
root.geometry("600x450")


text_to_type = ("The quick brown fox jumps over the lazy dog. "
                "This sentence contains every letter in the English alphabet.")


start_time = None
end_time = None


instruction_label = tk.Label(root, text="Type the text below as fast as you can:", bg ='#FFF574', width = 70, font = ('Ariel',20,'bold'))
instruction_label.pack(pady=10)


text_label = tk.Label(root, text=text_to_type, wraplength=500, justify="center", bg = '#A1D6CB', font = ('Ariel',14,'italic'))
text_label.pack(pady=10)

input_text = tk.Text(root, height=5, width=50)
input_text.pack(pady=10)

result_label = tk.Label(root,bg = 'violet', text="", fg="red", font = ('Ariel',14), highlightthickness=0)
result_label.pack(pady=10)



def start_typing():
    global start_time
    start_time = time.time()
    input_text.delete(1.0, tk.END)  # Clear any previous input
    submit_button.config(state=tk.NORMAL)  # Enable the submit button



def calculate_speed():
    global start_time, end_time
    typed_text = input_text.get(1.0, tk.END).strip()

    if typed_text == text_to_type:
        end_time = time.time()
        time_taken = end_time - start_time
        words = len(typed_text.split())
        wpm = (words / time_taken) * 60  # words per minute
        result_label.config(text=f"Your typing speed is: {wpm:.2f} words per minute.")
    else:
        result_label.config(text="Oops! The text doesn't match. Try again.")

    submit_button.config(state=tk.DISABLED)  # Disable the submit button after submitting



start_button = tk.Button(root, text="Start Typing", command=start_typing, bg = '#00FF9C', width = 15,height = 3 , font = ('Ariel',12))
start_button.pack(pady=10)


submit_button = tk.Button(root, text="Submit", state=tk.DISABLED, command=calculate_speed, bg = '#FF8383', width = 10,height = 3 , font = ('Ariel',10))
submit_button.pack(pady=10)


root.mainloop()
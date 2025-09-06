

 🧮 Calculator with History

A simple Python-based calculator that not only performs basic arithmetic operations but also **saves your calculations to a history file (`history.txt`)**. You can view, clear, and manage your calculation history easily.



 🚀 Features

* Perform basic arithmetic: `+`, `-`, `*`, `/`
* Saves each calculation to a `history.txt` file
* View past calculations in reverse order (most recent first)
* Clear history when needed
* Prevents division by zero
* User-friendly input format



 📂 Example Usage


---------Simple calculator (type history , clear , exit)
Enter the calculation (+ - * /) or command (history , clear , exit) 3 + 5
Result: 8

Enter the calculation (+ - * /) or command (history , clear , exit) 10 * 2
Result: 20

Enter the calculation (+ - * /) or command (history , clear , exit) history
10 * 2 = 20
3 + 5 = 8

Enter the calculation (+ - * /) or command (history , clear , exit) clear
History cleared

Enter the calculation (+ - * /) or command (history , clear , exit) exit
Good bye




 ▶️ How to Run

 Prerequisites

* Python 3 installed on your system.

 Steps

1. Clone/download this repository.
2. Open the terminal (or command prompt).
3. Navigate to the project folder.
4. Run the program with:

python calculator.py




 🧩 Commands

* **Perform a calculation** → `number operator number` (example: `7 - 3`)
* **View history** → type `history`
* **Clear history** → type `clear`
* **Exit program** → type `exit`



 📝 Notes

* History is stored in `history.txt`.
* Calculations are displayed in reverse order (latest first).
* Whole number results (e.g., `8.0`) are automatically converted to integers (`8`).



 🎉 Future Improvements

* Add support for advanced operations (square root, power, modulus, etc.).
* Create a GUI version with buttons.
* Save history with timestamps.




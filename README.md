# **Horizon Cinemas**
## 🚀 **Getting Started**

This repository contains python module that creates a program for management and booking system of chain cinema company.

## 🖥️ **HOW TO USE**

In our system we have different views and systems in the directory allowing us to split the tasks in the program according to role, this all gets ran through the executable python file, horizon.py.
Once horizon.py has been started our GUI will appear with the sign in screen. These are the main logins we used for each user type.
View | Username | Password
------------- | -------------| -------------
Manager |sude_ceo | manager 
Admin |fi_admin |admin
Booking staff |cam_staff |staff

Once logged in a range of menus will show depending to which login was used Here is a quick explanation about what each page will do and how to use it.

## 🎯 **Features**
**1.Listings:** The listings page shows the films we show and where they are, simply select a film and see the information the user need. To continue with this process, we used a continue to booking button which takes the user to the booking page.

**2.Booking:** In this screen the user can select the Film they would like to see, select the date, updating the show times, after this they can select more ticket specific items such as ticket type and number of tickets, once the information has been selected, check availability can be pressed, providing the user with a price and allowing them to continue with the process. After filling out Personal information in the correct format they can place the booking.

**3.Cancellation:** If a customer wants a ticket cancelled they can get staff to go through the booking process, in this page the staff member simply needs the booking number given to the customer via the booking screen confirmation. Once this has been inputted the system will present options and allow the booking to be cancelled.

**4.Manage Screening:** The manage screening section provides a few very simple process; 

- Add film
- Remove Film
- Update Show Times
- Attach Shows to Screen

These processes all effect the database system.

**5.Generate Report:** This is where staff members can generate various reports based on the cinema’s performance and staff’s performance.

**6.Add cinema:** Give the information to add a new cinema and it will be added to the database allowing staff to then attach films and showing to the new cinema.

## 📚 **Packages** 
To use our booking system we have packages that are used to run the program;
- numpy 1.24.1 
- pandas 1.5.2
- tkcalendar 1.6.1
- python-dateutil 2.8.2

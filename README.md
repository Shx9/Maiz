# Maiz

This repo is a proof-of-concept for a Pakistan-based reservation startup that I and my partner were brainstorming in early 2022. The concept was to allow for restaurant + other SMB reservations in Pakistan, since most reservations/appointments are still recorded on physical ledgers. 

Although we tabled the idea due to market size considerations, amongst other reasons, I built out the basic web app (a) to formalize and further my understanding of the business idea, (b) to practice programming and (c) for fun.

The purpose of the web app is to essentially show how customers may readily access business information and make reservations, and how business owners can easily confirm reservations that will be sent to their phones. Ease of use and connecting to phones is particularly important in this market, as simplicity is a key criteria for users, smartphone penetration is growing, and smartphone usage for business needs is quite high. 

What this web app does:
- Utilizes Google Maps API to grab data on restaurants/businesses of the type that the user inputs
- Utilizes SendBlue.co's API to send mockup messages to the user's phone, indicating that they have confirmed a customer's reservation
- Has a semi-pretty UI

What this web app does not do:
- Doesn't have a databse, and as such, does not log in the user or store reservations

What I would add/change if I were to continue working on this:
- add a proper back-end
- add a 'favorites' feature
- build a calendar UI for easy appointment visualization
- build it in an android development language (e.g., Java) due to android penetration in Pakistan

Built with Python (Flask), as well as HTML, CSS (Bootstrap).
